# Adaline from Scratch — Gradient Descent & Stochastic Gradient Descent

This project implements the Adaptive Linear Neuron (Adaline) algorithm **from scratch**, using both **batch gradient descent (GD)** and **stochastic gradient descent (SGD)**.

It's part of a series of custom machine learning algorithm implementations aimed at gaining deep insight into the inner workings of classical models.

---

## 🔍 What’s Inside

- `adaline_gd.py` – Adaline with Batch Gradient Descent  
- `adaline_sgd.py` – Adaline with Stochastic Gradient Descent  
- `utils.py` – Utility for plotting decision regions  
- `demo.ipynb` – Interactive notebook: training, visualization & comparison  
- `demo_script.py` – Script version of the notebook (optional)
- `requirements.txt` – Dependencies for easy setup

---

## 📊 Dataset

We use a subset of the **Iris dataset**, focusing on binary classification (Setosa vs. Versicolor) using two features:

- Sepal length  
- Petal length

---

## Key Concepts

| Feature                     | AdalineGD (Batch GD)           | AdalineSGD (Stochastic GD)    |
|----------------------------|-----------------------------------------------------------------|
| Weight Update              | Once per epoch (entire dataset) | Per training sample           |
| Convergence                | Stable but may be slow          | Faster updates, noisier path  |
| Loss Function              | Mean Squared Error (MSE)        | Same                          |
| Suitable For               | Smaller datasets                | Large-scale or streaming data |

---

## 🛠️ How to Run

### 1. Clone the repo or navigate to this subfolder
```bash
git clone https://github.com/your_username/custom-ml-algorithms.git
cd custom-ml-algorithms/adaline

