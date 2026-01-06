# Analysis Guidelines for Disaster Reconnaissance

**Crucial**: Read this document before analyzing any property. These rules prevent hallucination and ensure consistency.

## 1. Archetype Classification
- **Do NOT guess**. Check `archetypes.xlsx` carefully.
- **Common Error**: Do not classify small 2-story brick buildings as "Residential" (T1). They are likely **T8 (Main Street Commercial)** or similar.
- **Description**: Provide a **detailed verbal description** of the building in the `Archetype Description` field. Do not use the choices if they are just generic categories; write a sentence (e.g., "Historic 2-story brick commercial building with flat roof and decorative cornice").

## 2. Timeline & Existence
- **Check `Timeline Evidence`**: Look for headers like `2018_satellite.jpg` or `2021_drone.png` in the report.
- **Interpolation Rules**:
    - If you see a photo from 2018 showing the building, mark `Existence (Year -4)` (assuming 2022 event) as **Yes**.
    - If you see it exists in 2018 and 2020, assume it exists in 2019.
    - If "After" photos or a 2022 timeline photo show it destroyed/demolished, mark subsequent years as **No**.
- **No Evidence**: If you have NO photos for a specific post-event year (e.g., Year +3), mark it as **Unknown**. Do NOT guess.

## 3. High Verbosity Areas
Be descriptive! Do not use single words for these fields:
- **Structural Wall System**: Describe the bond (e.g., Running bond, Flemish bond), estimate wythes (e.g., "3-wythe depth visible in rubble"), and note the brick type (e.g., "Buff/Yellow face brick").
- **Material**: Mention colors, textures, and condition. (e.g., "Red brick with lime mortar," "Heavy timber joists splintered").
- **Mechanism of Failure**: Describe the *sequence* if possible. (e.g., "Global collapse. Roof truss failure appears to have pushed out URM walls. Debris is intermixed.").
- **Parapet**: Note decorative styles (e.g., "Corbelled cornice," "Dental molding").

## 4. Input Choices
- **Check `features (1).xlsx`**: Always prefer the "Input Choices" listed in the Excel file.
- **Additions**: If a specific observation (e.g., "Storefront") is not in the list but is accurate, note it in the table.

## 5. Debris Analysis
- Look at the rubble closely.
    - **Mixed debris** (brick + wood) = Simultaneous collapse?
    - **Clean brick pile** = Wall failure?
    - **Roof sitting on ground** = Pancake collapse?

## 6. Uncertainty & Estimation
- **Estimates**: If you are not 100% sure of a numeric value (like "Construction Year" or "Wall Thickness") based on a document, explicitly write `(est)` next to the value.
    - Example: `1900 (est)` instead of just `1900`.
- **Confidence Levels**:
    - **Low Uncertainty**: You have a document (Property Card, Report) stating this fact.
    - **Moderate Uncertainty**: You are estimating based on strong visual norms (e.g., standard brick sizes, architectural style).
    - **High Uncertainty**: You are guessing or the image is unclear.

## 7. Orientation & Facades
- **Objective Terms**: Unless you have confirmed the building's orientation via a map or file metadata (e.g., `north_wall.jpg`), do NOT use cardinal directions (North, South, East, West).
- **Relative Terms**: Use `Front` (facing street), `Rear`, `Left Side`, `Right Side`.
- **Estimation**: If you strongly suspect orientation based on shadows or sun, mark it with `(est)` and HIGH Uncertainty.

## 8. Human vs. Agent Roles
- **Agent (The Draftsman)**:
    - **Drafting**: Fill out the visual basics (Materials, Roof Shapes, Collapse Mechanisms) to 80% completion.
    - **Timeline**: Build the existence timeline from available `photos/timeline/` images.
    - **Flagging**: Mark every uncertain observation (Uncertainty column).
- **Student (The Auditor)**:
    - **Verification**: You MUST check every "High Uncertainty" tag.
    - **GPS**: You are responsible for finding and entering the exact `Latitude` and `Longitude`.
    - **Research**: Use the Toolkit links to find the exact "Construction Year" or confirm "Historic" status.
    - **Logic Check**: Ensure the values make sense (e.g., did the Agent say "Flood Depth: 4ft" when the water line is clearly at the roof?).
