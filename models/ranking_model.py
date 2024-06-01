import torch
from torch.utils.data import Dataset
from transformers import RobertaModel, RobertaTokenizer, AdamW


class SearchSessionDataset(Dataset):
    def __init__(self, queries, docs, labels, tokenizer, max_length=512):
        self.queries = queries
        self.docs = docs
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.queries)

    def __getitem__(self, idx):
        query = self.queries[idx]
        doc = self.docs[idx]
        label = self.labels[idx]

        inputs = self.tokenizer.encode_plus(
            query, doc, add_special_tokens=True, max_length=self.max_length,
            return_token_type_ids=True, padding='max_length', truncation=True,
            return_attention_mask=True, return_tensors='pt'
        )

        return {
            'input_ids': inputs['input_ids'].flatten(),
            'attention_mask': inputs['attention_mask'].flatten(),
            'token_type_ids': inputs['token_type_ids'].flatten(),
            'labels': torch.tensor(label, dtype=torch.float)
        }
        
        
class RankingModel(torch.nn.Module):
    def __init__(self):
        super(RankingModel, self).__init__()
        self.roberta = RobertaModel.from_pretrained('roberta-base')
        self.classifier = torch.nn.Linear(self.roberta.config.hidden_size, 1)

    def forward(self, input_ids, attention_mask, token_type_ids):
        outputs = self.roberta(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        pooled_output = outputs[1]
        logits = self.classifier(pooled_output)
        return logits
    

