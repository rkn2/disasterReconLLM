---
description: Process ALL property folders in a disaster directory, skipping those already completed.
---

1.  **Identify Target Scope**
    -   Ask the user (or confirm from context) which `[Disaster_Name]` folder to process (e.g., `Mayfield_Tornado`).
    -   Locate `[Disaster_Name]/individual/`.

2.  **List Properties**
    -   Use `list_dir` to get all subfolders in `individual/`.

3.  **Iterate and Check Status**
    -   For **EACH** property folder:
        1.  Check `Report.md`.
        2.  **Skip condition**: If `Report.md` contains filled-in observations (i.e., it doesn't just look like the blank template), skip it.
            -   *Check*: Does the table have values other than empty pipes `| |`?
        3.  **Process condition**: If `Report.md` is missing or is just the blank scaffold:
            -   **Execute Analysis**: Perform the steps defined in `process_property.md` (Check Context -> Inspect Evidence -> Perform Analysis).
            -   *Optimization*: Read the guidelines once at the start, don't re-read for every single property.

4.  **Final Report**
    -   Summarize which properties were processed and which were skipped.
