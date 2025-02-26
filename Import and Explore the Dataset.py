import pandas as pd 
import numpy as np
file_path = 'customer_transactions.csv' # Update this path if necessary 
data = pd.read_csv(file_path)
#Display the first 10 rows of the dataset
print("First 10 rows of the dataset:") 
print(data.head(10))
summary = { 
'columns': data.columns.tolist(), 
'data_types': data.dtypes.to_dict(), 
'missing_values': data.isnull().sum().to_dict(), 
'shape': data.shape 
}
print("\nSummary report of the dataset:") 
print(f"Number of rows: {summary['shape'][0]}") 
print(f"Number of columns: {summary['shape'][1]}") 
print("Columns and their data types:") 
for column, dtype in summary['data_types'].items(): 
    print(f"{column}: {dtype}") 
print("Missing values in each column:") 
for column, missing in summary['missing_values'].items(): 
    print(f"{column}: {missing}") 