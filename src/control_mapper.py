import pandas as pd
import json
from gap_analysis import analyze_gaps
from risk_report import generate_report

# Load NIST controls
nist_df = pd.read_csv("data/nist_800_171_controls.csv")

# Load app controls
with open("data/mock_app_controls.json", "r") as f:
    app_data = json.load(f)

app_df = pd.DataFrame(app_data["controls"])

# Merge on Control ID
merged_df = pd.merge(nist_df, app_df, left_on="Control_ID", right_on="control_id", how="left")

# Analyze gaps
results = analyze_gaps(merged_df)

# Generate report
generate_report(results)

print(f"Compliance report generated: {results['score']}% compliance")
