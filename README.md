# Codveda Level 3 — Advanced (Data Analytics Internship)

Daniel Quoby Soglo · quobydaniels@gmail.com

Three tasks on the **Telecom churn** and **Sentiment** datasets. All run end-to-end; numbers are real output.

## Tasks

### 1. Predictive Modeling — Classification (`level3_task1_classification.py`)
- Dataset: Telecom customer churn (Codveda 80/20 split).
- LabelEncoder (train-only fit), StandardScaler, Logistic Regression / Decision Tree / Random Forest, grid search on RF.
- **Result (F1 / accuracy):** LR 0.258/0.853 · DT 0.715/0.918 · RF 0.775/0.946 · **Tuned RF 0.826/0.955** (`max_depth=20, min_samples_split=5, n_estimators=100`).

### 3. NLP — Sentiment Analysis (`level3_task3_nlp.py`)
- Dataset: cleaned sentiment data (Level 1 output).
- Tokenize/stopword/lemmatize; VADER on original text (±0.05 thresholds); word cloud.
- **Result:** Positive 443 · Negative 185 · Neutral 82.

### 2. Interactive Dashboard — Streamlit ✅
- **Status:** completed with a self-hosted Streamlit dashboard (`level3_task2_dashboard.py`) — Linux-friendly equivalent of Power BI/Tableau.
- **What it does:** loads the cleaned sentiment data, computes 3-class sentiment via VADER, and shows interactive charts — sentiment distribution, top emotions, likes per year, retweets vs likes, engagement by platform — all filterable from the sidebar.
- **Verified:** boots clean (`streamlit run` → health check `ok`); 3-class sentiment matches Task 3 (443 Positive / 185 Negative / 82 Neutral).
- **Alternative:** Tableau Public (`L3_TASK2_TABLEAU_GUIDE.md`) for a publishable dashboard-with-URL if you prefer the named tool.

## Charts
All PNGs under `plots/`.

## Reproduce
```bash
python3 -m venv venv && source venv/bin/activate
pip install pandas numpy matplotlib scikit-learn nltk wordcloud
python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('vader_lexicon')"
python3 level3_task1_classification.py
python3 level3_task3_nlp.py
```

*Raw datasets ship in the parent Codveda bundle (`data/`). Copy them next to this folder to run.*