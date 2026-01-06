import pandas as pd

file_path = 'features.xlsx'
df = pd.read_excel(file_path)

# Columns to remove (Attribute Names)
to_remove = [
    'Date Analyzed', 
    'Observer Name', 
    'Wall Damage (N,S,E,W)',
    '**Date Analyzed**', # In case of markdown formatting in excel
    '**Observer Name**'
]

# Filter
df = df[~df['Attribute Name'].isin(to_remove)]

# Save
df.to_excel(file_path, index=False)
print("Removed legacy/duplicate columns from features.xlsx")
