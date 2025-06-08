# Custom Linear Regression

This repository contains a custom implementation of Linear Regression with support for:

- L1 and L2 regularization (penalty)
- Early stopping based on loss convergence
- Full batch gradient descent optimization

The implementation is designed for educational purposes and to demonstrate core ML algorithm principles.

---

## Files

```bash
- `linear_regression_custom.py`: Implementation of `LinearRegressionCustom` class and utility plotting function.
- `demo.ipynb`: Jupyter notebook demonstrating data loading, training, visualization, and comparison with scikit-learn.
- `demo_script.py`: Script version of the demo notebook for quick command-line testing.
- `requirements.txt`: Python package dependencies.
```

---

## Model Parameters

```bash
- n_iter: Number of iterations (epochs) for training.

- learning_rate: Gradient descent step size.

- C: Regularization strength (inverse).

- penalty: 'l1' or 'l2' regularization.

- early_stopping: Patience for early stopping.

- eps: Minimum improvement threshold for stopping.
```

---

## Usage

### 1. Clone the repository

```bash
git clone <repository_url>
cd <repository_folder>

---

## Install dependencies
```bash
pip install -r requirements.txt
```
---

## Run the demo
```bash
jupyter notebook demo.ipynb

. Or run the script:

python demo_script.py
```
---

## Results

The demo notebook/script trains the model on the Ames Housing dataset and compares the prediction results to scikit-learn's LinearRegression model.

