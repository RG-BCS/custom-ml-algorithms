# 🔍 KNN From Scratch (NumPy)

This project provides a from-scratch implementation of the K-Nearest Neighbors (KNN) algorithm using NumPy, with benchmarking against scikit-learn's version.

---

## 🚀 Features

- Clean KNN implementation from scratch
- Vectorized Minkowski distance computation
- Support for Euclidean, Manhattan distances
- `predict_proba` support
- Jupyter Notebook demo + CLI demo script

---

## 📁 File Structure

```
| File             | Description                        |
|------------------|------------------------------------|
| `knn.py`         | Custom KNN implementation          |
| `demo_script.py` | CLI demo script                    |
| `demo.ipynb`     | Interactive Jupyter demo           |
| `requirements.txt`| Python dependencies               |
| `README.md`      | Project overview                   |
```

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

## 📦 Installation

```bash
git clone https://github.com/yourusername/custom-knn.git
cd custom-knn
pip install -r requirements.txt
```

---

📊 Sample Output

```bash
Custom KNN       → Train: 0.9780, Test: 0.9561
scikit-learn KNN → Train: 0.9780, Test: 0.9561
```

