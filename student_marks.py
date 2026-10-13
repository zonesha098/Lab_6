
import pandas as pd
import matplotlib.pyplot as plt

# Student data
names = [
    "  ali  ",
    "SARA",
    "ahMED ",
    "  Fatima",
    "USMAN",
    "aYEsHa ",
    "bilal",
    "  HINA  "
]

marks = ["78", "85", "absent", "92", "67", "88", "74", "81"]

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Clean names
df["Name"] = df["Name"].str.strip().str.title()

# Convert marks to numeric values
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Fill missing marks with the mean of the other students
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

# Print cleaned data
print("Cleaned Student Marks:")
print(df)
print("\nMean used for the absent student:", round(mean_marks, 2))

# Plot marks
plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=30)
plt.tight_layout()

# Save plot in the Lab_6 folder
plt.savefig("marks_bar.png")
plt.show()