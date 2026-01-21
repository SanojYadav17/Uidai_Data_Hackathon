# Uidai_Data_Hackathon
# AadhaarPulse Index project for UIDAI Data Hackathon 2026 using data analytics and visualization.

# AadhaarPulse Index Project

## Overview
This project analyzes Aadhaar enrolment data across Indian states and districts to create a comprehensive "AadhaarPulse Index". The index provides a comparative score for each state based on enrolment growth, age coverage, and stability, helping to identify trends and disparities in Aadhaar adoption.

## Project Structure
- **main.py**: Loads, cleans, merges, and analyzes Aadhaar enrolment data. Calculates the AadhaarPulse Index and exports statewise results.
- **visualization.py**: Generates visualizations (bar charts, histograms, scatter plots) to explore and present the index and its components.
- **api_data_aadhar_enrolment_0_500000.csv**, **api_data_aadhar_enrolment_500000_1000000.csv**, **api_data_aadhar_enrolment_1000000_1006029.csv**: Raw Aadhaar enrolment data split by record ranges.
- **AadhaarPulse_Index_Statewise.csv**: Output file containing the final index and scores for each state.

## Data Processing & Analysis
1. **Data Loading & Merging**: All CSVs are loaded and concatenated into a master DataFrame.
2. **Cleaning**: Handles missing values, normalizes state/district names, and parses dates.
3. **Feature Engineering**:
   - **Total Enrolment**: Sum of all age groups.
   - **Month Extraction**: For time-based analysis.
4. **Aggregation**: State-level aggregation of enrolment and age group data.
5. **Scoring**:
   - **Age Coverage Score**: Measures balance across age groups (0–100 scale).
   - **Growth Score**: Assesses average monthly enrolment growth (0–100 scale).
   - **Stability Score**: Evaluates consistency in enrolment (0–100 scale).
   - **AadhaarPulse Index**: Weighted sum of the above scores.
6. **Ranking**: States are ranked by their AadhaarPulse Index.
7. **Output**: Results are saved to `AadhaarPulse_Index_Statewise.csv`.

## Visualizations
- **Top/Bottom 10 States**: Bar charts of states with highest/lowest index.
- **Index Distribution**: Histogram of index values across all states.
- **Score Relationships**: Scatter plots showing how Age Coverage, Growth, and Stability scores relate to the index.

## How to Run
1. Ensure you have Python 3.x installed.
2. Install required packages:
   ```bash
   pip install pandas numpy matplotlib
   ```
3. Place all CSV files in the same directory as the scripts.
4. Run the analysis:
   ```bash
   python main.py
   ```
5. Generate visualizations:
   ```bash
   python visualization.py
   ```

## Output
- `AadhaarPulse_Index_Statewise.csv`: Contains statewise scores and rankings.
- Visualizations: Displayed interactively (not saved by default).

## Author
UIDAI Data Hackathon Project

---
*For questions or suggestions, please contact the project maintainer.*
