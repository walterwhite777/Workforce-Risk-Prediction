# Insights and Recommendations

## Key Insights

Based on the analysis of 15,004 employee records with a 23.83% overall churn rate (3,576 churned employees), the following insights highlight the primary drivers of employee churn:

- **Satisfaction Level**:

  - Employees with “Very Low” satisfaction (≤0.2) have the highest churn rate (62.54%), followed by “Low” satisfaction (49.39%).
  - High and Very High satisfaction groups have significantly lower churn rates (9.89% and 13.72%, respectively).
  - Low satisfaction is a critical driver of churn, with a clear correlation between dissatisfaction and leaving.

- **Department**:

  - The HR department has the highest churn rate (29.09%), followed by Accounting (26.60%) and Technical (25.62%).
  - Management and R&D departments have the lowest churn rates (14.44% and 15.37%).
  - Certain departments, particularly HR and Accounting, face higher attrition, possibly due to role-specific stressors.

- **Salary**:

  - Employees with low salaries have a churn rate of 29.74%, compared to 20.43% for medium and 6.63% for high salaries.
  - Low compensation significantly increases churn risk, while higher salaries correlate with retention.

- **Number of Projects**:

  - Employees with 2 projects (65.62%) or 7 projects (100%) have extremely high churn rates, suggesting under- or overwork.
  - Employees with 3–5 projects have lower churn rates (1.78%–22.17%).
  - Both insufficient and excessive workloads drive churn.

- **Tenure**:

  - Churn peaks at 5 years (56.55%) and 4 years (34.81%), indicating a critical period after 3–5 years of employment.
  - Employees with 7+ years have negligible churn rates (0%).
  - Mid-tenure employees are at higher risk, possibly due to career stagnation.

- **Promotions**:

  - Employees without promotions in the last 5 years have a 24.22% churn rate, compared to 5.96% for promoted employees.
  - Lack of career advancement increases churn likelihood.

- **Feature Importance**:

  - The Random Forest model identified satisfaction level, time spent at the company, number of projects, and average monthly hours as top predictors of churn.
  - Employee engagement and workload are critical factors in retention.

## Recommendations

To reduce churn, particularly for the pilot program’s new employees, the following actions are recommended:

1. **Enhance Employee Satisfaction**:

   - Implement an **employee recognition program** to boost morale and engagement, addressing the high churn among low-satisfaction employees.
   - Conduct regular satisfaction surveys to identify and address pain points early.

2. **Target High-Risk Departments**:

   - Focus retention efforts on HR, Accounting, and Technical departments.
   - Introduce **department-specific initiatives**, such as stress management workshops or team-building activities, to improve workplace culture.

3. **Improve Compensation**:

   - Review and adjust salaries for low- and medium-paid employees to align with market standards, reducing the 29.74% churn rate among low-salary employees.
   - Offer performance-based bonuses to incentivize retention.

4. **Optimize Workload**:

   - Ensure employees are assigned 3–5 projects to avoid under- or overwork, as extreme project loads (2 or 7 projects) lead to high churn.
   - Monitor average monthly hours to prevent burnout from excessive workloads.

5. **Support Mid-Tenure Employees**:

   - Develop **career development programs** for employees with 3–5 years of tenure, offering training, mentorship, or role transitions to prevent stagnation.
   - Create clear career paths to retain talent during this high-risk period.

6. **Promote Career Advancement**:

   - Increase opportunities for promotions, especially for employees without recent advancements, to reduce the 24.22% churn rate.
   - Implement a transparent promotion process to motivate employees.

7. **Leverage Predictive Model**:

   - Use the Random Forest model’s predictions to proactively identify at-risk employees in the pilot program.
   - Share the Looker Studio dashboard with HR to prioritize interventions for employees with high churn probabilities.

## Conclusion

By addressing low satisfaction, low salaries, excessive workloads, and lack of promotions, the organization can significantly reduce churn. The predictive model and dashboard provide a proactive tool to identify at-risk employees, enabling targeted retention strategies. Implementing these recommendations will enhance employee engagement and retention, supporting the success of the pilot program.