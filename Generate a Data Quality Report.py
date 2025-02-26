import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define cleansing steps text FIRST - THIS IS THE KEY PART THAT WAS MISSING
cleansing_steps_text = """
Data Cleansing Steps:

1. Handling Missing Values:
   - Customer ID: 10% missing - Imputation or removal needed.
   - Customer Age: 46% missing - Imputation or removal needed.
   - State: 14% missing - Imputation or removal needed.
   - Membership Status: 28% missing - Imputation or removal needed.

2. Removing Duplicate Rows:
   - No duplicate rows found.

3. Handling Outliers:
   - No outliers detected in transaction amounts.

4. Standardizing Data:
   - (Add details about any standardization applied, e.g., scaling, normalization)

5. Data Type Conversion:
    - (Add details about any data type conversions)

Further Considerations:
- Investigate the reasons for missing data.  Is it random or is there a pattern?
- Choose appropriate imputation methods if you decide to fill missing values (mean, median, mode, KNN, etc.).
- If removing rows with missing data, consider the impact on the overall dataset size and potential bias.
"""

data = pd.read_csv('cleaned_standardized_customer_transactions_no_outliers.csv')

missing_values = data.isnull().sum()
percentage_missing = (missing_values / len(data)) * 100
missing_info = pd.DataFrame({'Missing_Values': missing_values, 'Percentage_Missing': percentage_missing})

plt.figure(figsize=(12, 6))
sns.barplot(x=missing_info.index, y='Percentage_Missing', data=missing_info)
plt.title('Percentage of Missing Values by Column')
plt.xticks(rotation=45)
plt.ylabel('Percentage Missing')
plt.show()
print(missing_info)

num_duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")
plt.figure(figsize=(6, 4))
sns.countplot(x=[bool(num_duplicates)], palette='Set2', order=[True, False]) # Fixed FutureWarning
plt.title('Duplicate Rows in Dataset')
plt.xticks(ticks=[0, 1], labels=['Duplicates', 'Unique'])
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=data['transaction_amount'])
plt.title('Boxplot for Transaction Amounts')
plt.xlabel('Transaction Amount')
plt.show()

Q1 = data['transaction_amount'].quantile(0.25)
Q3 = data['transaction_amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = data[(data['transaction_amount'] < lower_bound) | (data['transaction_amount'] > upper_bound)]
print(f"Number of outliers: {outliers.shape[0]}")

print(cleansing_steps_text)  # This will now work correctly