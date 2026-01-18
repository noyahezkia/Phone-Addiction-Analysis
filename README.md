# Teen Phone Addiction Analysis Project

## Project Documentation

### Project Description
This project investigates the relationship between smartphone usage patterns and addiction levels among teenagers, focusing on the distinction between "productive" and "distractive" usage.

**Main Objectives:**
* To determine whether time dedicated to educational purposes on a phone acts as a "protective factor" that reduces addiction levels, or if any increased usage leads to higher addiction regardless of content.
* To compare addiction levels across different primary usage purposes (Gaming, Social Media, Education).

**Assumptions & Hypotheses:**
* **Primary Hypothesis:** Educational usage is a "protective factor". Users with high educational usage will exhibit lower addiction levels compared to those with high general usage.
* **Assumption:** The dataset is rich and clean of missing values, but contains outliers that must be filtered to ensure statistical validity.
* **Assumption:** Content type is a more significant predictor of addiction than total duration of use alone.

### Folder/Module Structure
The project is built with a modular architecture to ensure readability and maintainability:

* `data/`: Contains the raw dataset (`teen_phone_addiction_dataset.csv`).
* `src/`: Source code modules:
    * `data_handler.py`: Handles data ingestion, basic cleaning (duplicates/NaNs), and outlier removal using the IQR method.
    * `correlations.py`: Logic for calculating Pearson correlations and linear regression.
    * `group_comparisons.py`: Implementation of independent t-tests for group analysis and one way ANOVA. 
    * `logger_config.py`: Centralized logging configuration (INFO level).
    * `visualizations.py`: Utility functions for Bar, Box, and Scatter plots.
* `main.py`: The entry point script that orchestrates the analysis pipeline.
* `tests/`: Directory for unit tests covering major project stages.
    * `tests_conf.py`: Configuring sample data for testing.
* `requirements.txt`: List of dependencies (pandas, scipy, statsmodels, etc.).

### Key Stages
The analysis follows a structured pipeline:
1. **Data Ingestion & Preprocessing:** Loading the CSV, cleaning missing values, and removing outliers using IQR to prevent skewed results.
2. **Correlation Analysis:** Computing the relationship (Pearson r) between addiction and specific usage types (Education, Social Media, Gaming).
3. **Hypothesis Testing (t-test):** Comparing addiction levels of users in the upper median of educational usage against users in the upper median of general usage.
4. **Predictive Modeling (Regression):** Running an OLS model to determine the contribution of demographic, psychological, and behavioral factors to addiction levels.
5. **Group Variance Analysis (ANOVA):** Testing if addiction levels vary significantly based on the participant's primary phone usage purpose.
6. **Visualization:** Generating graphs to summarize findings, including addiction distribution by category and correlation trends

---

## Data Description
* **Dataset Name:** teen_phone_addiction_dataset.
* **Specifications:** 3,000 rows and 25 columns.
* **Data Types:** Includes demographic, behavioral (usage hours), and psychological metrics.
* **Link to Dataset:** [Kaggle - Teen Phone Addiction Dataset](https://www.kaggle.com/datasets/sumedh1507/teen-phone-addiction/data).

---

## Instructions for Running the Project

### 1. Installation
Ensure Python 3.x is installed. [cite_start]Install the necessary libraries using the requirements file[cite: 49]:
```bash
pip install -r requirements.txt
```

### 2. Execution
```bash
python main.py
```

* The results of the statistical tests (t-test, ANOVA, Regression) will be logged in logs/analysis.log.
* Visualization windows will open sequentially for Bar charts, Box plots, and Scatter plots.

### 3. Testing
```bash
pytest tests/
```