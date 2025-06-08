# Custom C# Custom Cross-Validation Utility

This repository contains a custom implementation of k-fold cross-validation supporting multiple scoring metrics including accuracy, precision, recall, and F1-score.

## Features

- Supports non-stratified and stratified (binary classification) k-fold splits
- Random seed control for reproducibility
- Implements common classification metrics
- Compares results to scikit-learn for validation

## Usage

```python
from cross_val_score import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
clf = LogisticRegression(max_iter=500)

scores = cross_val_score(clf, X_scaled, y, cv=5, scoring='f1-score', random_state=42)
print("F1 scores:", scores)
print("Mean F1:", scores.mean())
