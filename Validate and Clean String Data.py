import pandas as pd
data = pd.read_csv('cleaned_standardized_customer_transactions_no_outliers.csv')
print(data.head())
data['state'] = data['state'].str.strip().str.lower() 
data['customer_id'] = data['customer_id'].str.strip() 
data['transaction_type'] = data['transaction_type'].str.strip().str.lower() 
missing_states = data['state'].isnull().sum() 
missing_ids = data['customer_id'].isnull().sum()
print(f'Missing state entries: {missing_states}') 
print(f'Missing customer_id entries: {missing_ids}')
print(data.head())
