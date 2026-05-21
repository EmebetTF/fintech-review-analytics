from sklearn.feature_extraction.text import TfidfVectorizer

# Business-oriented themes
THEME_KEYWORDS = {

    "Account Access Issues": [
        "login",
        "password",
        "otp",
        "verification",
        "authenticate"
    ],

    "Transaction Performance": [
        "transfer",
        "transaction",
        "slow",
        "delay",
        "payment"
    ],

    "App Stability": [
        "crash",
        "freeze",
        "bug",
        "error",
        "loading"
    ],

    "UI and User Experience": [
        "interface",
        "design",
        "navigation",
        "layout",
        "easy"
    ],

    "Feature Requests": [
        "fingerprint",
        "biometric",
        "feature",
        "dark mode",
        "budget"
    ],

    "Customer Support": [
        "support",
        "help",
        "service",
        "response"
    ]
}


def extract_keywords(texts):
    """
    Extracts important keywords using TF-IDF.
    """

    vectorizer = TfidfVectorizer(
        max_features=100,
        ngram_range=(1, 2)
    )

    X = vectorizer.fit_transform(texts)

    return vectorizer.get_feature_names_out()


def assign_theme(text):
    """
    Assigns business theme to review.
    """

    text = str(text).lower()

    for theme, keywords in THEME_KEYWORDS.items():

        if any(keyword in text for keyword in keywords):
            return theme

    return "Other"