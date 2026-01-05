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

## Features & Schema

The core logic of the reports is defined in **[features (1).xlsx](features%20(1).xlsx)**. This file acts as the configuration for both the script and the AI Agent.

-   **Attribute Name**: The actual field being analyzed (e.g., "Archetype Number", "No. of Stories").
-   **Input Choices / Options**: Constrains the AI to valid outputs (e.g., "1, 2, 3+" or "Brick, CMU, Wood").
-   **Reasoning / Identification Guide**: This column provides the prompt logic or "thinking instructions" for the AI Agent.

*To change what the agent looks for, edit this Excel file.*

## Usage Guide (Instructor Only)

### Step 1: Prepare the Data
Ensure student data is organized correctly. Here is an example using the included `mayfield` dataset:

```text
mayfield/
├── supplementary/
│   ├── Mayfield SUA Appendix C - Historic Survey-compressed.pdf
│   └── 1984.pdf
└── individual/
    └── address1/
        ├── photos/
        │   ├── before/
        │   │   └── front before.png
        │   └── after/
        │       ├── front after.png
        │       └── damaged.png
        └── files/
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

**Option A: Single Property**
> "Run the Property Analysis workflow on `[Disaster_Name]/individual/[Property_Address]`."

**Option B: Batch Processing (All Properties)**
> "Run the Batch Processing workflow on `[Disaster_Name]`."

The agent will:
1.  Loop through all folders.
2.  Check if `Report.md` is empty/new.
3.  If empty, it will analyze the photos and fill it.

## Example Output

You can see a complete example of the folder structure and a finalized report in the `mayfield` folder included in this repo.

-   **[mayfield/individual/address1/Report.md](mayfield/individual/address1/Report.md)**: This is an example of a report that has been scaffolded by the script and then populated by the Agent with visual observations.
