import pandas as pd
df = pd.read_csv('customer_transactions.csv')
missing_values = df.isnull().sum() 
percentage_missing = (missing_values / len(df)) * 100 
missing_info = pd.DataFrame({'Missing_Values': missing_values, 'Percentage_Missing': 
percentage_missing}) 
print(missing_info)
mean_transaction_amount = df['transaction_amount'].mean() 
df['transaction_amount'].fillna(mean_transaction_amount, inplace=True)
df.to_csv('updated_customer_transactions.csv', index=False)
