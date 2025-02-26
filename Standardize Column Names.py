import pandas as pd
df = pd.read_csv('cleaned_customer_transactions.csv')
df.columns = df.columns.str.lower() 
df.columns = df.columns.str.replace(' ', '') 
df.columns = df.columns.str.replace('[^a-zA-Z0-9]', '')
df.to_csv('standardized_customer_transactions.csv', index=False)