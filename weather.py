
import pandas as pd
import matplotlib.pyplot as plt

# Create a messy 15-day weather log with one duplicate row
data = {
    "Date": [
        "2026-09-01", "2026-09-02", "2026-09-03",
        "2026-09-04", "2026-09-05", "2026-09-06",
        "2026-09-07", "2026-09-08", "2026-09-09",
        "2026-09-10", "2026-09-11", "2026-09-12",
        "2026-09-13", "2026-09-14", "2026-09-15",
        "2026-09-15"
    ],
    "City": [
        " Islamabad ", "ISLAMABAD", "lahore", " Lahore ",
        "KARACHI", "karachi ", " Islamabad", "Lahore",
        "KARACHI", "islamabad", " Lahore ", "Karachi",
        "ISLAMABAD", "lahore", " Karachi ", " Karachi "
    ],
    "Temperature": [
        "32C", "30C", "35C", "33C", "31C", "29C",
        "34C", "32C", "30C", "31C", "34C", "28C",
        "33C", "36C", "29C", "29C"
    ],
    "Humidity": [
        55, 58, None, 62, 65, None, 50, 57,
        68, 54, None, 72, 52, 45, 70, 70
    ],
    "Condition": [
        " sunny ", "CLOUDY", "Rainy", " sunny",
        "RAINY ", "cloudy", "SUNNY", "Cloudy ",
        " rainy", "Sunny", "CLOUDY", "Rainy",
        " Sunny ", "sunny", "CLOUDY", "CLOUDY"
    ]
}

df = pd.DataFrame(data)

# Clean text columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# Remove the temperature unit and convert to numbers
df["Temperature"] = (
    df["Temperature"]
    .str.replace("C", "", regex=False)
    .astype(float)
)

# Convert dates to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Remove duplicate rows
df = df.drop_duplicates().reset_index(drop=True)
print("Rows after dropping duplicates:", len(df))

# Fill missing humidity with the median
median_humidity = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_humidity)

print("Missing Humidity filled with median:", median_humidity)

# One-hot encode the Condition column
encoded = pd.get_dummies(
    df["Condition"], prefix="Condition", dtype=int
)

print("\nEncoded Condition columns:")
print(encoded.to_string(index=False))

# Print condition counts
print("\nCondition counts:")
print(df["Condition"].value_counts())

# Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])
print(
    "\nCorrelation (Temperature, Humidity):",
    round(correlation, 2)
)

# Create a 2 x 2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Weather Overview", fontsize=16)

# 1. Line plot: Temperature over Date
axes[0, 0].plot(
    df["Date"], df["Temperature"], marker="o"
)
axes[0, 0].set_title("Temperature Over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=35)

# 2. Scatter plot: Temperature vs Humidity
axes[0, 1].scatter(
    df["Temperature"], df["Humidity"]
)
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity")

# 3. Pie chart: Number of days per condition
condition_counts = df["Condition"].value_counts()
axes[1, 0].pie(
    condition_counts,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Days by Condition")

# 4. Histogram: Temperature distribution
axes[1, 1].hist(
    df["Temperature"], bins=6, edgecolor="black"
)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the complete dashboard
plt.savefig("weather_dashboard.png", dpi=300)
print("\nSaved weather_dashboard.png")

plt.show()