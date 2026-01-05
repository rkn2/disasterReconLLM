# Disaster Reconnaissance Report Generator

This repository contains the tools and workflows for automating the generation of technical reconnaissance reports from post-disaster data collected by students.

## Overview

The system works in two stages:
1.  **Scaffolding (Script)**: A Python script scans the student-organized folders and creates blank `Report.md` files with the correct table structure.
2.  **Analysis (Agent)**: An AI Agent (Gemini/Antigravity) processes the images and fills in the technical observations (archetype, failure mechanism, etc.).

## Prerequisites

-   Python 3.12 or higher.
-   Required libraries: `pandas`, `openpyxl`.

```bash
pip install pandas openpyxl
```

## Repository Structure

-   `generate_reports.py`: The scaffolding script.
-   `features (1).xlsx`: Schema definition for report attributes.
-   `archetypes.xlsx`: Building classification reference.
-   `analysis_guidelines.md`: Instructions for the AI Agent.
-   `.agent/workflows/process_property.md`: The codified workflow for the Agent.
-   `DATA_COLLECTION_GUIDE.md`: Instructions for students (data collection only).

## Usage Guide (Instructor Only)

### Step 1: Prepare the Data
Ensure student data is organized as follows:
```
[Disaster_Name]/
  individual/
    [Property_Address]/
      photos/before/
      photos/after/
      files/
```

### Step 2: Run Scaffolding
Run the python script to generate the blank Markdown reports for all properties in the disaster folder.

```bash
# Example for a folder named "Mayfield_Tornado"
python3 generate_reports.py --disaster Mayfield_Tornado
```

This will create a `Report.md` in every property folder.

### Step 3: Run Agent Analysis
Use your Agent interface to analyze the properties.

**Prompt:**
> "Run the Property Analysis workflow on `[Disaster_Name]/individual/[Property_Address]`."

The agent will:
1.  Read the `Report.md` you just generated.
2.  Look at the photos.
3.  Fill in the "Observation" columns based on `analysis_guidelines.md`.
