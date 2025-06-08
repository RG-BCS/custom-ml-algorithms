# Perceptron from Scratch (Binary Classification)

This project contains a minimal yet complete implementation of the **Perceptron algorithm** — one of the earliest and simplest types of artificial neural networks — built from scratch using **NumPy**.

The model is applied to a binary classification task using the **Iris dataset**, and visualized using `matplotlib`.

---

## What You'll Learn

- How the Perceptron learning algorithm works internally
- How to implement a simple neural classifier from scratch
- How to visualize decision boundaries in 2D
- The difference between zero-initialized and randomly-initialized weights

---

## Folder Structure

```
perceptron/
    ├── perceptron.py # Core implementation of the Perceptron class
    ├── utils.py # Utility functions (e.g., decision boundary plotting)
    ├── demo_script.py # Script to train, plot, and evaluate
    ├── demo.ipynb # Interactive version for notebooks
    ├── requirements.txt # Required packages
    └── README.md # You're reading it!
```

---


---

## 📊 Dataset

- **Iris Dataset** from `sklearn.datasets`
- Binary classification: **Setosa (0)** vs **Versicolor (1)**
- Using only two features: **Sepal Length** and **Petal Length**

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

## Requirements

``` bash
pip install -r requirements.txt
```
---

## Notes
```bash
- Uses stochastic updates (one sample at a time)  
- No loss function in the traditional sense — updates are based on sign errors  
- Great starting point for understanding neural networks & linear classifiers
```
