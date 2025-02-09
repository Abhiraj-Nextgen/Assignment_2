import pandas as pd
import numpy as np

data = {'Name': ['Abhiraj', 'Krish', 'Aarav', 'Adarsh'], #Creating a DataFrame
        'Age': [24, 31, 26, 35],
        'Salary': [70000, 100000, 60000, 80000]}
df = pd.DataFrame(data)

#Read data from CSV file 
df.to_csv('sample_data.csv', index=False)  # Save to CSV
df_csv = pd.read_csv('sample_data.csv')  # Read from CSV

print("First few rows:\n", df.head()) #Inspecting the first few rows

print("Salary column:\n", df['Salary']) #Selecting a column and inspect that column

df_filtered = df[df['Age'] > 30] #Filtering rows based on some criteria (Age > 30)
print("Filtered DataFrame (Age > 30):\n", df_filtered)

df['Bonus'] = df['Salary'] * 0.1 #Creating a new column (Bonus = 10% of Salary)
print("DataFrame with Bonus column:\n", df)

df_grouped = df.groupby('Age').agg({'Salary': 'mean'}) #Grouping a column and aggregate it (Mean Salary by Age Group)
print("Grouped DataFrame:\n", df_grouped)

df2 = pd.DataFrame({'Name': ['Abhiraj', 'Krish', 'Aarav', 'Adarsh'], #Merging two DataFrames on a shared column
                    'Department': ['HR', 'IT', 'Finance', 'Marketing']})
df_merged = pd.merge(df, df2, on='Name')
print("Merged DataFrame:\n", df_merged)

#Handle missing data (filling NaN with mean value)
df_missing = df.copy()
df_missing.loc[2, 'Salary'] = np.nan  #NaN
df_missing.fillna(df.mean(numeric_only=True), inplace=True)
print("DataFrame after handling missing values:\n", df_missing)

#Using pivot to reshape the DataFrame
df_pivot = df.pivot(index='Name', columns='Age', values='Salary')
print("Pivoted DataFrame:\n", df_pivot)
