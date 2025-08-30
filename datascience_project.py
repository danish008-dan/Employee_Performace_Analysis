#10 emp dataset [IIT] project -
from dis import UNKNOWN

# importing libraries -

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from unicodedata import category

# Basic Exploration -

# Q1 loading dataset -
df = pd.read_csv("employee_performance_dataset.csv")
print(df.head(10))  # give starting 10 rows
print(df.tail())  # give last 5 rows

# Q2 and Q3 basic exploration -
print(df.shape)  # gives no. of column and rows
print(df.info()) # Shows a concise summary: column names, data types etc
print(df.describe())  # Provides summary statistics for numeric columns


# DATA CLEANING -
# Q4 checking duplicated records and droping them -
print(df.duplicated().sum()) # there are 5 duplicate records in the dataset

# removing 5 duplicated records -
df_remove = df.drop_duplicates()
print(df_remove)

#checking for duplicat records -
print(df_remove.duplicated().sum())  # no duplicate records


# Q5 identifying columns containing NAN values -
print(df.isna().sum()) # there are 56 null values in the dataset

# filling NAN values with average of there respective columns -
'''df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Performance_Score'].fillna(df['Performance_Score'].mean(), inplace=True)
#df['Work_Location'].fillna(df['Work_Location'].mode()[0], inplace=True)  using zero bcoz it gives first mode value
df['Projects_Handled'].fillna(df['Projects_Handled'].mean(), inplace=True)'''

# Q6 replacing missing work_Location values with "unknown" -
df["Work_Location"] = df["Work_Location"].fillna("Unknown")
print(df)

# Q7 missing Salary should be filled with median bcoz it reduce the effects of outlier on the data -
df['Salary'] = df['Salary'].fillna(df['Salary'].median())


# SORTING & FILTERING -
# Q8 getting top 10 employees with highest salary -
top10_employee = df.nlargest(10, 'Salary')[
    ['Employee_ID', 'Name', 'Salary', 'Work_Location', 'Projects_Handled']
]

print(top10_employee)

# Q9  finding employees who have handled more than 15 projects -
fill1 = df[(df["Projects_Handled"] > 15)]
print(fill1)

# Q10 listing employees with performance score greater than 8 -
fill2 = df[(df["Performance_Score"] > 8)]
print(fill2)

# Q11 finding employees who are eligible for promotion and having performance_score > 7 -
fill3 = df[(df["Promotion_Eligible"] == "Yes") & (df["Performance_Score"] > 7 )]
print(fill3)

# Feature Engineering -
# Q12 creating a new column Experience_Years = 25 - joining year - # matalb ye ki new column ka name hoga experience year = 25 jo ki show krega employee ne 2025 tk kitne saal kaam kiya he


# converting joining_date into joining_time -
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

# Extracting only the year -
df["Joining_Year"] = df["Joining_Date"].dt.year

# calculating Experience_Year -
df["Experience_Year"] = 2025 - df["Joining_Year"]

# showing result -
print(df[["Name","Joining_Year","Experience_Year"]].head())


# Q13 creating a new column Bonus such that - if P_score > 7 (bonus = 15% od salary), else bonus = 10% of salary
df["Bonus"] = np.where(df["Performance_Score"] > 7,
                       0.15 * df["Salary"],
                       0.10 * df["Salary"])

# showing results -
print(df[["Name","Salary","Performance_Score","Bonus"]].head())



# Q14 categorizing employees into three groups based on P-score -
# defining conditions -
conditions = [
    (df["Performance_Score"] >= 8) & (df["Performance_Score"] <= 10),
    (df["Performance_Score"] >= 5) & (df["Performance_Score"] <=  7),
    (df["Performance_Score"] >= 1) & (df["Performance_Score"] <=  4)
]

# defining categories -
categories = ["High Performer", "Average", "Low Performer"]

# Creating New Column -
df["Performance_Category"] = np.select(conditions, categories, default = "Unknown")

# showing results -
print(df[["Name", "Performance_Score", "Performance_Category"]].head())


# Q15 Categorizing employees into workload groups based on projects_handled -
# defining categories -
conditions1 = [
    (df["Projects_Handled"] >= 0) & (df["Projects_Handled"] <=  5),
    (df["Projects_Handled"] >= 6) & (df["Projects_Handled"] <=  12),
    (df["Projects_Handled"] >= 13) & (df["Projects_Handled"] <= 20)

]
# defining categories -
categories1 = ["Low", "Medium", "High"]

# Creating New Column -
df["Workload_Group"] = np.select(conditions1, categories1, default = "Unknown")

# showing results -
print(df[["Name", "Projects_Handled", "Workload_Group"]].head())


# GROUPING AND AGGREGATION -
# Q16 calculating the Average salary department wise -
avg_salary_dept = df.groupby("Department")["Salary"].mean()
print(avg_salary_dept)

# Q17 finding the number of employees in each work location -
location_counts = df["Work_Location"].value_counts()
print(location_counts)

# Q18 finding the maximum performance_score in each department -
max_P_scores = df.groupby("Department")["Performance_Score"].max()
print(max_P_scores)

# Q19 finding which department has the highest average number of projects handles -
avg_Projects_Handled = df.groupby("Department")["Projects_Handled"].mean()
print(avg_Projects_Handled)
max_value = avg_Projects_Handled.max()
print(max_value)


# visualisations -
# Q20  Boxplot of Salary across Departments
df.boxplot(column="Salary", by="Department")
plt.title("Boxplot of Salary across Departments")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

# Q21 Bar chart - number of employees in each Work Location
df["Work_Location"].value_counts().plot(kind="bar")
plt.title("Number of Employees in each Work Location")
plt.xlabel("Work Location")
plt.ylabel("Number of Employees")
plt.show()

# Q22 Scatter plot - Performance Score vs Projects Handled
plt.scatter(df["Performance_Score"], df["Projects_Handled"], alpha=0.6)
plt.title("Scatter Plot: Performance Score vs Projects Handled")
plt.xlabel("Performance Score")
plt.ylabel("Projects Handled")
plt.show()

# Q23 Histogram - Distribution of Salary
plt.hist(df["Salary"], bins=15, edgecolor="black", alpha=0.7)
plt.title("Distribution of Salary")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Advanced Thinking -

# Q24 If the company wants to promote only those employees who : (have P_Score > 7), (have P_Handled > 10), (marked as Promotion_Eligible = Yes)
# finding how many employees qualify -
# Applying the filter conditions to find qualified employees
qualified = df[
    (df["Performance_Score"] > 7) &
    (df["Projects_Handled"] > 10) &
    (df["Promotion_Eligible"] == "Yes")
]

# Counting the number of qualified employees (converted to integer)
qualified_count = int(qualified.shape[0])

# Displaying the count of qualified employees
print("Qualified Employees:", qualified_count)

# Displaying details of the qualified employees
qualified_details = qualified[["Employee_ID", "Name", "Department",
                                "Performance_Score", "Projects_Handled"]].sort_values("Employee_ID")

# Showing the details in a readable format
print(qualified_details.to_string(index=False))



# Q25  which department shows the most consistent (lowest variance) performance -
# Calculating the variance in performance scores for each department
department_variance = df.groupby('Department')['Performance_Score'].var()

# Finding the department with the lowest variance
lowest_variance_department = department_variance.idxmin()
lowest_variance_value = department_variance.min()

# Display the results
print(f"Department with the most consistent performance: {lowest_variance_department}")
print(f"Variance in performance scores: {lowest_variance_value}")

