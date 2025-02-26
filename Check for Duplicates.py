import pandas as pd 
df = pd.read_csv('updated_customer_transactions.csv')
duplicate_mask = df.duplicated() 
num_duplicates = duplicate_mask.sum() 
print("Number of duplicate rows:", num_duplicates) 
cleaned_df = df.drop_duplicates() 
num_removed = len(df) - len(cleaned_df) 
print("Number of duplicates removed:", num_removed) 
cleaned_df.to_csv('cleaned_customer_transactions.csv', index=False)
