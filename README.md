# Employee_Performace_Analysis
"Employee performance analysis project involving data cleaning, feature engineering, and visualizations to explore key factors like salary, performance score, and promotion eligibility, using an employee performance dataset."


Project Overview

The dataset includes employee details such as:

Employee ID

Name

Department

Salary

Performance Score

Work Location

Projects Handled

Promotion Eligibility

Joining Date

The main tasks performed in this project include:

Data Cleaning:

Identifying and removing duplicate records.

Handling missing data by filling in missing values (e.g., median for salary, mode for work location).

Feature Engineering:

Creating new columns such as Experience Years and Bonus.

Categorizing employees based on performance scores and workload.

Exploratory Data Analysis (EDA):

Summary statistics and visualizations for insights.

Identifying trends like the relationship between performance scores and projects handled.

Grouping and Aggregation:

Average salary by department, number of employees per work location, etc.

Advanced Analysis:

Identifying employees eligible for promotion based on specific criteria.

Finding the department with the most consistent performance based on variance in performance scores.

Technologies Used

Python

Pandas

Numpy

Matplotlib

Seaborn

Installation

Clone this repository to your local machine:

git clone https://github.com/your-username/employee-performance-analysis.git


Navigate to the project directory:

cd employee-performance-analysis


Install the required libraries:

pip install -r requirements.txt

Usage

The code processes the employee performance dataset to perform various analyses. Simply load the dataset and run the Python script. The dataset is assumed to be in CSV format, with the filename employee_performance_dataset.csv.

After cleaning and analyzing the dataset, here are two potential business insights:

1. High-Performing Employees Are Often Overlooked for Promotions

By filtering employees based on performance scores and promotion eligibility, you may observe a pattern where some high-performing employees are not being considered for promotions. Analyzing the Performance_Score, Promotion_Eligible, and Projects_Handled columns could reveal discrepancies in how promotions are awarded compared to employee performance.

Insight: Employees with high performance scores but low project handling experience could be overlooked for promotions, while those with a greater number of projects but lower performance scores are promoted. This suggests a potential misalignment between promotion criteria and actual performance, which could be addressed by revising promotion policies to better align with employees' contributions.

2. Department-Specific Performance Variability

The variance in performance scores across departments can be a significant insight. If one department has significantly higher variance in performance compared to others, it might indicate that the employees in that department have more uneven workloads, differing skill sets, or lack of training consistency. This would be especially useful for improving department-specific training programs and optimizing resource allocation.

Insight: For example, if the IT department shows the lowest variance, this suggests that performance is relatively consistent, potentially due to standardized processes, training, or workload distribution. On the other hand, departments with high variance might benefit from a closer look into workload balance, skill gaps, and training needs to enhance overall performance consistency.

These insights could lead to strategic improvements in both employee recognition and department-specific management practices
