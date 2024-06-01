import sys
import os
import json
from sklearn.metrics import ndcg_score, mean_squared_error
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sussllm.utils.logger import setup_logger

def load_dataset(file_path):
    """Load the dataset from a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def calculate_mrr(ground_truths, predictions):
    """Calculate the Mean Reciprocal Rank (MRR) for the given predictions."""
    mrr_total = 0
    for true_answers, preds in zip(ground_truths, predictions):
        rank = 1
        for pred in preds:
            if pred in true_answers:
                mrr_total += 1 / rank
                break
            rank += 1
    return mrr_total / len(ground_truths)

def evaluate_model(dataset_path, model):
    """Evaluate the given model using the specified dataset."""
    logger.info("Loading dataset...")
    dataset = load_dataset(dataset_path)
    predictions = []
    ground_truths = []
    
    logger.info("Predicting...")
    for data_point in dataset:
        query = data_point['query']
        correct_documents = data_point['correct_documents']
        predicted_ranking = model.predict(query)
        predictions.append(predicted_ranking)
        ground_truths.append(correct_documents)

    logger.info("Calculating Metrics...")
    mrr = calculate_mrr(ground_truths, predictions)
    ndcg = ndcg_score([ground_truths], [predictions])
    
    logger.info(f"Mean Reciprocal Rank (MRR): {mrr}")
    logger.info(f"Normalized Discounted Cumulative Gain (nDCG): {ndcg}")

if __name__ == "__main__":
    logger = setup_logger('evaluation_logger', 'evaluation.log')
    dataset_path = 'data/dataset.json'  # Path to the dataset
    model_path = 'data/model.pkl'       # Path to the trained model

    # evaluate_model(dataset_path, model)
