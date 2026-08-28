# Codveda Level 3 — Advanced

Level 3 of the Codveda internship: classification, a dashboard, and NLP.

## Task 1 — Classification (`level3_task1_classification.py`)

Telecom churn prediction using Codveda's own 80/20 train/test split.

I encoded the categorical columns (State, International plan, Voice mail
plan) with LabelEncoder fit on the training set only, then transformed the
test set — fitting separately would let the category codes drift between
the two.

Compared three models:

| Model | Accuracy | F1 |
|---|---|---|
| Logistic Regression | 0.853 | 0.258 |
| Decision Tree | 0.918 | 0.715 |
| Random Forest | 0.946 | 0.775 |
| Random Forest (tuned) | **0.955** | **0.826** |

The tuned random forest used max_depth=20, min_samples_split=5,
n_estimators=100, chosen by grid search with 3-fold CV on F1.

Accuracy is the wrong headline metric here — only about 14% of customers
churn, so predicting "no churn" every time scores ~86% accuracy while
being useless. F1 is what I paid attention to.

## Task 2 — Dashboard (`level3_task2_dashboard.py`)

The brief said Power BI or Tableau. Power BI doesn't run on Linux, so I
built the dashboard in Streamlit instead — same job, works on my machine.

It loads the cleaned sentiment data, computes a 3-class sentiment
(positive / negative / neutral) with VADER, and shows:

- sentiment distribution (443 positive, 185 negative, 82 neutral)
- top emotions
- likes per year
- retweets vs likes
- engagement by platform

All of it is filterable from the sidebar (sentiment, platform, year).

Run it with:

```bash
streamlit run level3_task2_dashboard.py
```

(from the parent folder, since it reads `level1_basic/cleaned_sentiment_dataset.csv`)

If you'd rather see it in Tableau, there's a guide in
`L3_TASK2_TABLEAU_GUIDE.md`.

## Task 3 — NLP Sentiment Analysis (`level3_task3_nlp.py`)

Tokenized, removed stopwords and lemmatized the text with nltk, then scored
sentiment with VADER.

One detail that mattered: I scored the *original* text, not the cleaned
tokens. VADER reads punctuation and capitalisation as intensity signals
("great!!!" scores higher than "great"), so stripping those first makes it
less accurate, not more.

Results: 443 positive, 185 negative, 82 neutral.

## Running

```bash
python3 -m venv venv && source venv/bin/activate
pip install pandas numpy matplotlib scikit-learn nltk wordcloud
python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('vader_lexicon')"
python3 level3_task1_classification.py
python3 level3_task3_nlp.py
```

The raw CSVs are in the parent `data/` folder of the main project.
