# Logistic Regression from Scratch

This repository implements **binary** and **multiclass logistic regression** using **gradient descent**, built completely from scratch using NumPy. It includes functionality such as regularization, early stopping, and is benchmarked against `scikit-learn` to ensure correctness and practical usability.

---

## 📁 Folder Structure

```
logistic_regression/
  ├── logistic_binary.py # Binary logistic regression using gradient descent
  ├── logistic_multiclass.py # Multiclass logistic regression (softmax) with L1/L2 regularization
  ├── utils.py # Utility functions (e.g., decision boundary plotting)
  ├── demo_script.py # End-to-end demo for binary & multiclass classification
  ├── requirements.txt
  └── README.md
```

---

## 📌 Features

### ✅ Binary Logistic Regression
- Implements logistic regression using the sigmoid function
- Full-batch gradient descent optimization
- Option to standardize input features
- Visualizes decision boundaries on 2D datasets (Iris)

### ✅ Multiclass Logistic Regression
- Uses softmax activation for multi-class classification
- Trains with cross-entropy loss
- Regularization support:
  - **L1** (Lasso)
  - **L2** (Ridge)
- Early stopping if the loss plateaus
- Probabilistic predictions with `predict_proba`

---

## 📊 Demos Included

### Binary Classification
- Dataset: **Iris** (class 0 vs 1 only)
- Decision boundary plotted using `plot_decision_region`
- Uses `LogisticRegression_` from `logistic_binary.py`

### Multiclass Classification
- Dataset: **Digits**
- Model: `MultiClassLogisticRegression` vs `sklearn.linear_model.LogisticRegression`
- Accuracy comparison shown on test set
- Uses the full softmax classifier and measures against scikit-learn’s baseline

---

## 🚀 How to Run

### Option 1: Run the notebook

```bash
jupyter notebook demo.ipynb
```
**Option 2: Run the script**
```bash
python demo_script.py
```

---

=== Binary Classification Demo (Iris Dataset) ===
```bash
[Decision boundary plot shown]
```

---

=== Multiclass Classification Demo (Digits Dataset) ===
```bash
Sklearn Logistic Regression Accuracy: 0.961
Custom Logistic Regression Accuracy: 0.951
```
