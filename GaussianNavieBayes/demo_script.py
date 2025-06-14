# -*- coding: utf-8 -*-
"""perceptron.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vBkRx3zcZqLB5_Zuq6uHAsPLXGc655Hl
"""

# demo_script.py

"""
Command-line demo of custom Gaussian Naive Bayes vs Scikit-learn GNB
"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB as SklearnGNB

from gaussian_nb import GaussianNaiveBayes_

def run_demo():
    # Load dataset
    data = load_breast_cancer()
    X, y = data.data, data.target

    # Train/test split
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Feature scaling
    scaler = StandardScaler()
    x_train_sc = scaler.fit_transform(x_train)
    x_test_sc = scaler.transform(x_test)

    # Initialize both models
    custom_model = GaussianNaiveBayes_()
    sklearn_model = SklearnGNB()

    # Train
    custom_model.fit(x_train_sc, y_train)
    sklearn_model.fit(x_train_sc, y_train)

    # Evaluation
    print(f"[Custom GNB] Train Accuracy: {custom_model.score(x_train_sc, y_train):.4f} | Test Accuracy: {custom_model.score(x_test_sc, y_test):.4f}")
    print(f"[Sklearn GNB] Train Accuracy: {sklearn_model.score(x_train_sc, y_train):.4f} | Test Accuracy: {sklearn_model.score(x_test_sc, y_test):.4f}")

if __name__ == "__main__":
    run_demo()