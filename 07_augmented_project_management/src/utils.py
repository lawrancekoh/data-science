import re
import string
import spacy

# Initialize spacy model
# User must allow downloading if not present, but good practice is to load global resource once
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Warning: Spacy model 'en_core_web_sm' not found. Functions using it may fail.")
    print("Please run: python -m spacy download en_core_web_sm")
    nlp = None

def clean_text(text):
    """
    Basic text cleaning: lowercase, remove brackets, punctuation, newlines.
    """
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('\\W', ' ', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def parse_text(text):
    """
    Advanced processing using Spacy: entity preservation, lemmatization, stopword removal.
    """
    if nlp is None:
        return text
    
    sent = nlp(text)
    ents = {x.text: x for x in sent.ents}
    tokens = []
    for w in sent:
        if w.is_stop or w.is_punct or w.is_digit:
            continue
        if w.text in ents:
            tokens.append(w.text)
        else:
            tokens.append(w.lemma_.lower())
    
    text = ' '.join(tokens)
    text = re.sub(r'[,-]', ' ', text)
    return text
