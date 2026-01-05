import pandas as pd

file_path = '/Users/rebeccanapolitano/antigravityProjects/disasterRecon/features (1).xlsx'
try:
    df = pd.read_excel(file_path)
    print("Columns:", df.columns.tolist())
    
    # Check for timeline or existence related rows
    timeline_rows = df[df['Attribute Name'].astype(str).str.contains('Exist|Year|Time', case=False, na=False)]
    print("\n--- Timeline/Existence Rows ---")
    print(timeline_rows[['Attribute Name', 'Input Choices / Options']].head(10))

    # Check a few rows for Input Choices structure
    print("\n--- Sample Input Choices ---")
    print(df[['Attribute Name', 'Input Choices / Options', 'Uncertainty (unc)']].head(5))

except Exception as e:
    print(e)
