# Business Case: Employee Churn Prediction Pilot Program

## Problem Statement
The organization is facing challenges with employee retention, leading to increased costs and disruptions. Stakeholders have requested a data-driven pilot program to proactively identify employees at risk of leaving. The goal is to develop a predictive model to forecast churn among new employees and provide actionable insights to improve retention.

## Objectives
- **Primary Objective**: Build a machine learning model to predict which new employees are likely to leave the company based on historical employee data.
- **Secondary Objectives**:
  - Analyze historical employee data to identify key factors driving churn.
  - Deliver a dashboard to visualize churn predictions and contributing factors for stakeholders.
  - Provide recommendations to reduce churn based on data insights.

## Key Questions
### Analysis Questions
- What factors are causing employee churn?
- Which employees are predicted to leave?
- Are employees satisfied, and how does satisfaction impact churn?
- Which departments experience the highest churn rates?

### Project Questions
- **Success Criteria**: Develop a highly accurate prediction model (e.g., >90% accuracy) to identify at-risk employees.
- **Failure Criteria**: An inaccurate model that fails to predict churn reliably.
- **Key Trends**: Identify features (e.g., satisfaction level, salary) driving churn.
- **Actionable Outcomes**: Recommend strategies to address churn based on predictive insights.

## Deliverables
- A machine learning model trained on historical employee data (15,004 records) to predict churn.
- A comprehensive data analysis report highlighting churn drivers.
- A Looker Studio dashboard visualizing predictions for new employees and key insights.
- Actionable recommendations to improve employee retention.

## Scope
- **Data**: Historical employee data (15,004 records) with features like satisfaction level, salary, department, and churn status, plus a new employee dataset for predictions (without churn labels).
- **Target Audience**: HR stakeholders and management.
- **Tools**: PostgreSQL for data storage, Python (PyCaret) for analysis and modeling, Looker Studio for visualization.