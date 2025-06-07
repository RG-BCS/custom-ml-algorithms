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

<dl> <dt><strong>AdalineGD</strong></dt> <dd>Uses batch gradient descent — weight updates are performed after evaluating the entire dataset.</dd> <dt><strong>AdalineSGD</strong></dt> <dd>Uses stochastic gradient descent — weights are updated per individual sample, enabling faster but noisier convergence.</dd> <dt><strong>Loss Function</strong></dt> <dd>Mean Squared Error (MSE) is used to measure prediction error and guide weight updates.</dd> <dt><strong>Activation Function</strong></dt> <dd>Identity function; the raw net input is used directly (linear activation).</dd> <dt><strong>Standardization</strong></dt> <dd>Feature standardization (zero mean and unit variance) is crucial for stable and fast convergence.</dd> </dl>
---

## 🛠️ How to Run

### 1. Clone the repo or navigate to this subfolder
```bash
git clone https://github.com/your_username/custom-ml-algorithms.git
cd custom-ml-algorithms/adaline

