def analyze_gaps(df):
    def risk_level(status):
        if status == "Not Implemented":
            return "High"
        elif status == "Partially Implemented":
            return "Medium"
        else:
            return "Low"

    df["Risk_Level"] = df["status"].apply(risk_level)
    df["Mitigation"] = df["Risk_Level"].map({
        "High": "Implement immediately to meet compliance.",
        "Medium": "Enhance existing controls to fully comply.",
        "Low": "Maintain current control."
    })

    compliance_score = round((df["status"] == "Implemented").sum() / len(df) * 100, 2)
    return {"score": compliance_score, "details": df}
