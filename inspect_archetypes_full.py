import pandas as pd

base = '/Users/rebeccanapolitano/antigravityProjects/disasterRecon'
print("--- Full Archetypes List ---")
df_arch = pd.read_excel(f'{base}/archetypes.xlsx')
print(df_arch.to_string(index=False))

print("\n--- Feature: Archetype Description ---")
df_feat = pd.read_excel(f'{base}/features (1).xlsx')
row = df_feat[df_feat['Attribute Name'] == 'Archetype Description']
print(row.to_string(index=False))
