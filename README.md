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

### Day 8: Data Cleaning — Laptop Price Dataset

### Project Overview
Cleaned a raw, uncleaned Laptop Price dataset using Python to find and fix missing values, duplicate records, inconsistent column names, wrong data types and impossible values, and saved a clean version ready for analysis.

### Tools Used

Python
Pandas and NumPy
Jupyter Notebook
Git and GitHub

### Dataset
Laptop Price dataset (uncleaned version) from Kaggle.
Source: (add Kaggle link)
The raw data has 1,273 laptops and 12 columns: company, type, screen size, screen resolution, CPU, RAM, storage, GPU, operating system, weight and price (INR).

### Data Cleaning

Dropped the unnamed row-number column 0.
Identified missing values: isnull() showed none, but missing values were stored as ? (in Inches, Memory and Weight). Replaced ? with NaN.
Found and removed 29 duplicate rows.
Renamed columns to lowercase snake_case with units in the name (e.g. Ram → ram_gb, Weight → weight_kg, OpSys → os).
Converted data types: removed “GB”/”kg” units and converted RAM to integer and weight to float; converted screen size to float; rounded price to whole rupees; converted brand, type and os to category.
Merged inconsistent labels: Mac OS X and macOS → macOS.
Found impossible values (a weight of 0.0002 kg, notebooks weighing up to 11.1 kg, screen sizes of 24–35.6 inches) and treated them as missing.
Handled missing values: screen size and weight were filled with the median of the same laptop type; the 1 row with missing storage was dropped.
Saved the cleaned dataset.

### Results

	Before	After
Rows	1,273	1,243
Columns	12	11
Missing values	3 (hidden as ?)	0
Duplicate rows	29	0
Numeric columns stored as text	3	0

### Key Findings
Missing values aren’t always blank. In this dataset they were written as ?, so isnull() missed them and they only showed up when converting columns to numbers. The duplicates only appeared after the row-number column was dropped. Checking describe() after the type conversion revealed data-entry errors in weight and screen size that would have distorted any analysis.

### Project Files

data_cleaning.ipynb: step-by-step cleaning with outputs and notes.
data/laptop_data_raw.csv: original uncleaned dataset.
data/laptop_data_cleaned.csv: cleaned dataset.

### Conclusion
This project applied a full data cleaning workflow to a real-world dataset: loading, identifying missing and hidden values, removing duplicates, renaming columns, fixing data types, handling outliers and missing values, and saving the result. The cleaned dataset is ready for analysis and visualization.

