# Extractive Text Summarization

## 📌 Overview

This project explores **extractive text summarization** techniques, progressing from basic frequency-based methods to more advanced graph-based approaches. The project now includes:

- **Original method**: Frequency-based extractive summarizer (03-1_text_summarization.ipynb)
- **Enhanced version**: Advanced TextRank implementation with evaluation (03-2_text_summarization_expanded.ipynb)
- **Real-world dataset**: CNN/DailyMail news articles and summaries
- **Evaluation framework**: Automatic ROUGE scoring for objective comparison

## 🎯 Problem Statement

In the age of information overload, manually reading and summarizing large documents is time-consuming. Automated text summarization algorithms can quickly identify key information and produce concise summaries, making them invaluable for:

- Research analysts processing reports
- Journalists summarizing articles
- Students reviewing academic papers
- Business professionals handling documents

## 📂 Data Sources

### CNN/DailyMail Dataset

We use the standard CNN/DailyMail summarization dataset containing:

- **News articles** from CNN and the Daily Mail
- **Professional summaries** (highlights) for each article
- **Diverse topics**: Politics, business, technology, entertainment, etc.
- **Standard benchmark**: Enables comparison with state-of-the-art methods

### Project Data Structure

```bash
03_text_summarization/
├── data/
│   ├── raw/                    # Original text files
│   ├── cnn_dailymail/          # CNN/DM dataset cache
│   └── sample/                 # Sample articles for testing
├── scripts/
│   ├── data_loader.py          # Dataset loading utilities
│   └── requirements.txt         # Project dependencies
├── notebooks/
│   ├── 03-2_text_summarization_expanded.ipynb  # Enhanced notebook (TextRank)
│   └── 03-1_text_summarization.ipynb           # Original frequency-based notebook
└── README.md                   # Project documentation
```

### Data Acquisition

The CNN/DailyMail dataset is loaded using the Hugging Face `datasets` library. A sample of articles is cached locally for quick access during development.

## 🔧 Preprocessing & Data Cleaning

### Data Quality Issues Addressed

- **Text formatting**: Inconsistent paragraph breaks, extra whitespace
- **Special characters**: HTML entities, punctuation variations
- **Stop words**: Common words that add little semantic value
- **Case sensitivity**: Mixed uppercase/lowercase text
- **Sentence boundaries**: Abbreviations causing incorrect tokenization

### Enhanced Cleaning Pipeline

1. **Text normalization**: Remove citation brackets, extra whitespace, special characters
2. **Sentence tokenization**: NLTK's sentence tokenizer with abbreviation handling
3. **Word tokenization**: Split sentences into words
4. **Stopword removal**: Filter out common English stopwords
5. **Lemmatization**: Reduce words to their base forms (e.g., "running" → "run")
6. **Length filtering**: Skip very short sentences to improve quality

## 🛠 Tools & Tech Stack

| Category | Tools & Libraries |
|----------|-------------------|
| Core | Python 3.8, NLTK 3.8, NumPy 1.24, Hugging Face Datasets |
| Text Processing | NLTK Tokenizers, Regex, WordNet Lemmatizer |
| Evaluation | rouge-score (ROUGE metrics) |
| Development | Jupyter Notebook, Git |

## 📊 Methodology

### Original Frequency-Based Method (03-1_text_summarization.ipynb)

1. **Word Frequency Analysis**: Count word occurrences, excluding stop words
2. **Sentence Scoring**: Sum word frequencies for each sentence
3. **Threshold Selection**: Select sentences scoring above median frequency

### Advanced TextRank Method (03-2_text_summarization_expanded.ipynb)

1. **Similarity Matrix**: Calculate cosine similarity between sentence vectors
2. **Graph Construction**: Sentences as nodes, similarity as edges
3. **PageRank Algorithm**: Compute importance scores iteratively
4. **Top-K Selection**: Select highest-scoring sentences as summary

### Evaluation Framework

- **ROUGE-1**: Unigram overlap with reference summary
- **ROUGE-2**: Bigram overlap with reference summary
- **ROUGE-L**: Longest common subsequence similarity

## 🚀 How to Run

### Setup

```bash
# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies with pinned versions
pip install -r scripts/requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### Execution

```bash
# Navigate to project
cd 03_text_summarization

# Launch Jupyter Notebook
jupyter notebook notebooks/03-2_text_summarization_expanded.ipynb
# or
jupyter notebook notebooks/03-1_text_summarization.ipynb
```

## 📝 Dependencies

- Python 3.8+
- nltk==3.8.1
- numpy==1.24.3
- datasets==2.14.0
- rouge-score==2.0.1

## 📚 References

- NLTK Documentation: https://www.nltk.org/
- TextRank: Bringing Order into Texts (Mihalcea & Tarau, 2004)
- CNN/DailyMail Dataset: https://huggingface.co/datasets/cnn_dailymail
- ROUGE: A Package for Automatic Evaluation of Summaries (Lin, 2004)

## 🤝 License

MIT — See LICENSE file for details.

### 🤖 AI-Augmented Development
This expanded notebook (03-2_text_summarization_expanded.ipynb) was created with the assistance of an AI agent (Hermes/Atemis) following a structured delegation workflow. The AI analyzed requirements, designed the project structure, implemented the code, and ensured educational quality. This demonstrates a modern approach to rapid prototyping and learning with AI as a collaborative partner.

---
**Workflow**: Requirement analysis → Project design → Implementation → Evaluation → Documentation