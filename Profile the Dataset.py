import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'cleaned_standardized_customer_transactions_no_outliers.csv'
data = pd.read_csv(file_path)

summary_statistics = data.describe(include='all')
print("Summary Statistics:")
print(summary_statistics)

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(data['transaction_amount'], bins=30, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')  # Separate command on a new line
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=data['transaction_amount'])
plt.title('Boxplot for Transaction Amounts')
plt.xlabel('Transaction Amount')  # Correct placement
plt.show()

numerical_data = data.select_dtypes(include=['number'])
correlation_matrix = numerical_data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()