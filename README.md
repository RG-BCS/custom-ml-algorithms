# custom-ml-algorithms

A curated collection of **classic machine learning algorithms**, all implemented from scratch using **Python and NumPy** — without relying on high-level ML libraries like scikit-learn.

This repo focuses on building a deep understanding of the **inner mechanics** of machine learning models, optimization, and evaluation techniques.  
It’s ideal for learning, teaching, interviews, and showcasing applied ML knowledge.

---

## What's Included

| Category              | Algorithms / Techniques                                         |
|-----------------------|-----------------------------------------------------------------|
| **Linear Models**      | Adaline (GD & SGD), Perceptron, Linear Regression (L1 & L2)     |
| **Logistic Regression**| Binary & Multiclass, Early Stopping, Regularization             |
| **Bayesian Models**    | Gaussian Naive Bayes                                            |
| **Instance-Based**     | k-Nearest Neighbors (KNN)                                       |
| **Ensemble Methods**   | Bagging, Majority Voting Classifier                             |
| **Dimensionality Reduction** | Principal Component Analysis (PCA)                        |
| **Model Selection**    | k-Fold Cross Validation, Train/Test Split, Manual Grid Search   |

---

## Project Goals

- Reinforce understanding of ML fundamentals through first-principles implementations  
- Gain hands-on experience with optimization (GD, SGD), regularization, and evaluation  
- Build models that mimic core scikit-learn behavior — but with full transparency  
- Showcase ability to go beyond library usage and into core algorithm mechanics

---

## 📈 Highlights

- **Built from scratch** — zero reliance on scikit-learn internals  
- **Gradient Descent** with early stopping and learning rate schedules  
- **Multiclass Logistic Regression** with softmax activation  
- **Manual cross-validation** and performance metrics  
- PCA with visualization for dimensionality reduction  
- **Bagging & ensemble logic** using pure Python  

---

## Example Use

```python
from linear_models.logistic_regression import LogisticRegression

model = LogisticRegression(learning_rate=0.1, max_iter=1000, regularization="l2")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


