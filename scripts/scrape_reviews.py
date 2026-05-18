from google_play_scraper import reviews, Sort
import pandas as pd


apps = {
    "CBE": "PUT_REAL_APP_ID_HERE",
    "BOA": "PUT_REAL_APP_ID_HERE",
    "Dashen": "PUT_REAL_APP_ID_HERE"
}


all_reviews = []

for bank, app_id in apps.items():
    print(f"Scraping {bank}...")

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=500
    )

    for review in result:
        all_reviews.append({
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"].strftime("%Y-%m-%d"),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

print("Before cleaning:", df.shape)

# Drop missing values
df = df.dropna(subset=["review", "rating"])

# Remove duplicates
df = df.drop_duplicates(subset=["review"])

print("After cleaning:", df.shape)

df.to_csv("data/raw/cleaned_reviews.csv", index=False)

print("Saved successfully.")