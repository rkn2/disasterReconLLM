import pandas as pd
import os

base_path = '/Users/rebeccanapolitano/antigravityProjects/disasterRecon'
features_path = os.path.join(base_path, 'features (1).xlsx')
archetypes_path = os.path.join(base_path, 'archetypes.xlsx')
address1_path = os.path.join(base_path, 'mayfield/individual/address1')

print("--- Features Excel ---")
try:
    df_features = pd.read_excel(features_path)
    print("Columns:", df_features.columns.tolist())
    print("First 2 rows:")
    print(df_features.head(2))
except Exception as e:
    print("Error reading features:", e)

print("\n--- Archetypes Excel ---")
try:
    df_arch = pd.read_excel(archetypes_path)
    print("Columns:", df_arch.columns.tolist())
    print("First 2 rows:")
    print(df_arch.head(2))
except Exception as e:
    print("Error reading archetypes:", e)

print("\n--- Address1 Contents ---")
for root, dirs, files in os.walk(address1_path):
    level = root.replace(address1_path, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print('{}{}/'.format(indent, os.path.basename(root)))
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print('{}{}'.format(subindent, f))
