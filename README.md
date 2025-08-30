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
