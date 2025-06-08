# Custom Gaussian Naive Bayes (Binary Classification)

This repository contains a from-scratch implementation of the **Gaussian Naive Bayes (GNB)** algorithm for binary classification tasks, along with a comparison against Scikit-learn's built-in `GaussianNB`.

---

## What You'll Learn

- How GNB works under the hood
- Implementing probabilistic models from scratch using NumPy
- Comparing custom ML algorithms with Scikit-learn

---

## Project Structure
 ```
  GaussianNaiveBayes/ 
    ├── gaussian_nb.py # Custom implementation 
    ├── demo.ipynb # Interactive walkthrough 
    ├── demo_script.py # Script for terminal execution 
    ├── requirements.txt # Dependencies 
    └── README.md # You're reading it 
``` 
---

## Dataset

- **Breast Cancer Wisconsin (Diagnostic)** from `sklearn.datasets`
- Binary classification: `malignant (0)` vs `benign (1)`

---

## How to Run

### Option 1: Run the Notebook

```bash
jupyter notebook demo.ipynb
```
### Option 2: Run the Notebook

```bash
python demo_script.py
```
---

## Results(Sample)
```bash
[Custom GNB] Train Accuracy: 0.9780 | Test Accuracy: 0.9649

[Sklearn GNB] Train Accuracy: 0.9780 | Test Accuracy: 0.9737
```
