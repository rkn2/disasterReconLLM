---
description: Process a single property folder to generate a technical report.
---

1.  **Read Guidelines**
    -   Read `analysis_guidelines.md` to load the rules into context.
    -   Read `features.xlsx` and `archetypes.xlsx` if you need to refresh valid inputs.

2.  **Scaffold Report**
    -   Check if `Report.md` exists in the property folder.
    -   If not, run `python3 generate_reports.py --disaster [Disaster_Name]`.
    -   // turbo
    -   If it does exist but is empty of observations, proceed.

3.  **Check Context**
    -   Look in `../../supplementary` (or `[Disaster_Name]/supplementary`) for context files.
    -   Read any PDFs or text files there (e.g., National Register docs, Disaster Summary) to understand the area's history and the disaster's specifics.
    -   *Goal*: Establish the "Construction Year", "Significance", or "EF-Rating" base values.

4.  **Inspect Evidence**
    -   Use `view_file` to look at:
        -   `photos/before/*`
        -   `photos/after/*`
        -   `files/*.pdf` (if any)

4.  **Perform Analysis (The "Brain" Work)**
    -   Analyze the images based on the High Verbosity rules in the guidelines.
    -   Look specifically for:
        -   Archetype inputs (verify T-code).
        -   Failure Mechanism (Debris mix).
        -   Materials (Bond, color, texture).
    -   Fill in `Report.md`.

5.  **Review**
    -   Double-check that "Existence (Year +X)" is Unknown if you lack data.
    -   Ensure descriptions are verbose sentences, not just "Brick" or "Collapse".
