# AI-ML-Internship
My AI/ML internship learning journey and daily tasks.
Hello! I am an Information Technology student at Bharati Vidyapeeth University College of Engineering, Pune, graduating in 2028.

I am interested in Artificial Intelligence, Machine Learning, Data Science, and Python programming.

Internship Goals

Understand AI, Machine Learning, Deep Learning, and Generative AI.

Strengthen Python programming fundamentals.

Learn practical AI/ML development workflows.

Build hands-on projects and solve real-world problems.

Learn Git, GitHub, and collaborative software development.

Document my daily learning and internship tasks.

Technologies and Tools

Python

Visual Studio Code

Jupyter Notebook

Git and GitHub

Learning Progress

Understand AI/ML fundamentals

Install and configure the development environment

Create and manage GitHub repositories

Complete internship assignments and projects

Repository Purpose

This repository documents my AI/ML internship learning journey, environment setup, assignments, and practical projects.


## Day 2: Python Fundamentals

### Learning Objectives
- Understand Python syntax and variables.
- Learn Python data types.
- Practice if-else statements and loops.
- Understand and use functions.

### Projects Completed
1. `python_practice.py` - Practice with variables, data types, conditions, loops, and functions.
2. `student_grade_calculator.py` - Calculates total marks, percentage, and grade.
3. `simple_calculator.py` - Performs arithmetic operations using functions.

### Concepts Practiced
- Variables and data types
- Conditional statements
- For and while loops
- Functions and return values
- User input and error handling

## Day 3: Python Data Structures and File Handling

### Learning Objectives
- Learned Lists, Tuples, Dictionaries, and Sets.
- Practiced reading and writing text files.
- Learned how to store and retrieve student records.

### Projects Completed
1. `student_record_management.py` — Adds, displays, and searches student records.
2. `students.txt` — Stores student records for later retrieval.

### Concepts Practiced
- Python data structures
- File handling
- Reading and writing text files
- Functions and menu-driven programs
- Organizing project files

## Day 4: Introduction to NumPy

### Learning Objectives

Learned why NumPy is important for numerical computing and AI/ML.

Created one-dimensional (1D) and two-dimensional (2D) arrays.

Practiced array indexing and slicing.

Performed mathematical operations using NumPy.

Compared Python lists with NumPy arrays.

### Projects Completed

numpy_practice.py - Practiced NumPy arrays, indexing, slicing, and mathematical operations.

numpy_practice.ipynb - Created a Jupyter Notebook with separate code cells for NumPy practice examples.

student_marks_analysis.py - Analyzed student marks using NumPy, calculated subject averages and class average, identified the highest and lowest marks, and found the top-performing student.

### Concepts Practiced

NumPy installation and import

1D and 2D arrays

Array indexing and slicing

Sum, mean, maximum, and minimum

Python lists vs NumPy arrays

Student marks analysis 
## Day 5: Pandas Data Analysis

### Project: Online Shopping Sales Analysis

#### Learning Objectives
- Learned how to load and analyze CSV datasets using Pandas.
- Explored datasets using DataFrames.
- Checked the number of rows and columns.
- Identified missing values in the dataset.
- Filtered data using conditions.
- Calculated summary statistics and analyzed sales revenue.
- Created a bar chart to visualize revenue by product category.

#### Tools and Technologies
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- CSV Dataset

#### Project Files
- `pandas_practice.ipynb` – Jupyter Notebook containing the sales analysis.
- `online_sales.csv` – Dataset containing online shopping product and sales information.

#### Analysis Performed
- Loaded and displayed the online sales dataset.
- Checked dataset dimensions and missing values.
- Filtered products using specific conditions.
- Calculated total and average revenue.
- Identified products with the highest revenue.
- Compared revenue across product categories.
- Visualized category-wise revenue using a bar chart.

#### Key Findings
- Electronics generated the highest total revenue among the categories in the current dataset.
- Stationery generated the lowest total revenue among the categories in the current dataset.
- Product revenue was analyzed to identify the top-performing products.

#### Concepts Practiced
- Pandas DataFrames
- Reading CSV files
- Data filtering and grouping
- Data aggregation using `sum()` and `mean()`
- Missing-value analysis using `isnull()`
- Data visualization using Matplotlib

#### Deliverables
- Completed Pandas practice notebook.
- Online shopping sales dataset.
- Basic sales analysis and visualization.
- Updated GitHub repository.

## Day 6: Data Visualization Using Python

### Project: Online Shopping Sales Visualization

**Objective:** Analyze online shopping sales data and visualize revenue patterns using Python data visualization libraries.

### Tools and Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

### Dataset
- File: `online_sales.csv`
- 25 records and 7 original columns
- Product details, category, price, quantity, payment method, and city

### Tasks Completed
- Loaded and explored the sales dataset using Pandas.
- Calculated order revenue using price and quantity.
- Created a bar chart to compare total revenue by product category.
- Created a line chart to examine revenue variation across orders.
- Created a histogram to understand the distribution of order revenue.
- Created a pie chart to visualize each category's share of total revenue.
- Generated five observations summarizing the sales data.

### Key Learnings
- Understanding the importance of data visualization.
- Creating charts using Matplotlib and Seaborn.
- Grouping and analyzing data with Pandas.
- Identifying revenue patterns and comparing product categories.
- Communicating data insights through visualizations.

### Deliverables
- `data_visualization.ipynb` — Visualization notebook
- `online_sales.csv` — Dataset
- Four visualizations and an observation summary

### Status
Completed — notebook and analysis prepared for GitHub submission.
## Day 7: Week 1 Mini Project — Netflix Data Analysis

### Project Overview
Analyzed a Netflix Movies and TV Shows dataset using Python to explore content types, yearly additions, ratings, genres, and country representation.

### Tools Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- Git and GitHub

### Dataset
Netflix Movies and TV Shows dataset by Shivam Bansal.

Source: https://www.kaggle.com/datasets/shivamb/netflix-shows

### Data Cleaning
- Checked missing values and duplicate rows.
- Removed duplicate rows where present.
- Trimmed extra spaces in text columns.
- Replaced missing director, cast, and country values with `Unknown`.
- Converted `date_added` into a datetime format.

### Visualizations
1. Distribution of Movies and TV Shows.
2. Netflix titles added by year.
3. Top 10 content ratings.
4. Top 10 genres.

### Key Findings
The analysis found that movies outnumber TV shows in this dataset. TV-MA was the most frequent rating, and 2019 had the highest number of recorded additions. See the notebook for the complete genre, release-year, and country results.

### Project Files
- `netflix_analysis.ipynb` — analysis, charts, and insights.
- `netflix_titles.csv` — dataset used in the analysis.

### Conclusion
This project applied data cleaning, exploratory data analysis, visualization, and interpretation to a real-world dataset. Findings depend on the dataset snapshot used.

## Day 10: Laptop Price Prediction using Machine Learning

### Objective
Build a Linear Regression model to predict laptop prices in Indian Rupees using laptop specifications.

### Dataset
- Source file: `Day 9/laptop_data_cleaned.csv`
- Records: 1,243 laptops
- Input features: 10
- Target: `price_inr`

### Workflow
1. Loaded and inspected the cleaned dataset.
2. Separated input features and target prices.
3. Split the data into 80% training and 20% testing sets.
4. Handled missing values, scaled numeric features, and encoded categorical features using a preprocessing pipeline.
5. Trained a Linear Regression model.
6. Generated predictions and evaluated model performance.
7. Visualized actual vs. predicted prices and prediction errors.
8. Saved the trained pipeline as `laptop_price_model.pkl`.

### Model Evaluation

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | ₹13,389.00 |
| Root Mean Squared Error (RMSE) | ₹22,628.06 |
| R² Score | 0.5905 |

### Example Prediction
For one sample laptop configuration, the model predicted a price of approximately ₹74,971.77. This is a model estimate, not a verified market price.

### Files
- `Day_10/laptop_price_prediction.ipynb` — machine learning notebook
- `Day_10/laptop_price_model.pkl` — saved preprocessing and prediction pipeline

### Conclusion
The Linear Regression model provides a baseline for laptop price prediction. The evaluation results show that there is room to improve predictive performance, particularly for some higher-priced laptops.

### Tools
Python, Pandas, NumPy, Matplotlib, Scikit-learn, Joblib, Jupyter Notebook.
