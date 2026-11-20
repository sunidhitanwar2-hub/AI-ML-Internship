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

### Day 9: Exploratory Data Analysis — Laptop Price Dataset

### Project Overview
Performed exploratory data analysis on the cleaned Laptop Price dataset from Day 8 to understand what drives laptop prices, how the market is segmented, and how brands are positioned, and wrote 5 business insights from the results.

### Tools Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- Git and GitHub

### Dataset
Cleaned Laptop Price dataset from Day 8 (`data/laptop_data_cleaned.csv`): 1,243 laptops, 11 columns, no missing values.
Original source: Laptop Price dataset (uncleaned version), Kaggle. <!-- add the Kaggle dataset link here -->

### Analysis
- **Descriptive statistics:** mean, median, mode, standard deviation, range and skewness of price; summary of all numeric and categorical columns; counts by brand, type, OS and RAM.
- **Feature extraction:** pulled CPU series, GPU brand, SSD, touchscreen, IPS panel and resolution width out of long text columns.
- **Trends and patterns:** correlation with price; median price by type, RAM, SSD, CPU series, GPU brand, touchscreen and brand.

### Key Statistics
| Metric | Value |
|---|---|
| Mean price | ₹60,604 |
| Median price | ₹52,694 |
| Price range | ₹9,271 – ₹3,24,955 |
| Skewness | 1.52 (right skewed) |
| Most common RAM | 8 GB (48%) |
| Laptops with SSD | 66% |
| Most common OS | Windows 10 (82%) |

### Visualizations
1. Distribution of laptop prices
   ![Price distribution](charts/1_price_distribution.png)
2. Median price by laptop type
   ![Price by type](charts/2_price_by_type.png)
3. Laptop price by RAM size
   ![Price by RAM](charts/3_price_by_ram.png)
4. SSD vs no SSD, and price by CPU series
   ![SSD and CPU](charts/4_ssd_and_cpu.png)
5. Brands: number of laptops vs median price
   ![Brands](charts/5_brands.png)

### Business Insights
1. **RAM is the biggest driver of price.** It has the highest correlation with price (0.68). Median price rises from ₹26.6k (4 GB) to ₹59.5k (8 GB) to ~₹1 lakh (16 GB). 8 GB is the most common configuration and the mid-range sweet spot, so RAM upgrades are an easy way to upsell.
2. **SSD is expected above the budget segment.** 66% of laptops have an SSD, and their median price (₹67.5k) is more than double that of laptops without one (₹30k).
3. **The market has a large budget segment and a premium segment.** Notebooks are 55% of laptops with a ~₹37k median, while Gaming, Ultrabook and Workstation laptops have medians of ₹79k–₹1.1 lakh. Notebooks drive volume; premium types drive revenue per sale.
4. **Brands are positioned at clear price levels.** Lenovo, Dell and HP hold ~66% of laptops in the mid range (₹48k–₹53k). Acer is the budget brand (₹30k), while MSI (₹85k) and Apple (₹71k) are premium.
5. **Processor tier sets the price band.** Core i3 ≈ ₹26.6k, Core i5 ≈ ₹51k, Core i7 ≈ ₹79k. Core i5 and i7 make up ~73% of laptops, so most of the market is mid to high performance.

### Project Files
- `eda_laptop_prices.ipynb`: statistics, analysis, charts and insights.
- `charts/`: the 5 visualizations as PNG images.
- `data/laptop_data_cleaned.csv`: cleaned dataset from Day 8.

### Conclusion
Laptop prices in this dataset are driven mainly by specs (RAM, SSD, CPU tier and laptop type), while screen size and weight have very little effect. Brands target different price segments. Findings describe this dataset snapshot, not the full market.

## Day 10: Laptop Price Prediction using Machine Learning

### Objective
Build a Linear Regression model to predict laptop prices in Indian Rupees using laptop specifications.

### Dataset
- File: `Day 9/laptop_data_cleaned.csv`
- Records: 1,243 laptops
- Input features: 10
- Target variable: `price_inr`

### Workflow
1. Loaded and inspected the cleaned dataset.
2. Separated features and target prices.
3. Split the dataset into 80% training and 20% testing sets.
4. Preprocessed numeric and categorical features using a Scikit-learn pipeline.
5. Trained a Linear Regression model.
6. Generated predictions and evaluated performance.
7. Visualized actual versus predicted prices and prediction errors.
8. Saved the trained pipeline using Joblib.

### Model Evaluation

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | ₹13,389.00 |
| Root Mean Squared Error (RMSE) | ₹22,628.06 |
| R² Score | 0.5905 |

### Example Prediction
The model predicted approximately ₹74,971.77 for one sample laptop configuration. This is a model estimate, not a verified market price.

### Project Files
- `Day_10/laptop_price_prediction.ipynb` — machine learning notebook
- `Day_10/laptop_price_model.pkl` — saved preprocessing and prediction pipeline

### Conclusion
The Linear Regression model provides a baseline for laptop price prediction. Its results indicate that predictive performance could be improved, particularly for some higher-priced laptops.

### Tools Used
Python, Pandas, NumPy, Matplotlib, Scikit-learn, Joblib, Jupyter Notebook.


## Day 11: Classification Models

### Objective
Learn the basics of classification and train two machine learning classification models.

### Dataset
- Iris Flower Dataset
- Source: Scikit-learn built-in dataset
- Total samples: 150
- Features: 4
- Classes: Setosa, Versicolor, Virginica

### Models Implemented
1. Logistic Regression
2. Decision Tree Classifier

### Tasks Completed
- Loaded and explored the Iris dataset.
- Separated input features and target labels.
- Split the dataset into training and testing sets (80:20).
- Trained a Logistic Regression model.
- Trained a Decision Tree model.
- Evaluated both models using accuracy.
- Compared model performance using a table and bar chart.
- Generated classification reports and confusion matrices.

### Key Learnings
- Understanding classification problems.
- Training and testing classification models.
- Making predictions on unseen data.
- Evaluating model performance using accuracy, precision, recall, and F1-score.

### Conclusion
Successfully implemented and compared Logistic Regression and Decision Tree classification models using the Iris dataset.


## Day 12 - Model Evaluation

### Objective
Evaluate machine learning classification models using different performance metrics.

### Dataset
Iris Flower Dataset from Scikit-learn.

### Models Evaluated
1. Logistic Regression
2. Decision Tree Classifier

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Work Completed
- Loaded and prepared the Iris dataset.
- Split the dataset into training and testing sets.
- Trained Logistic Regression and Decision Tree models.
- Generated predictions using both models.
- Calculated Accuracy, Precision, Recall, and F1 Score.
- Generated Confusion Matrices.
- Created Classification Reports.
- Compared model performance.

### Key Learning
Learned how to evaluate classification models using different metrics and interpret their performance.

## Day 13 - Natural Language Processing (NLP)

### Objective
Learn basic NLP concepts and perform text preprocessing.

### Dataset
A small sample dataset containing five text sentences.

### Tasks Completed
- Lowercasing
- Tokenization
- Stopword Removal
- TF-IDF Vectorization

### Results
- Processed 5 text sentences.
- Identified 18 unique words.
- Generated a TF-IDF matrix of shape (5, 18).
- Converted text data into numerical features.

### Key Learning
Learned how to clean text data and convert human language into numerical representations using TF-IDF.

## Day 14 – Sentiment Analysis Using Machine Learning

### Objective
Build a machine learning model that classifies text reviews as Positive or Negative.

### Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- NLP and TF-IDF
- Logistic Regression

### Tasks Completed
1. Created a sample sentiment dataset.
2. Cleaned and preprocessed text.
3. Converted text into numerical features using TF-IDF.
4. Split the dataset into training and testing sets.
5. Trained a Logistic Regression model.
6. Evaluated the model using Accuracy, Precision, Recall, F1 Score, and a Confusion Matrix.
7. Tested predictions on new reviews.
8. Saved the trained model and TF-IDF vectorizer.

### Files Generated
- `sentiment_model.pkl`
- `tfidf_vectorizer.pkl`
- `sentiment_dataset.csv`
- `sentiment_analysis.ipynb`

### Conclusion
Successfully completed a beginner-level sentiment analysis project using NLP and Machine Learning. The model classifies reviews as Positive or Negative.

**Note:** This project uses only 20 sample reviews for practice. A larger, more diverse dataset is needed for reliable real-world predictions.

# Day 15 – LLM and Hugging Face Model Comparison

## Objective
- Understand the evolution of AI from Machine Learning to Generative AI.
- Create a Hugging Face account.
- Explore the Hugging Face Model Hub.
- Test different pre-trained AI models.
- Compare model outputs and document observations.

## Tools and Technologies
- Python
- Jupyter Notebook
- Hugging Face Model Hub
- Transformers
- PyTorch
- VS Code

## Models Tested

### 1. Qwen2.5-0.5B-Instruct
- **Task:** Text Generation
- Generated a simple explanation of Artificial Intelligence.
- Demonstrated how an LLM can generate human-readable text.

### 2. DistilBERT SST-2
- **Task:** Sentiment Analysis
- Analyzed a sample product review.
- **Result:** POSITIVE
- **Confidence:** 0.9999

### 3. DistilBART CNN
- **Model:** `sshleifer/distilbart-cnn-6-6`
- **Task:** Text Summarization
- Generated a shorter summary of an article about Artificial Intelligence.
- Demonstrated automatic text summarization.

## Model Comparison

| Model | Task | Observation |
|---|---|---|
| Qwen2.5-0.5B-Instruct | Text Generation | Generated an explanation of AI |
| DistilBERT SST-2 | Sentiment Analysis | Predicted positive sentiment |
| DistilBART CNN | Summarization | Generated a concise summary |

## Learning Outcomes
- Learned about Hugging Face and its Model Hub.
- Learned how to load pre-trained models using the Transformers library.
- Explored text generation, sentiment analysis, and summarization.
- Understood how different transformer models perform different NLP tasks.
- Learned to compare model outputs.

## Conclusion
Successfully explored Hugging Face and tested three different pre-trained AI models for text generation, sentiment analysis, and text summarization. This task provided practical experience with Large Language Models and transformer-based NLP applications.

## Project File
- `llm_model_comparison.ipynb` – Notebook containing model loading, testing, outputs, comparison, and conclusion.

# Day 16: Basic RAG on Company Documentation

## Overview
Today, I worked on building a basic **Retrieval-Augmented Generation (RAG)** system using sample company documents.

RAG allows an AI model to answer questions using information retrieved from specific documents instead of relying only on its pre-trained knowledge.

## Objective
- Understand the concept of Retrieval-Augmented Generation.
- Load and process company documentation.
- Split documents into smaller chunks.
- Generate embeddings for the text chunks.
- Retrieve relevant information using vector search.
- Use an LLM to generate answers based on the retrieved content.
- Experiment with different chunk sizes and compare the results.

## Documents Used
I created five sample policy documents for a fictional company called **NovaTech Solutions**:

1. Leave Policy
2. Remote Work Policy
3. IT Security Policy
4. Expense Policy
5. Employee Onboarding Guide

## RAG Workflow

The project follows this pipeline:

`Company Documents → Text Chunking → Embeddings → Vector Search → LLM Answer Generation`

### Main Steps
1. **Document Loading:** Load the sample company documents.
2. **Text Chunking:** Divide documents into smaller sections for easier retrieval.
3. **Embeddings:** Convert text chunks into numerical representations.
4. **Retrieval:** Search for the most relevant chunks based on a user's question.
5. **Answer Generation:** Provide the retrieved context to an LLM to generate an answer.
6. **Evaluation:** Compare the results using different chunk sizes.

## Experiments
I experimented with different chunk sizes to understand how chunking affects document retrieval and answer quality.

The project includes:
- Chunk-size comparison results
- Response evaluation results
- A comparison report
Technologies Used

Python

Jupyter Notebook

NumPy

Pandas

Matplotlib

Seaborn

PyTorch

Transformers

Sentence Transformers

### Key Learnings

Understood the basic concept of RAG.

Learned how document chunking supports information retrieval.

Understood how embeddings represent text numerically.

Explored how vector search retrieves relevant document sections.

Learned how an LLM can use retrieved context to answer questions.

Compared retrieval and response results using different chunk sizes.

### Conclusion

This project helped me understand how Retrieval-Augmented Generation connects document retrieval with language models. It demonstrated how an AI system can use custom company documents to provide context-based answers.

# Day 17 – Complete RAG API using FastAPI

## Objective
To build an end-to-end Retrieval-Augmented Generation (RAG) API that allows users to upload PDF or TXT documents and ask questions based on their content.

## Technologies Used
- Python 3.11
- FastAPI
- Uvicorn
- Sentence Transformers
- Hugging Face Transformers
- Qwen 2.5 0.5B Instruct
- PyPDF
- NumPy
- Swagger UI

## Project Structure
```text
Day_17/
├── docs/
├── results/
├── screenshots/
├── uploads/
├── main.py
├── rag_pipeline.py
├── document_processor.py
├── requirements.txt
└── README.md
```

## Implementation

### 1. Document Processing
- Accepted PDF and TXT file uploads.
- Extracted text using PyPDF for PDF files.
- Divided extracted text into smaller overlapping chunks.
- Handled empty files and unsupported formats.

### 2. RAG Pipeline
- Generated text embeddings using `all-MiniLM-L6-v2`.
- Used NumPy cosine similarity through normalized embedding dot products to retrieve relevant chunks.
- Used Qwen 2.5 0.5B Instruct to generate answers from retrieved document content.

### 3. FastAPI Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/upload` | Upload and process documents |
| POST | `/ask` | Ask questions about uploaded documents |

### 4. API Testing
Tested the API using FastAPI Swagger UI at:

`http://127.0.0.1:8000/docs`

- Uploaded a PDF document about DBMS.
- Generated document chunks and embeddings.
- Asked questions about the uploaded document.
- Received AI-generated answers with source text and similarity scores.
- Verified successful API responses.

### 5. Error Handling
- Unsupported file formats return HTTP 400.
- Empty files are rejected.
- Documents without readable text are rejected.
- Asking questions with an unknown document ID returns HTTP 404.

## Key Learnings
- Building REST APIs using FastAPI.
- Handling file uploads with Python.
- Extracting and chunking document text.
- Generating and retrieving embeddings.
- Connecting an LLM with a RAG pipeline.
- Testing API endpoints using Swagger UI.
- Handling invalid inputs and API errors.

## Limitations and Future Improvements
- Add file-size limits for large uploads.
- Add persistent vector storage instead of in-memory storage.
- Improve support for scanned PDFs using OCR.
- Add more document formats.
- Improve

# Day 18 – AI Agent: Company HR Research Agent

## Objective
Built an AI Agent that answers employee questions about company HR policies using tools connected to the Day 17 RAG API.

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Requests
- RAG API

## Project Files
- `main.py` – FastAPI application
- `agent.py` – Agent workflow and decision-making
- `tools.py` – Functions used by the agent
- `hr_policy.txt` – Company HR policy document

## Tools Created
1. Company Document Search
2. Leave Information
3. Working Hours

## Workflow
1. Receive an employee question.
2. Select the appropriate tool.
3. Retrieve information through the RAG API.
4. Generate and return the final answer.

## Testing
Tested the agent using FastAPI Swagger UI at `http://127.0.0.1:8000/docs`.

## Learning Outcomes
- Understood AI Agent workflows.
- Practised planning and tool selection.
- Connected an AI Agent with a RAG API.
- Tested API responses using Swagger UI.

## Conclusion
Successfully built a Company HR Research Agent that selects appropriate tools to answer employee questions using company documents.

# Day 19 – LangGraph Workflows

## Objective
Build an HR assistant using LangGraph with nodes, state, conditional routing, and memory.

## Technologies
- Python
- LangGraph
- FastAPI
- Requests

## Features
- Question validation
- Document retrieval using Day 17 RAG API
- Conditional routing
- Error handling
- Checkpoint memory using MemorySaver

## Workflow
User Question → Validation → Document Retrieval → Answer

Invalid questions or retrieval failures are routed to an error-handling node.

## Learning Outcomes
Learned how to create LangGraph workflows, manage state, implement conditional routing, and use memory.

## Conclusion
Successfully created a basic LangGraph HR assistant integrated with the existing RAG API.
# Day 20 – Tool Creation and Function Calling

## Overview
Built a Company AI Tool Assistant using Python. It selects and executes tools based on user requests.

## Tools Implemented
- Calculator
- Web Search
- Database Query
- File Reader (PDF/TXT)
- Weather
- Email Draft
- Date and Time
- CSV Data Analyzer
- Company Search using Day 17 RAG API

## Key Features
- Keyword-based tool selection
- Parameter extraction
- Tool planning and execution
- Tool chaining (Weather → Email)
- Basic error handling

## Technologies
Python, SQLite, Pandas, FastAPI, Requests, PyPDF

## Project Structure
- `main.py` – Main application
- `tools.py` – Tool functions
- `tool_selector.py` – Tool selection
- `tool_planner.py` – Tool planning
- `tool_executor.py` – Tool execution
- `data/` – Sample CSV data
- `docs/` – Project documentation

## Testing
Successfully tested weather retrieval, email draft creation, calculator, database, CSV analysis, file reading, and company document search.

## Learning Outcome
Learned tool creation, function calling, tool selection, tool chaining, and error handling.

# Day 21 – Async Programming and FastAPI

## Overview
This project demonstrates asynchronous APIs and advanced FastAPI features.

## Features
- Async and Await endpoints
- Background Tasks
- Middleware
- Pydantic Validation
- Dependency Injection
- API Versioning
- Performance Benchmarking

## Performance Results

| API | Execution Time |
|---|---:|
| Synchronous | 5.06 sec |
| Asynchronous | 3.11 sec |

**Observed improvement:** 38.54% reduction in execution time.

## Run the API
```bash
pip install -r requirements.txt
python -m uvicorn async_api:app --reload --port 8002
```

Open Swagger UI: `http://127.0.0.1:8002/docs`

## Technologies
Python, FastAPI, Uvicorn, Asyncio, Pydantic, HTTPX.

# Day 22 – Multi-Agent Research Assistant

## Overview
Built a company research assistant using five specialized agents that work together to answer questions from company documents.

## Agents
- Coordinator Agent – Manages the workflow.
- Research Agent – Retrieves company information using the RAG API.
- Analyzer Agent – Analyzes research findings.
- Critic Agent – Reviews and approves the analysis.
- Writer Agent – Generates the final report.

## Features
- Multi-agent communication
- Shared state management
- Workflow planning
- Critic review and correction loop
- FastAPI integration
- Company document research

## Run the Project
Start the Day 17 RAG API on port 8001, then run:

```bash
python -m uvicorn main:app --reload --port 8003
```

Open Swagger UI: `http://127.0.0.1:8003/docs`

## Technologies
Python, FastAPI, Requests, Pydantic, RAG, Multi-Agent Workflow.

# Day 23 – LangGraph Integration and Multi-Agent Communication

## Overview
Integrated LangGraph with the Multi-Agent Research Assistant to manage agent communication, shared state, and workflow execution.

## Features
- Coordinator, Research, Analyzer, Critic, and Writer Agents.
- LangGraph workflow integration.
- Shared state management.
- Conditional routing and error handling.
- Day 17 RAG API integration.
- FastAPI endpoint for research requests.

## Technologies
Python, LangGraph, FastAPI, LangChain Core, Uvicorn, Requests.

## Run the Project

Start Day 17 API:
```bash
python -m uvicorn main:app --reload --port 8001
```

Start Day 23 API:
```bash
python -m uvicorn main:app --reload --port 8004
```

Swagger UI: http://127.0.0.1:8004/docs

## Deliverables
- Agent Communication Flow
- Sequence Diagram
- System Explanation

## Result
Successfully tested the multi-agent workflow and generated a company research report using HR policy documents.

# Day 23 – Production Readiness and Docker

## Project Overview
A Multi-Agent Research Assistant built using FastAPI and LangGraph. It connects with the Day 17 RAG API to retrieve company information and generate research reports.

## Features
- Multi-agent workflow using LangGraph
- FastAPI endpoints
- Unit and API testing using Pytest
- Application logging
- Environment variable configuration using `.env`
- Docker containerization

## Project Structure
- `agents/` – Research, Analyzer, Critic and Writer agents
- `docs/` – Project documentation and reports
- `diagrams/` – Workflow diagrams
- `logs/` – Application logs
- `tests/` – Unit and API tests
- `main.py` – FastAPI application
- `graph_workflow.py` – LangGraph workflow
- `Dockerfile` – Docker configuration

## Run Locally
```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8004
```

Swagger UI: http://127.0.0.1:8004/docs

## Run Tests
```bash
python -m pytest tests/ -v
```

## Run with Docker
```bash
docker build --load -t day23-research-assistant .
docker run -d --name day23-container -p 8004:8004 --env-file .env day23-research-assistant
```

## Documentation
- Deployment Checklist
- Production Readiness Report
- Agent Communication Flow
- Sequence Diagram

## Technologies
Python, FastAPI, LangGraph, Pytest, Docker and Python Logging.
:::

# Day 25 – AI Industry Research and LLM Provider Comparison

## Project Overview
A research assignment on AI agents in the enterprise, based on Zapier's November 2026 survey article "88% of enterprises now use or test AI agents, but most still need a human in the loop". It also includes a mini practical comparing OpenAI, Claude, Gemini and Groq on cost, speed and accuracy.

## Features
- Summary of a recent AI article (technology, business impact, developer skills)
- Full article reference (title, publisher, date, URL)
- Key learning points
- Comparison table of OpenAI, Claude, Gemini and Groq (cost, speed, accuracy)
- Written takeaway on which provider to use for which task
- Sources cited for every figure, with the date the data was collected (20 Nov 2026)

## Project Structure
- `Day25_AI_Research_Summary.docx` – Research summary, key learning points and provider comparison
- `day25_sheet_row.tsv` – Day 25 tracker row
- `README.md` – Project description

## Research Topics
1. AI agents in the enterprise (main topic)
2. LLM API cost and speed trade-offs
3. Human-in-the-loop AI governance and safety

## Key Findings
- 88% of enterprises use or test AI agents; 71% run them in production (40% in 2025).
- Only 30% say agents handle most tasks without human help.
- Claude Fable 5.2 scored highest on accuracy (Artificial Analysis Intelligence Index 65), ahead of GPT-6.2 Astra (62) and Gemini 4 Neon (61).
- Groq is the fastest and cheapest, but only for open-weight models.
- GPT-6.2 Sol was the fastest of the three large providers.

## Skills for Developers
Agent orchestration, tool integration (APIs and MCP), reliability and logging, security and guardrails, model selection and cost control, clear process specification.

## Open the Report
Open `Day25_AI_Research_Summary.docx` in Microsoft Word.

## Data Notes
- Figures were gathered on 20 Nov 2026 and prices change often; verify before relying on them.
- OpenAI and Groq prices come from secondary sources because their own pricing pages could not be read.
- The source article is a vendor survey from Zapier, so treat it as an industry signal.

## Technologies
Web research, Artificial Analysis benchmarks, provider pricing pages, Markdown and Microsoft Word.
