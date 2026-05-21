import pandas as pd
import psycopg2


# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="YOUR_PASSWORD" # replace your own postgres password
)

cursor = conn.cursor()

print("Database connected successfully.")


# Load processed review dataset
df = pd.read_csv("data/raw/sentiment_analysis.csv")

print(df.head())


# Insert banks

banks = [

    ("Commercial Bank of Ethiopia", "CBE Mobile"),
    ("Bank of Abyssinia", "BOA Mobile Banking"),
    ("Dashen Bank", "Dashen Mobile Banking")
]

insert_bank_query = """

INSERT INTO banks (bank_name, app_name)

VALUES (%s, %s)

ON CONFLICT DO NOTHING;
"""

for bank in banks:
    cursor.execute(insert_bank_query, bank)

conn.commit()

print("Banks inserted successfully.")


# Fetch bank IDs

cursor.execute("SELECT bank_id, bank_name FROM banks")

bank_rows = cursor.fetchall()

bank_mapping = {}

for row in bank_rows:
    bank_mapping[row[1]] = row[0]

print(bank_mapping)


insert_review_query = """

INSERT INTO reviews (

    review_id,
    bank_id,
    review_text,
    rating,
    review_date,
    sentiment_label,
    sentiment_score,
    identified_theme,
    source

)

VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);

"""


for _, row in df.iterrows():

    full_bank_name = bank_name_mapping[row["bank"]]

    bank_id = bank_mapping[full_bank_name]

    values = (

        int(row["review_id"]),
        int(bank_id),
        row["review_text"],
        int(row["rating"]),
        row["date"],
        row["sentiment_label"],
        float(row["sentiment_score"]),
        row["identified_theme"],
        row["source"]
    )

    cursor.execute(insert_review_query, values)


conn.commit()

print("Reviews inserted successfully.")


cursor.close()
conn.close()

print("Database connection closed.")