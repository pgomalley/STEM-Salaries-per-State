# STEM-Salaries-per-State
# Problem Description:
As a junior majoring in Business Analytics and Information Systems and minoring in computer science, I will be entering the workforce next year. Given the current instability in the tech industry, I aim to understand the relationship between various factors such as demographic, background, company, and how they correlate to the salary an employee receives. I hypothesize that there is large correlations between certain aspects about an employee and the income one earns in the tech/STEM field.

# Dataset Description:
Our dataset consists of nearly 60,000 rows of data on salaries in tech/STEM careers. The data includes the following columns:

timestamp
Company
level
title
totalyearlycompensation
location
yearsofexperience
yearsatcompany
basesalary
stockgrantvalue
bonus
gender
cityid
dmaid
rowNumber
Masters_Degree
Bachelors_Degree
Doctorate_Degree
Highschool
Some_College
Race_Asian
Race_White
Race_Two_Or_More
Race_Black
Race_Hispanic
Race
Education
# Functions
I have created several functions to analyze the data:

SalaryStatistics()
This function provides basic statistics (mean, median, standard deviation, variance, percentiles) on salary data.

CompanyLocation()
This function presents salary statistics based on company location. It outputs two pie charts showing the top and bottom five states based on the count in the state column. The function also displays the corresponding values for these states.

SalaryBarCharts()
This function outputs two bar charts, demonstrating average salaries based on years at a company and years of experience.

RaceSalaryBarChart()
This function has two goals. First, to display the distribution of races within the tech industry, it uses the race columns to count this value and generates a pie chart. Secondly, it displays the average salary based on race, outputting a table with the relevant information.

# Getting Started
Clone the repository.
Install necessary packages.
Download the data file and change the file directory.
Run the main.py file to run the Utilities.py file.
Interpret the results and modify the scripts for your analysis if needed.
