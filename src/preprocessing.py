import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    """
    Cleans review text using:
    - lowercase conversion
    - tokenization
    - stopword removal
    - punctuation removal
    - lemmatization
    """

    doc = nlp(str(text).lower())

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.like_num
        and len(token.text) > 2
    ]

    return " ".join(tokens)