import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "top universities.csv"
data = pd.read_csv(file_path)

# Overview of the dataset
print("Dataset Overview:\n")
print(data.info())
print("\nFirst 5 Rows:\n")
print(data.head())

# Preprocessing
# Check for missing values
print("\nMissing Values:\n")
print(data.isnull().sum())

# Check for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())

# Remove duplicates if any
data = data.drop_duplicates()

# Exploratory Data Analysis (EDA)
# 1. Distribution of universities by country
'''country_counts = data['Country'].value_counts()
plt.figure(figsize=(12, 6))
country_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries with the Most Universities')
plt.ylabel('Number of Universities')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''
# 2. Average Global Rank by Country (Top 10)
average_rank = data.groupby('Country')['Global Rank'].mean().sort_values()
plt.figure(figsize=(12, 6))
average_rank.head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Countries with Best Average Rankings')
plt.ylabel('Average Global Rank (Lower is Better)')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Distribution of Rankings
plt.figure(figsize=(12, 6))
sns.histplot(data['Global Rank'], kde=True, bins=30, color='green')
plt.title('Distribution of Global Rankings')
plt.xlabel('Global Rank')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Universities per Region (Top 10)
region_counts = data['Region'].value_counts()
plt.figure(figsize=(12, 6))
region_counts.head(10).plot(kind='bar', color='purple')
plt.title('Top 10 Regions with Most Universities')
plt.ylabel('Number of Universities')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Summary Report
print("\nSummary of Analysis:\n")
print(f"Total Universities: {data.shape[0]}")
print(f"Total Countries: {data['Country'].nunique()}")
print(f"Total Regions: {data['Region'].nunique()}")

# Save preprocessed data
output_file = "cleaned_top_universities.csv"
data.to_csv(output_file, index=False)
print(f"Preprocessed data saved to {output_file}")


