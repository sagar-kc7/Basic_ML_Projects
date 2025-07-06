[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sagar-kc7/Basic_ML_Projects/blob/main/student-mat/student_mat.ipynb)


# 🎓 Student Performance Prediction using Regression (Student-Mat Dataset)

This project aims to predict students' final grade (`G3`) using a regression pipeline that includes advanced preprocessing techniques and machine learning models.

---

## 📁 Project Structure

- `notebooks/` - Jupyter Notebooks with EDA, modeling, and evaluation
- `data/` - Dataset (`student-mat.csv`)
- `README.md` - Project documentation

---

## ✅ Step-by-Step Workflow

### 1. 🧹 Data Preprocessing
- **Dataset**: `student-mat.csv` from UCI Machine Learning Repository
- Cleaned data, converted categorical variables to numerical using encoding.
- Explored basic statistics and visualized feature distributions, correlations, and relationships with the target `G3`.

### 2. 🔧 Feature Transformation
- Applied **Yeo-Johnson transformation** using `PowerTransformer` to make feature distributions more Gaussian.
  - Yeo-Johnson works for both positive and negative values (unlike Box-Cox).
- Followed by **StandardScaler** to normalize the data.

### 3. ✂️ Feature Selection
- Used **Lasso Regression (L1 penalty)** to select only important features.
- Filtered out features with low coefficients to reduce dimensionality and improve generalization.

### 4. 🧪 Outlier Analysis
- Checked for outliers using box plots, IQR, and Z-score methods.
- Optional removal of outliers based on their impact on model performance.

### 5. 🤖 Model Training & Evaluation

#### 🔁 Cross-validation:
- Applied **5-fold cross-validation** using `cross_val_score` to evaluate model performance.

#### 🌲 Random Forest Regressor:
- **Best Performance**:
  - Cross-validated R²
  - **Mean CV R²**
  - **Test R²**
  - **Me**


#### ⚡ XGBoost Regressor:
- Cross-validated R²
- **Mean CV R²**
- **Test R²**
- **MSE**
- Did not outperform Random Forest in the current setup

---

## 🛠️ Tools & Libraries

- Python (pandas, numpy, matplotlib, seaborn)
- scikit-learn
- XGBoost
- Jupyter Notebook

---
