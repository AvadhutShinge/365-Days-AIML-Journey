
import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# Display complete dataset
print("Student Dataset:")
print(df)

# Display first 3 rows
print("\nFirst 3 Students:")
print(df.head(3))

# Dataset information
print("\nDataset Information:")
print(df.info())

# Average marks
print("\nAverage Marks:")
print(df["Marks"].mean())

# Highest marks
print("\nHighest Marks:")
print(df["Marks"].max())

# Lowest marks
print("\nLowest Marks:")
print(df["Marks"].min())

# Filter students with marks above 80
print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])

# Sort students by marks
print("\nSorted Student Data:")
print(df.sort_values(by="Marks", ascending=False))

print("\nDay 27 Completed!")
