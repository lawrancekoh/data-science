# Data Science Portfolio

## Overview
Welcome to my data science portfolio. This repository showcases my expertise in data analysis, visualization, and machine learning through seven diverse real-world projects. The projects range from analyzing global COVID-19 data and predicting Titanic survival rates to implementing text summarization, sentiment analysis, customer segmentation, fake news detection, and AI-augmented project management. Each project demonstrates my proficiency in Python and essential data science libraries including pandas, scikit-learn, NLTK, TensorFlow and more, while solving complex analytical challenges using techniques like statistical analysis, machine learning, natural language processing, and visualizations.

## Projects

### 1. COVID-19 Global Impact Analysis
A comprehensive analysis of the COVID-19 pandemic using data from "Our World in Data". This project demonstrates:

- **Advanced Data Visualization** using:
  - Multi-axis plots for comparing cases and deaths
  - Time series trend analysis
  - Box plots for yearly distribution analysis
  - Bar plots for continental comparisons
  - Interactive user-input driven visualizations
- **Statistical Analysis** including:
  - Fatality rate calculations and trends
  - Regional distribution analysis
  - Year-wise monthly trend analysis
- **Data Processing Techniques**:
  - Missing value imputation
  - Feature engineering (e.g., daily growth rates)
  - Data cleaning and preprocessing
  - Time-based aggregations

[View Project](./01_covid19_analysis/notebooks/01_covid19_global_analysis.ipynb)

### 2-1. Titanic Survival Analysis
An exploratory data analysis of the famous Titanic dataset, investigating factors that influenced passenger survival. Key analyses include:

- **Data Cleaning & Preprocessing**:
  - Missing value imputation for Age and Embarked columns
  - Feature engineering (Family Size calculation)
  - Data type handling and column management
- **Statistical Analysis**:
  - Survival rates by passenger class
  - Age distribution analysis
  - Fare analysis and correlation with survival
  - Family size impact on survival
- **Passenger Demographics**:
  - Class distribution
  - Embarkation port analysis
  - Age and gender distribution
- **Key Findings**:
  - Higher class passengers had better survival rates
  - Age correlation with survival outcomes
  - Family size influence on survival chances
  - Port of embarkation survival patterns

[View Project](./02_titanic_analysis/notebooks/02-1_titanic_survival_analysis.ipynb)

### 2-2. Titanic Data Visualizations
A comprehensive visualization study of the Titanic dataset, focusing on different aspects of passenger demographics and their relationships. Features include:

- **Survival Analysis Visualizations**:
  - Distribution of survivors vs non-survivors
  - Class-wise passenger distribution
  - Age distribution analysis
- **Passenger Demographics Visualization**:
  - Age distribution through histograms
  - Class distribution analysis
  - Fare distribution through box plots
- **Correlation Analysis**:
  - Heatmap of numerical variables
  - Relationship between age and passenger class
- **Technical Implementation**:
  - Seaborn for statistical visualizations
  - Matplotlib for custom plots
  - NumPy and Pandas for data handling

[View Project](./02_titanic_analysis/notebooks/02-2_titanic_visualisations.ipynb)

### 3. Text Summarization
A simple project demonstrating text summarization techniques. This project showcases:

- **Natural Language Processing (NLP)**:
  - Text preprocessing and tokenization
  - Frequency-based summarization
  - Implementation of basic NLP techniques
- **Data Handling**:
  - Text data cleaning and preparation
  - Handling of large text datasets

[View Project](./03_text_summarization/notebooks/03_text_summarization.ipynb)

### 4. Hotel Sentiment Analysis
An analysis of hotel reviews to understand sentiment trends and correlations between different aspects of hotel services and overall guest satisfaction. This project includes:

- **Data Import and Setup**: Utilizes libraries such as `pandas`, `numpy`, `scipy`, and `matplotlib` for data manipulation and visualization.
- **Data Loading**: Reads hotel review data from an Excel file, including sentiment scores and star ratings.
- **Data Analysis**:
  - Sentiment Analysis: Calculates sentiment scores for hotel aspects like room, service, location, food, and value.
  - Correlation Analysis: Examines the relationship between overall guest satisfaction (GRI) and specific sentiments for different star categories.
  - Visualization: Includes code for visualizing data trends and correlations.
- **Statistical Testing**: Uses Pearson correlation tests to determine dependencies between overall satisfaction and specific sentiment scores.

[View Project](./04_sentiment_analysis/notebooks/04_sentiment_analysis.ipynb)

### 5. Customer Segmentation using RFM Analysis
This project involves analyzing transaction data to segment customers based on Recency, Frequency, and Monetary Value (RFM) metrics. Key features include:

- **Data Import and Setup**: Utilizes libraries such as `pandas`, `numpy`, `scipy`, and `matplotlib` for data manipulation and visualization.
- **Data Loading**: Reads transaction data from a CSV file, including transaction dates and amounts.
- **RFM Analysis**:
  - Calculation of Recency, Frequency, and Monetary Value for each customer.
  - Segmentation of customers into quantiles for scoring.
  - Grouping customers by RFM scores to identify most valuable, loyal, and at-risk customers.
- **Visualization**: Plots distributions of RFM metrics and customer segments.

[View Project](./05_customer_segmentation/notebooks/05_customer_segmentation.ipynb)

### 6. Fake News Detection
This project focuses on detecting fake news using Natural Language Processing (NLP) techniques. Key features include:

- **Data Description**:
  - The dataset includes text data from social media and news platforms, along with content tags and labels indicating the truthfulness of the content.
  - Labels are categorized as: Half-True, False, Mostly-True, True, Barely-True, and Not-Known.
- **Data Preprocessing**:
  - Handling missing values in the dataset.
  - Reclassification of labels into binary categories: Fake News (1) and Real News (0).
- **Modeling**:
  - Utilizes various machine learning models such as Logistic Regression, Naive Bayes, Random Forest, and Gradient Boosting.
  - Implements a Stacking Classifier to combine the predictions of multiple models for improved accuracy.
- **Evaluation**:
  - The models are evaluated based on metrics like Accuracy, Precision, Recall, and ROC_AUC.
  - The Stacking Classifier is used to make final predictions on the test set.
- **Visualization**:
  - The distribution of predictions is visualized to understand the model's performance.

[View Project](./06_fake_news_detection/notebooks/06_fake_news_detection.ipynb)

### 7. AI-Augmented Project Management
This capstone project leverages AI and machine learning to enhance project management processes. Key features include:

- **Data Import and Setup**: Utilizes libraries such as `pandas`, `numpy`, `scipy`, and `matplotlib` for data manipulation and visualization.
- **Data Loading**: Reads project task data from an Excel file, including task descriptions and associated labels.
- **Text Preprocessing**:
  - Cleaning and tokenization of text data using regular expressions and NLP libraries like `spacy`.
  - Lemmatization and removal of stop words to prepare text for analysis.
- **Modeling**:
  - Implementation of machine learning models such as Naive Bayes, Random Forest, and Gradient Boosting for task classification.
  - Use of a Stacking Classifier to improve model performance by combining multiple models.
- **Evaluation**:
  - Models are evaluated using metrics like Accuracy and F1 Score.
  - Visualization of model performance through confusion matrices.
- **Visualization**:
  - Distribution of task labels is visualized to understand the dataset.

[View Project](./07_augmented_project_management/notebooks/07_augmented_project_management.ipynb)

## Technical Skills Demonstrated

### Programming & Tools
- Python (3.8+)
- Jupyter Notebooks/JupyterLab
- Data Manipulation: Pandas, Polars
- Visualization: Matplotlib, Seaborn, Plotly
- Data Processing: NumPy, SciPy
- Machine Learning: Scikit-learn, XGBoost, LightGBM
- Natural Language Processing: NLTK, Spacy, Transformers
- Deep Learning: PyTorch, TensorFlow
- Version Control: Git
- Development Environment: VSCode with Python extensions
- Package Management: pip, conda
- Custom formatting and styling libraries: nbformat, ipywidgets

### Data Science Techniques
- **Exploratory Data Analysis (EDA)**
- **Data Cleaning & Preprocessing**
  - Missing value handling
  - Duplicate removal
  - Data type conversions
- **Time Series Analysis**:
  - Trend analysis
  - Monthly/Yearly aggregations
  - Rolling averages
- **Statistical Analysis**:
  - Distribution analysis
  - Rate calculations
  - Demographic analysis
  - Survival rate analysis
- **Interactive Analysis**:
  - User-input based visualizations
  - Dynamic metric selection
  - Filtered data exploration
- **Machine Learning Techniques**:
  - Implementation of classification algorithms such as Logistic Regression, Naive Bayes, Random Forest, and Gradient Boosting.
  - Use of a Stacking Classifier to improve model performance by combining multiple models.
- **Model Evaluation**:
  - Evaluation of models using metrics like Accuracy, Precision, Recall, and ROC_AUC.
  - Visualization of model performance through confusion matrices and distribution plots.
- **Data Handling**:
  - Handling of imbalanced datasets by reclassifying labels into binary categories.
  - Use of text vectorization techniques such as CountVectorizer and TfidfVectorizer for feature extraction.
- **Natural Language Processing (NLP)**:
  - Text summarization
  - Tokenization and text cleaning
  - Text preprocessing including handling missing values and reclassification of text labels.
  - Application of NLP techniques to detect fake news content.

## Repository Structure

The repository is organized into self-contained project directories, each with the following standard structure:

```text
Project_Folder/
├── notebooks/      # Jupyter Notebooks containing analysis and modeling
├── data/           # Datasets used in the project
├── src/            # Python source code and utility scripts
└── results/        # Generated plots, models, and reports
```

### Projects
├── 01_covid19_analysis/
├── 02_titanic_analysis/
├── 03_text_summarization/
├── 04_sentiment_analysis/
├── 05_customer_segmentation/
├── 06_fake_news_detection/
├── 07_augmented_project_management/
├── LICENSE
├── README.md
└── requirements.txt


## Dependencies
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter
- Scikit-learn
- NLTK
- TensorFlow
- Keras
- Transformers
- Plotly
- Wordcloud
- Spacy

## Contact & Connect
Feel free to reach out if you have any questions about my projects or would like to collaborate:
- LinkedIn: https://www.linkedin.com/in/lawrancekoh/
- Email: lawrancekoh@outlook.com

## License
This project is licensed under the MIT License - see the LICENSE file for details.
