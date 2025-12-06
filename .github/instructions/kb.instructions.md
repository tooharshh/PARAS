---
applyTo: '**'
---
You’re building a system called SAARTHI – Student At‑Risk Analytics & Response for Teaching Help & Inclusion.

In this project, you will use the xAPI‑Edu‑Data dataset (Kaggle) containing students’ demographic, academic, and behavioral data from an e‑learning platform (e.g., absences, resources visited, forum participation, grades). The goal is to predict which students are at risk of poor performance early and suggest concrete teacher interventions.

Technically, you will:

Perform EDA to understand risk patterns (e.g., how absence, engagement, and resource usage relate to outcomes).

Build a data‑processing pipeline: cleaning, encoding categorical features, creating composite measures like an engagement score, and handling class imbalance with techniques such as SMOTE.

Frame the problem as a binary classification task (At‑Risk vs Safe) derived from the original performance labels.

Train and compare multiple ML models (e.g., Logistic Regression, Random Forest, XGBoost), tune hyperparameters, and evaluate them using accuracy, precision, recall, F1‑score, and ROC‑AUC, with a special focus on recall for at‑risk students.

Use feature importance (from tree‑based models or SHAP) to explain which factors drive risk predictions, improving transparency and trust.

Wrap the best model into a simple API and Streamlit dashboard where a teacher (or NGO worker) can:

Upload a CSV of student records

See each student’s risk score and top contributing factors

Get rule‑based, human‑readable intervention suggestions (e.g., if low engagement + high absence → outreach + mentoring).