import pandas as pd
import src

from src.preprocessing import clean_text
from src.sentiment import (
    get_sentiment,
    normalize_sentiment
)
from src.thematic_analysis import assign_theme


# Load cleaned review dataset
df = pd.read_csv("data/raw/cleaned_reviews.csv")

print("Dataset loaded successfully.")

# Create review IDs
df["review_id"] = range(1, len(df) + 1)

# Preserve original review text
df["review_text"] = df["review"]

# Clean text
print("Cleaning text...")

df["clean_review"] = df["review_text"].apply(clean_text)

# Sentiment analysis
print("Running sentiment analysis...")

results = df["review_text"].apply(get_sentiment)

df["raw_label"] = results.apply(lambda x: x[0])
df["sentiment_score"] = results.apply(lambda x: x[1])

# Normalize labels
df["sentiment_label"] = df.apply(
    lambda row: normalize_sentiment(
        row["raw_label"],
        row["sentiment_score"]
    ),
    axis=1
)

# Theme assignment
print("Assigning themes...")

df["identified_theme"] = df["clean_review"].apply(assign_theme)

# Final dataframe
final_df = df[
    [
        "review_id",
        "review_text",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "rating",
        "date",
        "bank",
        "source"
    ]
]

# Save results
final_df.to_csv(
    "data/raw/sentiment_analysis.csv",
    index=False
)

print("Pipeline completed successfully.")