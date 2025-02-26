import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('cleaned_standardized_customer_transactions.csv')
plt.figure(figsize=(10, 6)) 
sns.boxplot(x=df['transaction_amount']) 
plt.title('Boxplot for Transaction Amounts') 
plt.xlabel('Transaction Amount') 
plt.show()
plt.figure(figsize=(10, 6)) 
sns.boxplot(x=df['customer_age']) 
plt.title('Boxplot for Customer Age') 
plt.xlabel('Customer Age') 
plt.show()
Q1 = df['transaction_amount'].quantile(0.25) 
Q3 = df['transaction_amount'].quantile(0.75) 
IQR = Q3 - Q1  
lower_bound = Q1 - 1.5 * IQR 
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['transaction_amount'] < lower_bound) | 
(df['transaction_amount'] > upper_bound)] 
print(f"Number of outliers in transaction_amount: {outliers.shape[0]}")
df_cleaned = df[(df['transaction_amount'] >= lower_bound) & (df['transaction_amount'] <= 
upper_bound)]
df_cleaned.to_csv('cleaned_standardized_customer_transactions_no_outliers.csv', index=False)
