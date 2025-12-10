# 🏦 Loan Prediction Machine Learning Project  
*A Machine Learning Model for Predicting Loan Approval*

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![ML](https://img.shields.io/badge/Category-Machine%20Learning-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📘 Overview

Loan approval is a critical decision-making process for financial institutions.  
This project builds a **machine learning classification model** that predicts whether a loan application should be *approved* or *rejected* based on applicant and loan features.

The aim is to provide a clean, end-to-end data science workflow that demonstrates:
- Real-world data preprocessing
- Insightful exploratory data analysis (EDA)
- Feature engineering
- Model building and evaluation
- Business insights backed by data

---

## 🎯 Project Objectives

- Understand factors influencing loan approvals  
- Build and compare different machine learning models  
- Achieve high accuracy and explainability  
- Provide insights that financial institutions can use  

---

## 📂 Repository Structure

Loan_Prediction_ML_Project/ │ ├── notebooks/ │   └── Loan_Prediction_ML_project.ipynb │ ├── data/ │   ├── raw/ │   └── processed/ │ ├── src/ │   ├── data_preprocessing.py │   ├── model_training.py │   └── utils.py │ ├── images/ │   └── visualizations/ │ ├── models/ │   └── trained_model.pkl │ ├── requirements.txt └── README.md

---

## 📊 Dataset Information

The dataset includes demographic and financial details such as:

- Gender  
- Marital Status  
- Number of Dependents  
- Education & Employment Status  
- Applicant & Coapplicant Income  
- Loan Amount & Duration  
- Credit History  
- Property Area  

**Target Variable:** `Loan_Status` (Y/N)

---

## 🔎 Exploratory Data Analysis (EDA)

Key insights explored:
- Income distribution and its effect on loan approval  
- Credit history as the strongest predictor  
- Loan amount patterns across different applicant categories  
- Property area trends  
- Detection of missing values and outliers  

This section includes:
- Histograms  
- Boxplots  
- Countplots  
- Correlation heatmaps  
- Feature comparisons  

---

## 🤖 Machine Learning Models Used

- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier  
- Support Vector Machine (optional)  
- Gradient Boosting (optional)

---

## 🏆 Model Performance Summary

| Model | Accuracy | F1 Score | Notes |
|-------|----------|----------|-------|
| Logistic Regression | 0.82 | — | Baseline model |
| Random Forest | 0.86 | — | Best performance |
| Decision Tree | 0.78 | — | Overfitting tendencies |

*(Replace with your actual metrics if different)*

---

## 🧠 Key Business Insights

- Applicants with **credit history = 1** are significantly more likely to get loan approval.  
- Higher applicant income does *not always* guarantee approval — credit rating is more influential.  
- Urban property areas show higher approval rates.  
- Applicants with shorter loan terms often have better chances of approval.  

---

## ▶️ How to Run This Project

1. Clone this repository  
   ```bash
   git clone https://github.com/Dhebbyfolami/Loan_Prediction_ML_Project.git

2. Install required libraries

pip install -r requirements.txt


3. Open Jupyter Notebook

jupyter notebook


4. Run the notebook

notebooks/Loan_Prediction_ML_project.ipynb




---

🚀 Future Enhancements

Add hyperparameter tuning using GridSearchCV

Deploy model using Streamlit or Flask

Add SHAP values for interpretability

Create an automated prediction API



---

💬 Contact

Your Name
📧 Email: dhebbyfolasayomi97@gmail.com
🔗 GitHub: https://github.com/Debbyfolami
💼 LinkedIn: Oluwasayo Adeola


---

📝 License

This project is licensed under the MIT License.

---
