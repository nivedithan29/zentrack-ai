# src/tools/csv_export_tool.py
import pandas as pd

def export_to_csv(records, filename="export.csv"):
    """
    records: list of dicts
    """
    if not records:
        print("No records to export.")
        return None
    df = pd.DataFrame(records)
    df.to_csv(filename, index=False)
    print(f"Saved CSV to {filename}")
    return filename
