# Titanic Survival Analysis

## 📌 Overview
This project is an in-depth exploratory data analysis (EDA) and predictive modeling task based on the famous Titanic dataset. It investigates the factors that influenced passenger survival, such as class, age, gender, and family size. This project serves as a classic demonstration of data science workflows from cleaning to insight generation.

## 🎯 Problem Statement
The sinking of the Titanic is one of the most infamous shipwrecks in history. While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others. This analysis answers the question: "What sorts of people were more likely to survive?"

## 🛠 Tools & Tech Stack
- **Python**: Core language.
- **Pandas**: Extensive use for data manipulation, null value imputation, and feature engineering.
- **Seaborn & Matplotlib**: Used for visualizing distributions, survival rates, and correlation heatmaps.
- **NumPy**: Numerical operations.
- **Domain Focus**: Classification (Survival), Feature Engineering, Demographic Analysis.

## 📊 Methodology
1. **Data Cleaning**:
   - **Imputation**: Filled missing `Age` values with the median and `Embarked` with the mode.
   - **Handling Nulls**: Identified and visualized missing data patterns.
2. **Feature Engineering**:
   - **Family Size**: Created a new feature combining `SibSp` (Siblings/Spouses) and `Parch` (Parents/Children) to analyze the impact of traveling with family.
3. **Exploratory Analysis**:
   - **Demographics**: Analyzed survival rates by Gender, Pclass (Passenger Class), and Embarked port.
   - **Distributions**: Visualized Age and Fare distributions for survivors vs. non-survivors.
   - **Correlations**: Generated heatmaps to identify strong relationships between variables.

## 🔑 Key Findings
- **Gender**: Female passengers had a significantly higher survival rate than males.
- **Class status**: Passenger Class 1 had the highest survival rate, indicating socio-economic status played a roll.
- **Age**: Children had a higher chance of survival, consistent with the "women and children first" protocol.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Navigate to the notebooks directory:
   ```bash
   cd notebooks
   ```
3. Open the analysis notebook:
   ```bash
   jupyter notebook "02-1_titanic_survival_analysis.ipynb"
   ```
