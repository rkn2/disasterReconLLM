# Student Guide: Data Collection & Folder Organization

This guide outlines how to collect data and organize property folders for the Disaster Reconnaissance project. Following this structure is critical for the automated reporting tools to work.

## 1. Folder Structure
For each disaster event you analyze, create a root folder named after the event (e.g., `Mayfield_Tornado`, `Lahaina_Fire`).

**Required Structure:**
```text
[Disaster_Name]/
├── supplementary/        <-- General info about the whole town/area
├── individual/
│   └── [Property Address]/       <-- e.g., "123_Main_St"
│       ├── photos/
│       │   ├── before/           <-- "Before" images go here
│       │   └── after/            <-- "After" images go here
│       └── files/                <-- PDF reports, property cards, etc.
└── features.xlsx         <-- (Optional) Project-level configuration
└── archetypes.xlsx       <-- (Optional) Project-level configuration
```

## 2. What to Collect

### A. Individual Properties (`individual/[Address]/`)
#### Images (`photos/`)
-   **Before Images**: High-quality Google Street View screenshots or historic photos showing the building intact.
    -   *Goal*: Clear view of facade, roof shape, and window layout.
-   **After Images**: Post-disaster photos showing the damage.
    -   *Goal*: Show debris, collapse mechanism, and remaining structural elements.
-   **Timeline Images (`photos/timeline/`)**: Any other photos from years before or after the event.
    -   *Goal*: Track the existence of the building over time.
    -   *Naming*: **CRITICAL**: Start filename with the Year (e.g., `2018_satellite.jpg`, `2021-03_drone.png`).

#### Documents (`files/`)
-   **Property Cards**: PDF exports from county assessor sites.
-   **Technical Reports**: Existing damage assessment reports if available.

### B. General Area (`supplementary/`)
This folder is for context that applies to the entire dataset or town, not just one building.
-   **Maps**: PDF or Image exports from ArcGIS/FEMA showing the path of the tornado/fire or flood plains.
-   **News Reports**: Articles summarizing the overall impact, timeline of the event, and casualty statistics.
-   **Drone Overviews**: High-altitude shots covering multiple blocks (useful for understanding the "Urban Setting" attribute).
-   **Demographics**: Census data or summaries of the town's population and housing stock.

## 3. Data Sources

### A. Location & Context
-   **ArcGIS / FEMA Maps**: Use official disaster maps to locate damaged properties and determine EF-ratings (approximate).
    -   *Look for*: Overlays of tornado paths or flood zones.
-   **Google Earth Pro**: Use the "Historical Imagery" slider (clock icon) to find "Before" images if current ones are updated post-disaster.

### B. Property Details (The "Before")
-   **Zillow / Redfin / Realtor.com**: Search the address to find real estate photos. These often have high-res interior/exterior shots that Google Street View misses.
    -   *Tip*: Even if "Off Market," the listing history often retains photos.
-   **County Assessor (GIS)**: Search the county's GIS portal for "Property Cards." These list construction year, square footage, and materials.

### C. Damage Evidence (The "After")
-   **Social Media**: Twitter (X), Facebook, and TikTok are valuable for real-time disaster footage.
    -   *Search Terms*: "[City Name] tornado", "[Street Name] damage", "aerial footage [City]".
-   **YouTube**: Look for drone flyovers of the disaster zone. Pause and screenshot your specific property if visible.
-   **NOAA / NWS Imagery**: The National Weather Service often releases high-resolution aerial comparison maps after major events.

## 4. Best Practices
1.  **Visual Verification**: Don't rely on just one source. If the assessor says "Brick" but the photo shows "Vinyl Siding," trust the photo (it might be a brick veneer or a renovation).
2.  **File Naming**: Keep filenames descriptive but simple (e.g., `front_facade_before.png`, `roof_collapse_after.jpg`).
3.  **PDFs**: Only put relevant PDFs in the `files/` folder.
