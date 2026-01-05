import pandas as pd
import os
import glob
import argparse

def generate_reports():
    parser = argparse.ArgumentParser(description='Generate property report scaffolds.')
    parser.add_argument('--disaster', type=str, default='mayfield', help='Name of the disaster folder (e.g., "mayfield", "Lahaina_Fire")')
    args = parser.parse_args()

    base_path = '/Users/rebeccanapolitano/antigravityProjects/disasterRecon'
    disaster_path = os.path.join(base_path, args.disaster)
    individual_path = os.path.join(disaster_path, 'individual')
    features_path = os.path.join(base_path, 'features (1).xlsx')
    
    # Load Excel Data
    try:
        df_features = pd.read_excel(features_path)
    except Exception as e:
        print(f"Error reading features excel: {e}")
        return

    # Iterate properties
    if not os.path.exists(individual_path):
        print(f"No folder found at {individual_path}")
        return

    properties = [d for d in os.listdir(individual_path) if os.path.isdir(os.path.join(individual_path, d))]
    
    for prop in properties:
        prop_dir = os.path.join(individual_path, prop)
        report_path = os.path.join(prop_dir, 'Report.md')
        
        # Find images
        before_images = glob.glob(os.path.join(prop_dir, 'photos', 'before', '*'))
        after_images = glob.glob(os.path.join(prop_dir, 'photos', 'after', '*'))
        pdfs = glob.glob(os.path.join(prop_dir, 'files', '*.pdf'))
        
        with open(report_path, 'w') as f:
            f.write(f"# Property Analysis: {prop}\n\n")
            
            f.write("## Images\n")
            f.write("### Before\n")
            if before_images:
                for img in before_images:
                    rel_path = os.path.relpath(img, prop_dir)
                    f.write(f"![Before Image]({rel_path})\n\n")
            else:
                f.write("_No before images found._\n\n")
                
            f.write("### After\n")
            if after_images:
                for img in after_images:
                    rel_path = os.path.relpath(img, prop_dir)
                    f.write(f"![After Image]({rel_path})\n\n")
            else:
                f.write("_No after images found._\n\n")
            
            f.write("## Documents\n")
            if pdfs:
                for pdf in pdfs:
                    rel_path = os.path.relpath(pdf, prop_dir)
                    f.write(f"- [{os.path.basename(pdf)}]({rel_path})\n")
            else:
                f.write("_No PDF documents found._\n\n")
            
            f.write("## Feature Analysis\n")
            f.write("> **Note:** If observed value is not in 'Input Choices', please note 'Add [Value] to choices'.\n\n")
            
            f.write("| Attribute Name | Observation (Before) | Observation (After) | Uncertainty | Input Choices | Identification Guide |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            
            # Populate table rows
            for index, row in df_features.iterrows():
                attr_name = row.get('Attribute Name', '')
                guide = row.get('Reasoning / Identification Guide (Agent Prompt)', '')
                choices = row.get('Input Choices / Options', '')
                uncertainty = row.get('Uncertainty (unc)', '')
                
                # Sanitize content for markdown table
                def clean(text):
                    return str(text).replace('|', '\\|').replace('\n', ' ').replace('nan', '')

                guide = clean(guide)
                choices = clean(choices)
                uncertainty = clean(uncertainty)

                # Special handling for Timeline/Existence
                if 'Existence (Multi-yr)' in str(attr_name):
                     # Expand to -5 to +5 years
                     for i in range(-5, 6):
                         year_offset = f"{i:+}".replace('+', '') if i <= 0 else f"+{i}"
                         if i == 0: year_label = "Existence (Event Year)"
                         else: year_label = f"Existence (Year {year_offset})"
                         
                         f.write(f"| {year_label} | | | {uncertainty} | Yes / No | {guide} |\n")
                else:
                    if pd.notna(attr_name):
                        f.write(f"| {attr_name} | | | {uncertainty} | {choices} | {guide} |\n")

        print(f"Generated report for {prop} at {report_path}")

if __name__ == "__main__":
    generate_reports()
