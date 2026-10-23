
import pandas as pd

# Load the CSV file
df = pd.read_csv("SQL_Sales_Dataset_200_Rows.xlsx - Sheet1.csv")

# Display first five rows
print(df.head())

# Display rows and columns
print(df.shape)

# Display column information
df.info()

# Display basic statistics
print(df.describe())

# Task 2: Handle missing values and duplicates

# Check missing values
print("Missing values:")
print(df.isnull().sum())

# Count duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values again
print("Missing values after checking:")
print(df.isnull().sum())

# Task 3: Total revenue by category

revenue = df.groupby("category")["total_price"].sum()

print("Total revenue by category:")
print(revenue)

# Task 4: Sort by multiple columns

sorted_df = df.sort_values(
    by=["category", "total_price"],
    ascending=[True, False]
)

print("Data sorted by category and total price:")
print(sorted_df.head(10))


# Task 5: Correlation matrix

correlation = df.corr(numeric_only=True)

print("Correlation Matrix:")
print(correlation.round(2))
