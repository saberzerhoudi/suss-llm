import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, jaccard_score, ndcg_score
from nltk.translate.bleu_score import sentence_bleu
from bert_score import score as bert_score

def calculate_term_overlap_rate(query1, query2):
    """
    Calculate Term Overlap Rate (Tau) using Jaccard similarity between two queries.
    
    Parameters:
    - query1: First query as a list of terms.
    - query2: Second query as a list of terms.
    
    Returns:
    - Term Overlap Rate as a float.
    """
    set1 = set(query1)
    set2 = set(query2)
    return jaccard_score(set1, set2)

def calculate_bleu(reference, candidate):
    """
    Calculate BLEU score for a single reference and a candidate sentence.
    
    Parameters:
    - reference: Reference sentence as a list of words.
    - candidate: Candidate sentence as a list of words.
    
    Returns:
    - BLEU score as a float.
    """
    return sentence_bleu([reference], candidate)

def calculate_bert_score(reference, candidate):
    """
    Calculate BERTScore for a pair of sentences.
    
    Parameters:
    - reference: Reference sentence as a string.
    - candidate: Candidate sentence as a string.
    
    Returns:
    - Precision, Recall, and F1 BERTScores as floats.
    """
    P, R, F1 = bert_score([reference], [candidate], lang="en")
    return P.mean().item(), R.mean().item(), F1.mean().item()

def calculate_click_stopping_metrics(y_true, y_pred):
    """
    Calculate accuracy, precision@10, recall@10, and F1-score for click and stopping behaviors.
    
    Parameters:
    - y_true: True labels as a list.
    - y_pred: Predicted labels as a list.
    
    Returns:
    - Dictionary with accuracy, precision@10, recall@10, and F1-score.
    """
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision@10": precision_score(y_true, y_pred, average='micro', k=10),
        "recall@10": recall_score(y_true, y_pred, average='micro', k=10),
        "F1-score": f1_score(y_true, y_pred, average='micro')
    }
    return metrics

def calculate_mrr(y_true, y_pred_scores):
    """
    Calculate the Mean Reciprocal Rank (MRR) for the given predictions.
    
    Parameters:
    - y_true: A list of lists where each sublist contains the indices of relevant documents.
    - y_pred_scores: A list of lists of scores predicted by the model.
    
    Returns:
    - MRR score as a float.
    """
    mrr_score = 0.0
    for true_labels, scores in zip(y_true, y_pred_scores):
        # Sort scores and get indices
        sorted_indices = np.argsort(scores)[::-1]
        # Find the rank of the first relevant document
        rank = 1
        for idx in sorted_indices:
            if idx in true_labels:
                mrr_score += 1.0 / rank
                break
            rank += 1
    mrr_score /= len(y_true)
    return mrr_score

def calculate_ndcg(y_true, y_pred_scores, k=3):
    """
    Calculate the Normalized Discounted Cumulative Gain (nDCG) at rank k.
    
    Parameters:
    - y_true: A list of binary lists indicating the relevance of each document.
    - y_pred_scores: A list of lists of scores predicted by the model.
    - k: Rank at which to calculate nDCG.
    
    Returns:
    - nDCG score as a float.
    """
    return ndcg_score(y_true, y_pred_scores, k=k)



if __name__ == "__main__":
    # Example data
    y_true = [[0, 2], [1], [2, 3]]
    y_pred_scores = [[0.1, 0.2, 0.3], [0.1, 0.4, 0.35], [0.5, 0.2, 0.1, 0.4]]
    y_true_binary = [[0, 0, 1], [0, 1, 0], [0, 0, 1, 1]]

    mrr = calculate_mrr(y_true, y_pred_scores)
    ndcg = calculate_ndcg(y_true_binary, y_pred_scores, k=3)

    print(f"MRR: {mrr}")
    print(f"nDCG@3: {ndcg}")