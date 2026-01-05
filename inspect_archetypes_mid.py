import pandas as pd
base = '/Users/rebeccanapolitano/antigravityProjects/disasterRecon'
df_arch = pd.read_excel(f'{base}/archetypes.xlsx')
print(df_arch.iloc[5:15].to_string(index=False))
