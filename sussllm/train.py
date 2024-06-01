import torch
from torch.utils.data import DataLoader
from transformers import AdamW, RobertaTokenizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import ndcg_score, label_ranking_average_precision_score
import numpy as np
from typing import List, Dict

from models.ranking_model import RankingModel
from dataset import SearchSessionDataset, DatasetManager
from utils.evaluation_metrics import calculate_mrr, calculate_ndcg


def train(model, data_loader, optimizer, device):
    model.train()
    total_loss = 0
    for batch in data_loader:
        optimizer.zero_grad()
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        token_type_ids = batch['token_type_ids'].to(device)
        labels = batch['labels'].to(device)
        outputs = model(input_ids, attention_mask, token_type_ids)
        loss = torch.nn.functional.binary_cross_entropy_with_logits(outputs.squeeze(), labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(data_loader)

def evaluate(model, data_loader, device):
    model.eval()
    y_true = []
    y_pred = []
    with torch.no_grad():
        for batch in data_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            token_type_ids = batch['token_type_ids'].to(device)
            labels = batch['labels'].to(device)
            outputs = model(input_ids, attention_mask, token_type_ids)
            y_true.append(labels.cpu().numpy())
            y_pred.append(outputs.cpu().numpy())
    y_true = np.concatenate(y_true, axis=0)
    y_pred = np.concatenate(y_pred, axis=0)
    mrr = label_ranking_average_precision_score(y_true, y_pred)
    ndcg = ndcg_score([y_true], [y_pred], k=3)
    return mrr, ndcg


def load_datasets(aol_file_path: str, trec_file_path: str) -> List[Dict]:
    dataset_manager = DatasetManager('dummy_path.json')

    # Load AOL and TREC data
    aol_data = dataset_manager.load_aol_data(aol_file_path)
    trec_data = dataset_manager.load_trec_data(trec_file_path)

    # This is a placeholder for the actual processing you would need to do
    queries = [data_point['query'] for data_point in trec_data]
    docs = [data_point['clicks'] for data_point in trec_data]  
    labels = [1 if data_point else 0 for data_point in trec_data]  

    return queries, docs, labels


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load and prepare your dataset
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    queries, docs, labels = load_datasets('datasets/aol/aol_data.csv', 'datasets/trec/sessiontrack2014.xml')
    dataset = SearchSessionDataset(queries, docs, labels, tokenizer)
    train_dataset, val_dataset = train_test_split(dataset, test_size=0.1)

    train_data_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)
    val_data_loader = DataLoader(val_dataset, batch_size=2)
    
    

    model = RankingModel().to(device)
    optimizer = AdamW(model.parameters(), lr=5e-6)

    for epoch in range(3):  
        train_loss = train(model, train_data_loader, optimizer, device)
        mrr, ndcg = evaluate(model, val_data_loader, device)

        print(f'Epoch {epoch+1}, Train Loss: {train_loss:.4f}, MRR: {mrr:.4f}, nDCG: {ndcg:.4f}')

if __name__ == '__main__':
    main()
    
    
    