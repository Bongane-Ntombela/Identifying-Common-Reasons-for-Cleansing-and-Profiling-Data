import pandas as pd 

df = pd.read_csv('standardized_customer_transactions.csv') 

# Normalize column names (convert to lowercase and strip spaces)
df.columns = df.columns.str.strip().str.lower()

print("Column names after normalization:")
print(df.columns)

# Fix the incorrect column name reference
df['transactiondate'] = pd.to_datetime(df['transactiondate'], errors='coerce')
df['transaction_amount'] = pd.to_numeric(df['transaction_amount'], errors='coerce')

df.to_csv('cleaned_standardized_customer_transactions.csv', index=False)
print("File saved successfully!")
