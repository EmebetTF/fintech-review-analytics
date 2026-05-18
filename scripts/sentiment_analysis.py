import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load dataset
df = pd.read_csv("data/raw/cleaned_reviews.csv")

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()


def classify_sentiment(text):
    score = analyzer.polarity_scores(str(text))["compound"]

    if score >= 0.05:
        label = "Positive"
    elif score <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return pd.Series([label, score])


df[["sentiment_label", "sentiment_score"]] = df["review"].apply(classify_sentiment)

print(df[["review", "sentiment_label", "sentiment_score"]].head())

df.to_csv("data/raw/sentiment_analysis.csv", index=False)

print("Sentiment analysis completed successfully.")