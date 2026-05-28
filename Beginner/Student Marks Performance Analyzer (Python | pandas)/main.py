import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("Python\Projects\Beginner\Student analyser\students.csv")

# Calculate total marks
df["Total"] = df["Math"] + df["Science"] + df["English"]

# Calculate average
df["Average"] = df["Total"] / 3

# Calculate percentage
df["Percentage"] = (df["Total"] / 300) * 100

# Rank students (highest total = rank 1)
df["Rank"] = df["Total"].rank(ascending=False)

# Best student
best_student = df.loc[df["Total"].idxmax(), "Name"]

# Subject averages
subject_avg = df[["Math", "Science", "English"]].mean()

print("\n===== STUDENT REPORT =====\n")
print(df)

print("\n===== SUBJECT AVERAGES =====\n")
print(subject_avg)

print("\nBEST STUDENT:", best_student)
