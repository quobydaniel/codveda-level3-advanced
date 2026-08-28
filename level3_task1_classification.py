"""
Level 3 (Advanced) - Task 1: Predictive Modeling (Classification)
Dataset: Telecom customer churn (Codveda's own 80/20 train/test split)
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Codveda provides an 80/20 split already.
train = pd.read_csv('../data/churn-bigml-80.csv')
test = pd.read_csv('../data/churn-bigml-20.csv')
print("Train:", train.shape, "| Test:", test.shape)


def preprocess(df, encoders=None, fit=False):
    df = df.copy()
    cat_cols = ['State', 'International plan', 'Voice mail plan']
    if fit:
        encoders = {}
        for col in cat_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoders[col] = le
    else:
        # Fit encoders on train only, reuse on test.
        for col in cat_cols:
            df[col] = encoders[col].transform(df[col])
    df['Churn'] = df['Churn'].astype(int)
    return df, encoders


train_p, encoders = preprocess(train, fit=True)
test_p, _ = preprocess(test, encoders=encoders, fit=False)

X_train, y_train = train_p.drop(columns=['Churn']), train_p['Churn']
X_test, y_test = test_p.drop(columns=['Churn']), test_p['Churn']

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
}

results = []
for name, m in models.items():
    m.fit(X_train_s, y_train)
    preds = m.predict(X_test_s)
    # F1 matters more than accuracy - churn is a minority class.
    results.append({
        'Model': name,
        'Accuracy': accuracy_score(y_test, preds),
        'Precision': precision_score(y_test, preds),
        'Recall': recall_score(y_test, preds),
        'F1-score': f1_score(y_test, preds),
    })

results_df = pd.DataFrame(results).set_index('Model').round(3)
print("\nModel comparison:")
print(results_df)

# Hyperparameter tuning via grid search, cross-validated on F1
print("\nRunning grid search on Random Forest...")
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
}
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid,
                     cv=3, scoring='f1', n_jobs=-1)
grid.fit(X_train_s, y_train)
best_preds = grid.best_estimator_.predict(X_test_s)

print(f"Best params: {grid.best_params_}")
print(f"Tuned Random Forest -> Accuracy: {accuracy_score(y_test, best_preds):.3f}, "
      f"F1: {f1_score(y_test, best_preds):.3f}")

plt.figure()
results_df.plot(kind='bar', ax=plt.gca())
plt.title('Classification Model Comparison')
plt.ylabel('Score')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('plots/model_comparison.png', dpi=120)
plt.close()

print("\nSaved plot -> plots/model_comparison.png")
