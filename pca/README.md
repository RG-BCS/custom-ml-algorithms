# PCA from Scratch (NumPy)

This project contains a clean, NumPy-only implementation of Principal Component Analysis (PCA), benchmarked against `scikit-learn`.

---

## Features

- Eigen decomposition-based PCA
- Standardization included
- Explained variance tracking
- Side-by-side comparison with `sklearn.decomposition.PCA`

---

## Project Structure

| File              | Description                            |
|-------------------|----------------------------------------|
| `pca.py`          | Custom PCA implementation              |
| `demo_script.py`  | CLI script for PCA + comparison        |
| `demo.ipynb`      | Visual demo with plotting              |
| `requirements.txt`| Python dependency list                 |
| `README.md`       | Documentation                          |

---

## Results Snapshot

```bash
Custom PCA shape: (124, 2)
Sklearn PCA shape: (124, 2)
```

___


> Visualization confirms both project into similar spaces with class separation.

---

## Educational Value

```bash
This implementation helps you understand:
- The role of eigenvectors/eigenvalues
- How PCA reduces dimensionality
- Tradeoffs in explained variance
```
---

