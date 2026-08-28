"""
Level 3 (Advanced) - Task 3: Natural Language Processing (NLP) - Sentiment Analysis
Dataset: Cleaned sentiment dataset (output of Level 1 Task 1 - run that first)
"""

import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud

df = pd.read_csv('../level1_basic/cleaned_sentiment_dataset.csv')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocess(text):
    """Tokenize, drop stopwords/punctuation, lemmatize."""
    tokens = word_tokenize(str(text).lower())
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    return [lemmatizer.lemmatize(t) for t in tokens]


# This cleaned/lemmatized text is used ONLY for the word-frequency /
# word-cloud step below - word frequency should ignore filler words
# like "the"/"and".
df['tokens'] = df['Text'].apply(preprocess)
df['clean_text'] = df['tokens'].apply(lambda t: ' '.join(t))

# VADER scores the ORIGINAL text, not the cleaned version. It's a
# rule-based lexicon that reads punctuation ("!!!") and capitalization
# ("AMAZING") as intensity signals, so stripping those first would make
# it LESS accurate, not more.
sia = SentimentIntensityAnalyzer()
df['compound'] = df['Text'].apply(lambda t: sia.polarity_scores(str(t))['compound'])

# These thresholds (+/- 0.05) are VADER's own documented cutoffs for
# classifying positive/negative vs. neutral.
df['Predicted_Sentiment'] = df['compound'].apply(
    lambda c: 'Positive' if c >= 0.05 else ('Negative' if c <= -0.05 else 'Neutral')
)

print("Predicted sentiment distribution:")
print(df['Predicted_Sentiment'].value_counts())

plt.figure()
df['Predicted_Sentiment'].value_counts().plot(
    kind='bar', color=['#2ecc71', '#95a5a6', '#e74c3c'])
plt.title('Predicted Sentiment Distribution (VADER)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('plots/sentiment_distribution.png', dpi=120)
plt.close()

wc = WordCloud(width=1000, height=600, background_color='white', max_words=100)
wc.generate(' '.join(df['clean_text']))
plt.figure(figsize=(10, 6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('Most Frequent Words')
plt.tight_layout()
plt.savefig('plots/wordcloud.png', dpi=120)
plt.close()

print("\nSaved plots -> plots/sentiment_distribution.png, plots/wordcloud.png")
