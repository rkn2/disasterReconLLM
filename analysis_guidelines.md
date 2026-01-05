# Analysis Guidelines for Disaster Reconnaissance

**Crucial**: Read this document before analyzing any property. These rules prevent hallucination and ensure consistency.

## 1. Archetype Classification
- **Do NOT guess**. Check `archetypes.xlsx` carefully.
- **Common Error**: Do not classify small 2-story brick buildings as "Residential" (T1). They are likely **T8 (Main Street Commercial)** or similar.
- **Description**: Provide a **detailed verbal description** of the building in the `Archetype Description` field. Do not use the choices if they are just generic categories; write a sentence (e.g., "Historic 2-story brick commercial building with flat roof and decorative cornice").

## 2. Timeline & Existence
- **Pre-Event**: If the building is visible in "Before" photos, mark Pre-Event years as **Yes**.
- **Post-Event**: Unless you have specific multi-year aerial imagery confirming the building was/is present in years +1 to +5, mark these as **Unknown**.
    - *Exception*: If you have definitive proof it was demolished and verified as empty for years, you might say "No", but "Unknown" is safer if you only have a snapshot.

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
