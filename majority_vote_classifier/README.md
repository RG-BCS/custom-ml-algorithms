# 🧠 Majority Vote Classifier

A custom ensemble learning implementation that combines multiple base classifiers using majority voting. Supports both **class label** and **probability-based** voting strategies, fully compatible with the `scikit-learn` API, including pipelines and `GridSearchCV`.

---

## 📁 Project Structure

```bash
majority_vote_classifier/
    │
    ├── majority_vote_classifier.py # Custom ensemble classifier
    ├── utils.py # Utility function for plotting decision boundaries
    ├── demo_script.py # Simple script for running the classifier
    ├── demo.ipynb # Jupyter notebook with full explanation and visualizations
    ├── requirements.txt # List of Python dependencies
    ├── README.md # Project overview and usage instructions
```

---


---

## Features
```bash
- Combines classifiers via majority voting
- Supports:
  - `'classlabel'` voting
  - `'probability'` voting
  - Optional weights for classifiers
- Compatible with `scikit-learn` utilities (e.g., `Pipeline`, `GridSearchCV`)
- Fully documented and extensible
- Includes cross-validation, ROC, PR curves, and decision region visualizations
```

---

## How to Run

### Option 1: Run Demo Script

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the demo script
python demo_script.py
```

### Option 2: Use Jupyter Notebook

```bash
# Launch Jupyter
jupyter notebook demo.ipynb

The notebook contains:

-Cross-validation scores
-ROC & Precision-Recall curves
-Decision boundary plots

```
---

## Requirements

```bash
numpy
matplotlib
scikit-learn
```

---

## Background

Ensemble methods combine the predictions of multiple models to produce better generalization.
This project implements a custom majority voting ensemble that mimics the functionality of VotingClassifier, but allows deeper customization and inspection.

---

# Use Cases

-Experimenting with ensemble methods in custom pipelines
-Teaching or learning ML ensembling concepts
-Extending voting behavior for more complex tasks (e.g., time-series or NLP classifiers)
