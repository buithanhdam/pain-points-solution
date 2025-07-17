import re

def preprocess(text: str) -> str:
    # Lowercase, remove punctuation (except for keywords)
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text