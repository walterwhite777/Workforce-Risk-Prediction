# Workforce-Risk-Prediction

## Overview
This repository presents a workforce risk prediction project focused on analyzing employee attrition and offering actionable strategies for HR retention. Using a dataset of 15,004 employee records, the analysis uncovered key churn drivers such as low satisfaction (62.5% attrition) and below-average salaries. The project delivers a detailed analysis, visualizations, and an interactive dashboard to support data-driven HR decisions.

## Project Purpose
	•	Uncover critical factors influencing employee attrition using historical workforce data.
	•	Build predictive models to estimate churn risk for new employees in a pilot program.
	•	Provide HR teams with insights to design targeted retention and engagement strategies.

## Contents 
- `business_case.md`: Outlines the problem statement, objectives, and deliverables.
- `technical_approach.md`: Details the methodology, tools (PostgreSQL, Python), and workflow.
- `insights_recommendations.md`: Summarizes key findings and actionable recommendations.
- `HR Analyzer.ipynb`: Jupyter Notebook for exploratory data analysis (EDA).
- `modeling.ipynb`: Jupyter Notebook for predictive modeling (optional reference).
- [Looker Studio Report Link](https://lookerstudio.google.com/reporting/9f5c4533-f29c-4592-a59f-25a727b963c5): Interactive Report.
![](https://github.com/aliaagamall/Employee-Risk-Analytics-and-Prediction/blob/main/Reports/Employee%20Attrition%20Risk%20Report.png)

## Technologies Used
- **Database**: PostgreSQL
- **Programming**: Python (Pandas, Matplotlib, Seaborn)
- **Visualization**: Google Looker Studio
- **Environment**: Jupyter Notebooks

## How to Use
1. Clone the repository:
   ```
   git clone https://github.com/walterwhite777/Workforce-Risk-Prediction.git
   ```
3. Install dependencies (e.g., `pandas`, `matplotlib`, `seaborn`) via pip:
   ```
   pip install pandas matplotlib seaborn
   ```
4. Explore `HR Analyzer.ipynb` for EDA and `modeling.ipynb` for predictions (requires PostgreSQL setup).
5. View the Looker Studio dashboard (link TBD) for interactive insights.

## Key Insights
	•	Employee satisfaction is a major factor: dissatisfaction correlates with 62.5% churn.
	•	Low salaries contribute to 29.7% attrition.
	•	HR and Accounting departments show the highest attrition rates (29.1% and 26.6%).
	•	Both under-allocated (2 projects) and over-allocated (7 projects) employees face higher churn risk.

## Recommendations
	•	Launch recognition and engagement programs to improve satisfaction.
	•	Review and adjust pay structures for low-paid employees.
	•	Balance workload distribution and invest in career development for mid-tenure employees.


