# Fintech Review Analytics

## Customer Experience Analytics for Fintech Apps

A real-world data analytics and data engineering project focused on scraping, analyzing, and visualizing Google Play Store reviews for Ethiopian banking applications.

This project was completed as part of the **10 Academy Artificial Intelligence Mastery – Week 2 Challenge**.

---

## Project Overview

Mobile banking adoption in Ethiopia is growing rapidly, and customer reviews on the Google Play Store provide valuable, unfiltered feedback about product quality, usability, reliability, and customer satisfaction.

This project analyzes customer reviews from three major Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to transform raw user reviews into actionable business insights through:

- Data Collection and Preprocessing
- Sentiment Analysis
- Thematic Analysis
- PostgreSQL Database Design
- Data Visualization
- Business Recommendations

---

## Business Objective

Omega Consultancy is advising Ethiopian banks on how to improve their mobile banking applications and retain customers in a competitive fintech environment.

This project helps product teams understand:

- What users love most
- What frustrates users most
- Which recurring issues need urgent attention
- Which features customers want next
- How competitors compare in customer experience

---

## Project Structure

```text
fintech-review-analytics/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── data/
│   └── raw/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── src/
│   └── __init__.py
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```

---

## Database Setup

### PostgreSQL Installation

Install PostgreSQL on your system. Refer to the [official documentation](https://www.postgresql.org/download/) for platform-specific instructions.

### Database Creation

Create a new database for the project:

```bash
createdb fintech_reviews
```

### Schema Design

The database consists of two main tables: `banks` and `reviews`.

- `banks`: Stores metadata about each bank.
- `reviews`: Stores processed user reviews and sentiment analysis results.

### Insertion Script

Use the provided SQL scripts in the `scripts/` directory to create tables and insert data:

```bash
psql -d fintech_reviews -f scripts/create_tables.sql
psql -d fintech_reviews -f scripts/insert_data.sql
```

---

## Schema Overview

### banks Table

Stores metadata for each bank, such as:

- `bank_id` (Primary Key)
- `name`
- `app_package`
- `created_at`

### reviews Table

Stores processed reviews and sentiment results, including:

- `review_id` (Primary Key)
- `bank_id` (Foreign Key)
- `user_name`
- `review_text`
- `rating`
- `sentiment`
- `created_at`

---

## Verification Queries

To validate the database and data integrity, use the following queries:

- **Count reviews per bank:**
  ```sql
  SELECT b.name, COUNT(r.review_id) AS review_count
  FROM banks b
  JOIN reviews r ON b.bank_id = r.bank_id
  GROUP BY b.name;
  ```

- **Average ratings:**
  ```sql
  SELECT b.name, AVG(r.rating) AS avg_rating
  FROM banks b
  JOIN reviews r ON b.bank_id = r.bank_id
  GROUP BY b.name;
  ```

- **Null validation:**
  ```sql
  SELECT COUNT(*) FROM reviews WHERE review_text IS NULL OR sentiment IS NULL;
  ```

---