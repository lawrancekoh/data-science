"""
Data loading utilities for the text summarization project.
Provides functions to load and cache the CNN/DailyMail dataset.
"""

from datasets import load_dataset
import os
import pickle

DATA_DIR = "../data/cnn_dailymail"
CACHE_FILE = "cnn_dailymail_sample.pkl"

def load_cnn_dailymail(sample_size=None, use_cache=True):
    """
    Load a sample of the CNN/DailyMail dataset.
    
    Args:
        sample_size: Number of examples to load (None for all)
        use_cache: Whether to use cached data if available
        
    Returns:
        List of dictionaries with 'article' and 'highlights' keys
    """
    cache_path = os.path.join(os.path.dirname(__file__), DATA_DIR, CACHE_FILE)
    
    if use_cache and os.path.exists(cache_path):
        print(f"Loading from cache: {cache_path}")
        with open(cache_path, 'rb') as f:
            return pickle.load(f)
    
    print("Loading CNN/DailyMail dataset...")
    dataset = load_dataset('cnn_dailymail', '3.0.0', split='train', streaming=True)
    
    data = []
    for i, example in enumerate(dataset):
        if sample_size and i >= sample_size:
            break
        data.append({
            'article': example['article'],
            'highlights': example['highlights']
        })
    
    # Cache the data
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, 'wb') as f:
        pickle.dump(data, f)
    
    return data

def save_text_files(data, output_dir="raw"):
    """
    Save articles and highlights as separate text files.
    
    Args:
        data: List of article/highlights dictionaries
        output_dir: Directory to save files
    """
    articles_dir = os.path.join(os.path.dirname(__file__), DATA_DIR, output_dir, "articles")
    highlights_dir = os.path.join(os.path.dirname(__file__), DATA_DIR, output_dir, "highlights")
    
    os.makedirs(articles_dir, exist_ok=True)
    os.makedirs(highlights_dir, exist_ok=True)
    
    for i, item in enumerate(data):
        # Save article
        with open(os.path.join(articles_dir, f"article_{i:04d}.txt"), 'w', encoding='utf-8') as f:
            f.write(item['article'])
        
        # Save highlights (reference summary)
        with open(os.path.join(highlights_dir, f"highlights_{i:04d}.txt"), 'w', encoding='utf-8') as f:
            f.write(item['highlights'])
    
    print(f"Saved {len(data)} articles and highlights to {output_dir}/")

# Example usage
if __name__ == "__main__":
    data = load_cnn_dailymail(sample_size=10)
    save_text_files(data, output_dir="sample")