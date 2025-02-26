# Data Cleansing and Profiling Project

## Project Overview

This project focuses on the critical steps of data cleansing and profiling to ensure data quality and reliability for analysis. We utilized a customer transaction dataset, performing various operations to clean and prepare the data for meaningful insights.

## Project Objectives

1. **Data Import and Exploration:**
   - Load the dataset and explore its structure, including columns, data types, and missing values.

2. **Missing Value Handling:**
   - Identify and handle missing values using appropriate strategies such as imputation or removal.

3. **Duplicate Removal:**
   - Detect and remove duplicate entries to ensure data uniqueness.

4. **Column Standardization:**
   - Standardize column names for consistency and ease of use.

5. **Data Type Correction:**
   - Ensure correct data types for each column to enable accurate analysis.

6. **Outlier Management:**
   - Identify and handle outliers in numerical columns to prevent distortion in analysis.

7. **String Data Validation:**
   - Clean and validate string data for consistency and uniformity.

8. **Irrelevant Feature Removal:**
   - Identify and remove features that do not contribute significantly to the analysis.

9. **Data Quality Reporting:**
   - Generate a comprehensive report summarizing the data quality after cleansing.

10. **Dataset Profiling:**
    - Profile the dataset to understand its statistical properties and distributions.

## Project Deliverables

- **Cleaned Dataset:** `cleaned_data_without_irrelevant_features.csv`
  - The final cleaned dataset, ready for analysis.
- **Data Quality Report:** 
  - A detailed report in the notebook and as a separate document (`Data Bytes (Report).pdf`), summarizing the data quality metrics and cleansing steps.
- **Profiling Report:** 
  - A comprehensive report in the notebook, providing summary statistics and visualizations of the dataset.
- **Visualizations:** 
  - Various plots and charts showcasing data distributions, missing values, and correlations, both in the notebook and the report.

## Project Insights

- **Missing Values:** Identified and handled missing values in key columns such as `customer_id`, `customer_age`, `state`, and `membership_status`.
- **Data Cleaning:** Corrected data types, standardized column names, and cleaned string data for consistency.
- **Outlier Management:** Detected and handled outliers in `transaction_amount` and `customer_age` to ensure data accuracy.
- **Feature Selection:** Removed irrelevant features to streamline the dataset for analysis.

## Conclusion

This project successfully cleaned and profiled the customer transaction dataset, addressing data quality issues and preparing the data for robust analysis. The deliverables provide a clear picture of the data's characteristics and the steps taken to ensure its quality.

Feel free to explore the code, reports, and visualizations in the repository for a deeper understanding of the data cleansing and profiling process.
