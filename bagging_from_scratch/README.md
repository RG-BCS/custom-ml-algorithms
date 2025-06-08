# Bagging From Scratch

An implementation of Bagging (Bootstrap Aggregating) using decision trees — built completely from scratch using scikit-learn's API conventions. 

Compare the results with sklearn’s `BaggingClassifier` to understand the underlying mechanics and performance.

---

## Folder Structure

```bash
bagging_from_scratch/

    ├── bagging_classifier.py           # BaggingFromScratch class with docstrings and clean code
    ├── demo.ipynb                      # Notebook walkthrough: training, comparison, plots
    ├── demo_script.py                  # Run it directly, terminal-friendly
    ├── utils.py                        # Plot decision boundaries
    ├── README.md                       # Professional project overview (enhanced again)
    ├── requirements.txt                # Dependencies

```

---

## Highlights

```bash
- Implements bagging using bootstrap resampling manually
- Compatible with `GridSearchCV`, pipelines
- Compares from-scratch implementation vs. sklearn built-in ensemble
- ROC curves, decision boundary plots, and AUC metrics
```
---

## Running the Code

### Option 1: Command-Line

```bash
pip install -r requirements.txt
python demo_script.py
```

### Option 2: Jupyter Notebook

```bash
jupyter notebook demo.ipynb
```

---

## Visual Results

```bash
-ROC curve comparisons
-Decision boundaries for custom and sklearn ensembles
-Accuracy on training vs test set
```

---

## Educational Use

```bash
This project is ideal for:

-Learning about ensemble methods
-Understanding bootstrapping and overfitting
-Comparing hand-crafted ML techniques with library abstractions
```



