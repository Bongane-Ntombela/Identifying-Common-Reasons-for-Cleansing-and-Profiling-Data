import pandas as pd
data = pd.read_csv('cleaned_standardized_customer_transactions_no_outliers.csv')
print(data.info())
constant_columns = [col for col in data.columns if data[col].nunique() == 1]
print(f'Constant Columns: {constant_columns}')
low_variability_columns = [col for col in data.columns if data[col].nunique() < 3 and col not in 
constant_columns]
print(f'Low Variability Columns: {low_variability_columns}')
irrelevant_columns = constant_columns + low_variability_columns
cleaned_data = data.drop(columns=irrelevant_columns)
print(cleaned_data.info())
cleaned_data.to_csv('cleaned_data_without_irrelevant_features.csv', index=False)