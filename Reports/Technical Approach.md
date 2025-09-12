# Technical Approach: Employee Churn Prediction Project

## Overview

This project develops a machine learning model to predict employee churn and delivers a dashboard to visualize predictions and insights. this project leverages a PostgreSQL database for data storage, two Python notebooks for analysis and modeling, and Google Looker Studio for visualization. The workflow includes data ingestion, exploratory data analysis (EDA), model building, prediction on new employee data, and dashboard creation.

## Tools and Technologies

- **Database**: PostgreSQL for storing and querying employee data.
- **Programming**: Python with libraries (Pandas, PyCaret, Matplotlib, Seaborn) for analysis and modeling.
- **Machine Learning**: PyCaret for automated model training and evaluation.
- **Visualization**: Google Looker Studio for creating an interactive dashboard.
- **Environment**: Jupyter Notebooks (two separate notebooks for analysis and modeling).

## Methodology

The project follows a structured data science workflow:

### 1. Data Ingestion and Database Setup

- **Data Source**: Two datasets were used:
  - Historical employee data (15,004 records) with features like `employee_id`, `satisfaction_level`, `last_evaluation`, `number_project`, `average_montly_hours`, `time_spend_company`, `Work_accident`, `Quit_the_Company`, `promotion_last_5years`, `Departments`, and `salary`.
  - New employee data (100 records) for predictions, excluding the `Quit_the_Company` label.
- **PostgreSQL Setup**:
  - Created a PostgreSQL database and two tables: `tbl_hr_data` for historical data and `tbl_new_employees` for new employee data.
  - Uploaded CSV files to PostgreSQL using Python’s `psycopg2` library.
  - Created a view (`tbl_full_data`) combining both datasets with a `type` column (`original` for historical, `pilot` for new employees) using a `UNION ALL` query.

### 2. Exploratory Data Analysis (EDA)

- **Notebook**: A dedicated Jupyter Notebook (HR Analyzer.ipynb) was used for EDA.
- **Process**:
  - Connected to the PostgreSQL database using `psycopg2` to query `tbl_full_data`.
  - Performed univariate analysis on numerical features (`satisfaction_level`, `last_evaluation`, `average_montly_hours`) and categorical features (`Departments`, `salary`, etc.), generating summary statistics and distributions.
  - Conducted bivariate analysis to explore churn rates (`Quit_the_Company`) across features like satisfaction level, department, salary, and tenure.
  - Visualized distributions and churn rates using Matplotlib and Seaborn (e.g., bar charts for `salary` and `Departments`, histograms for numerical features).
- **Output**: A comprehensive report with tables and visualizations, as shown in the provided analysis summary (e.g., churn rate by department, salary, and satisfaction level).

### 3. Model Development

- **Notebook**: A separate Jupyter Notebook (`modeling.ipynb`) for machine learning.
- **Preprocessing**:
  - Used PyCaret’s `setup` function with the historical dataset (`tbl_hr_data`).
  - Ignored `employee_id` as it’s not predictive.
- **Model Training**:
  - Trained multiple classification models using PyCaret’s `compare_models` to identify the best performer.
  - Selected the Random Forest model due to its high accuracy (\~93%).
  - Tuned the model using `tune_model` to optimize hyperparameters.
- **Prediction**:
  - Applied the trained model to the new employee dataset (`tbl_new_employees`) to predict churn probabilities and labels.
  - Generated a DataFrame (`pilot_predictions`) with predictions and probabilities.
- **Feature Importance**:
  - Extracted feature importances from the Random Forest model using `plot_model('feature')`.
  - Created a feature importance table with columns `feature` and `importance`.

### 4. Data Export to PostgreSQL

- Exported the prediction results (`pilot_predictions`) and feature importance table (`feature_table`) to PostgreSQL using `pandas.to_sql`.
- Created tables `tbl_pilot_predictions` and `tbl_feature_table` in the PostgreSQL database.

### 5. Dashboard Creation

- **Tool**: Google Looker Studio.
- **Data Sources**: Connected to PostgreSQL tables `tbl_pilot_predictions` and `tbl_feature_table`.
- **Design**:
  - Followed a wireframe similar to the reference dashboard:
    - **Main KPI**: Churn rate percentage for the pilot program (\~7%).
    - **Supporting KPIs**: Average satisfaction level, average tenure, average last evaluation, and department count.
    - **Feature Importance**: Bar chart showing key churn drivers (e.g., satisfaction level, tenure).
    - **Churn by Department**: Stacked bar chart showing predicted churn by department.
    - **Employee Sentiment**: Calculated field to categorize satisfaction level (&gt;0.5 as “Satisfied”, ≤0.5 as “Unsatisfied”).
  - Added a department filter for interactivity.
  - Styled with a blue gradient background, white text, and consistent fonts (e.g., Impact for titles).

## Workflow Summary

1. Loaded and stored data in PostgreSQL.
2. Conducted EDA in a dedicated notebook, producing a detailed report.
3. Built and trained a Random Forest model in a separate notebook using PyCaret.
4. Predicted churn for new employees and exported results to PostgreSQL.
5. Created an interactive Looker Studio dashboard to visualize predictions and insights.

This approach ensures a robust, reproducible, and stakeholder-friendly solution, showcasing proficiency in database management, data analysis, machine learning, and visualization.