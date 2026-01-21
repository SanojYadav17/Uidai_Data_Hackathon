import pandas as pd
import numpy as np
import os

print("===== AadhaarPulse Index Project Started =====")

# 1. CHECK WORKING DIRECTORY & FILES
print("Current Directory:", os.getcwd())
print("Files in folder:", os.listdir())

# 2. LOAD & MERGE DATASETS
files = [
    "api_data_aadhar_enrolment_0_500000.csv",
    "api_data_aadhar_enrolment_500000_1000000.csv",
    "api_data_aadhar_enrolment_1000000_1006029.csv"
]

dfs = []
for f in files:
    print(f"Loading: {f}")
    dfs.append(pd.read_csv(f))

master_df = pd.concat(dfs, ignore_index=True)

print("\nMaster dataset created")
print("Total rows:", master_df.shape[0])
print("Total columns:", master_df.shape[1])

# 3. ADVANCED DATA CLEANING
print("\nAdvanced cleaning started...")

# Date
master_df["date"] = pd.to_datetime(master_df["date"], errors="coerce")

# Age columns
age_cols = ["age_0_5", "age_5_17", "age_18_greater"]
master_df[age_cols] = master_df[age_cols].fillna(0)

# Text cleaning
master_df["state"] = master_df["state"].astype(str).str.strip().str.lower()
master_df["district"] = master_df["district"].astype(str).str.strip().str.lower()

# State name normalization
state_corrections = {
    "west bangal": "west bengal",
    "westbengal": "west bengal",
    "wb": "west bengal",
    "orissa": "odisha",
    "uttrakhand": "uttarakhand",
    "andaman & nicobar": "andaman and nicobar islands",
    "andaman and nicobar": "andaman and nicobar islands",
    "dadra & nagar haveli and daman & diu": "dadra and nagar haveli and daman and diu"
}

master_df["state"] = master_df["state"].replace(state_corrections)

# Final formatting
master_df["state"] = master_df["state"].str.title()
master_df["district"] = master_df["district"].str.title()

print("Advanced cleaning completed")

# 4. TOTAL ENROLMENT COLUMN
master_df["total_enrolment"] = (
    master_df["age_0_5"] +
    master_df["age_5_17"] +
    master_df["age_18_greater"]
)

print("Total enrolment column created")

# 5. MONTH COLUMN
master_df["month"] = master_df["date"].dt.to_period("M")

# 6. STATE LEVEL AGGREGATION
print("\nAggregating state-wise data...")

state_summary = master_df.groupby("state").agg({
    "total_enrolment": "sum",
    "age_0_5": "sum",
    "age_5_17": "sum",
    "age_18_greater": "sum"
}).reset_index()

print("State summary created")

# 7. AGE COVERAGE SCORE (0–100)
def age_coverage_score(row):
    total = row["age_0_5"] + row["age_5_17"] + row["age_18_greater"]
    if total == 0:
        return 0

    p1 = row["age_0_5"] / total
    p2 = row["age_5_17"] / total
    p3 = row["age_18_greater"] / total

    ideal = 1/3
    deviation = abs(p1 - ideal) + abs(p2 - ideal) + abs(p3 - ideal)
    score = max(0, 100 - deviation * 150)
    return round(score, 2)

state_summary["Age_Coverage_Score"] = state_summary.apply(age_coverage_score, axis=1)
print("Age Coverage Score calculated")

# 8. GROWTH SCORE
print("\nCalculating Growth Score...")

monthly = master_df.groupby(["state", "month"])["total_enrolment"].sum().reset_index()

growth_scores = {}

for state in monthly["state"].unique():
    temp = monthly[monthly["state"] == state].sort_values("month")
    if len(temp) < 2:
        growth_scores[state] = 50
    else:
        growth_rate = temp["total_enrolment"].pct_change().mean()
        score = np.clip((growth_rate + 1) * 50, 0, 100)
        growth_scores[state] = round(score, 2)

state_summary["Growth_Score"] = state_summary["state"].map(growth_scores)
print("Growth Score calculated")

# 9. STABILITY SCORE
print("\nCalculating Stability Score...")

stability_scores = {}

for state in monthly["state"].unique():
    temp = monthly[monthly["state"] == state]
    std = temp["total_enrolment"].std()
    mean = temp["total_enrolment"].mean()

    if mean == 0 or pd.isna(std):
        stability_scores[state] = 0
    else:
        cv = std / mean
        score = np.clip(100 - cv * 100, 0, 100)
        stability_scores[state] = round(score, 2)

state_summary["Stability_Score"] = state_summary["state"].map(stability_scores)
print("Stability Score calculated")

# 10. FINAL AADHAARPULSE INDEX
print("\nCalculating AadhaarPulse Index...")

state_summary["AadhaarPulse_Index"] = (
    0.40 * state_summary["Growth_Score"] +
    0.35 * state_summary["Age_Coverage_Score"] +
    0.25 * state_summary["Stability_Score"]
).round(2)

print("AadhaarPulse Index created")

# 11. RANKING
state_summary = state_summary.sort_values("AadhaarPulse_Index", ascending=False)
state_summary["Rank"] = range(1, len(state_summary) + 1)

# 12. SAVE OUTPUT
output_path = "AadhaarPulse_Index_Statewise.csv"
state_summary.to_csv(output_path, index=False)

print("\n===== PROJECT COMPLETED SUCCESSFULLY =====")
print(f"Final output saved as: {output_path}")

# 13. SHOW RESULTS
print("\nTop 10 States by AadhaarPulse Index:")
print(state_summary.head(10))

print("\nBottom 10 States by AadhaarPulse Index:")
print(state_summary.tail(10))
