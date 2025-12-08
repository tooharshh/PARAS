# PARAS
**P**redictive **A**nalytics for **R**isk & **A**cademic **S**upport - An early warning system that predicts at-risk students and suggests personalized interventions using Machine Learning.

## About

→ I built this project to understand how machine learning can help identify struggling students before they fall behind. The challenge was interesting because I had to work with imbalanced data (only 24% of students are at-risk) and figure out which behavioral signals actually matter for academic success.

→ The system uses three different ML models (Logistic Regression, Random Forest, XGBoost) to predict student risk levels, and provides a Streamlit dashboard where teachers can analyze individual students or upload entire class rosters.

→ I also built a rule-based intervention engine that generates specific, actionable recommendations based on what's causing a student to be at-risk.

## About the Dataset

The dataset I used is the [xAPI-Edu-Data from Kaggle](https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data). What makes this dataset realistic is that it captures actual e-learning platform behavior - not just demographics and grades, but how students interact with the system.

The data is imbalanced - only 115 students (24%) are low-performing, which made model training challenging.

## Model Training Results

I trained and compared three different models:

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | ~87% | ~82% | ~85% | ~83% |
| Random Forest | ~90% | ~86% | ~88% | ~87% |
| XGBoost | ~89% | ~84% ~87% | ~85% |

**Random Forest** performed best overall, which makes sense because it can capture non-linear relationships between features like engagement and attendance.

**Recall** is the most important metric here - we want to catch as many at-risk students as possible, even if it means some false positives.

## Problems I Faced

### 1. Class Imbalance
Only 24% of students were at-risk. I tried SMOTE (Synthetic Minority Over-sampling) to balance the training data, which improved recall significantly from ~72% to ~85%.

### 2. Feature Engineering
The raw features weren't enough. I created an **engagement_score** by combining:
- Raised hands
- Resources visited  
- Announcements viewed
- Discussion participation

This composite feature became the strongest predictor of risk.

### 3. Choosing the Right Model
Started with Logistic Regression (simple, interpretable), but Random Forest captured complex patterns better. XGBoost was slightly worse, probably because the dataset is small (480 students) and tree-based ensembles need more data.

## Tech Stack

• Python 3.13  
• Streamlit  
• scikit-learn  
• XGBoost  
• SMOTE (imbalanced-learn)  
• Pandas & NumPy  
• Plotly (interactive visualizations)  
• Matplotlib & Seaborn  

## Quick Start

### Run with Streamlit

```bash
# Clone the repo
git clone https://github.com/tooharshh/PARAS.git
cd PARAS

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run preprocessing to create data files
# Open preprocessing.ipynb and run all cells

# Train a model (Random Forest recommended)
# Open model_random_forest.ipynb and run all cells

# Launch dashboard
streamlit run app.py
```

## What I Learned

→ **Feature engineering beats fancy models** - Creating engagement_score had more impact than switching from Logistic Regression to XGBoost.

→ **SMOTE actually works** - Without it, models would just predict "safe" for everyone and get 76% accuracy.

## License

MIT License - See [LICENSE](LICENSE) file for details.

---
