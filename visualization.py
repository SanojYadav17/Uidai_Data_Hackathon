import pandas as pd
import matplotlib.pyplot as plt

# LOAD FINAL OUTPUT DATA
df = pd.read_csv("AadhaarPulse_Index_Statewise.csv")

print("Visualization started...")
print(df.head())

# 1. TOP 10 STATES BAR CHART
top10 = df.sort_values("AadhaarPulse_Index", ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top10["state"], top10["AadhaarPulse_Index"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 States by AadhaarPulse Index")
plt.xlabel("State")
plt.ylabel("AadhaarPulse Index")
plt.tight_layout()
plt.show()

# 2. BOTTOM 10 STATES BAR CHART
bottom10 = df.sort_values("AadhaarPulse_Index", ascending=True).head(10)

plt.figure(figsize=(12,6))
plt.bar(bottom10["state"], bottom10["AadhaarPulse_Index"])
plt.xticks(rotation=45, ha="right")
plt.title("Bottom 10 States by AadhaarPulse Index")
plt.xlabel("State")
plt.ylabel("AadhaarPulse Index")
plt.tight_layout()
plt.show()

# 3. INDEX DISTRIBUTION (HISTOGRAM)
plt.figure(figsize=(10,6))
plt.hist(df["AadhaarPulse_Index"], bins=10)
plt.title("Distribution of AadhaarPulse Index Across States")
plt.xlabel("AadhaarPulse Index")
plt.ylabel("Number of States")
plt.tight_layout()
plt.show()

# 4. AGE COVERAGE VS INDEX SCATTER
plt.figure(figsize=(10,6))
plt.scatter(df["Age_Coverage_Score"], df["AadhaarPulse_Index"])
plt.title("Age Coverage Score vs AadhaarPulse Index")
plt.xlabel("Age Coverage Score")
plt.ylabel("AadhaarPulse Index")
plt.tight_layout()
plt.show()

# 5. GROWTH SCORE VS INDEX SCATTER
plt.figure(figsize=(10,6))
plt.scatter(df["Growth_Score"], df["AadhaarPulse_Index"])
plt.title("Growth Score vs AadhaarPulse Index")
plt.xlabel("Growth Score")
plt.ylabel("AadhaarPulse Index")
plt.tight_layout()
plt.show()

# 6. STABILITY SCORE VS INDEX SCATTER
plt.figure(figsize=(10,6))
plt.scatter(df["Stability_Score"], df["AadhaarPulse_Index"])
plt.title("Stability Score vs AadhaarPulse Index")
plt.xlabel("Stability Score")
plt.ylabel("AadhaarPulse Index")
plt.tight_layout()
plt.show()

print("All visualizations generated successfully.")
