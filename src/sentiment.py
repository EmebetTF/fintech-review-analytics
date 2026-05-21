from transformers import pipeline

# Load transformer model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def get_sentiment(text):
    """
    Returns raw sentiment and confidence score.
    """

    result = classifier(str(text))[0]

    label = result["label"]
    score = result["score"]

    return label, score


def normalize_sentiment(label, score):
    """
    Converts transformer output into:
    Positive / Negative / Neutral
    """

    if score < 0.60:
        return "Neutral"

    if label == "POSITIVE":
        return "Positive"

    return "Negative"