# NYC Taxi Data Analytics Project

## Project Overview
This project involves processing and analyzing NYC Taxi data to gain insights into ride patterns, passenger behavior, and geographic trends. The processed data is visualized in an interactive Tableau dashboard to help users draw actionable conclusions. The workflow integrates data orchestration, transformation, and visualization layers, emphasizing scalability and automation.

## Goals
1. **Data Consolidation:** Aggregate NYC taxi data and enrich it with geospatial information to enhance analysis.
2. **Data Processing:** Transform raw data into a structured, analytics-ready format.
3. **Scalable Storage:** Store processed data in cloud buckets and BigQuery for seamless querying.
4. **Visualization:** Create an interactive Tableau dashboard for actionable insights.
5. **Automation:** Incorporate an orchestration layer to streamline data processing workflows.

---

## Approach

### Step 1: Data Collection
- **Source:** NYC Taxi data obtained from the [NYC Taxi & Limousine Commission website](PLACEHOLDER_FOR_LINK_TO_DATA_SOURCE).
- **Reasoning:** The dataset contains detailed trip records including timestamps, pickup and drop-off locations, and fare amounts. It is essential for understanding urban transportation patterns.

### Step 2: Geospatial Enrichment
- **Process:** Integrated latitude and longitude data by merging NYC Taxi data with their corresponding geospatial files (shapefiles).
- **Reasoning:** Adding geospatial data enables deeper analysis of location-based trends, such as popular pickup/drop-off zones and route optimizations.

### Step 3: Cloud Storage
- **Process:** Uploaded the latest year’s processed data to Google Cloud Storage buckets (PLACEHOLDER_FOR_BUCKET_LINK).
- **Reasoning:** Storing data in the cloud ensures scalability, reliability, and accessibility for further processing and visualization.

### Step 4: Data Orchestration and Processing in Mage AI
- **Process:** Utilized Mage AI to orchestrate and transform data pipelines:
  - Converted datetime columns for detailed time-based analysis.
  - Enriched data with relevant dimensions (e.g., payment types, trip distances, etc.).
  - Eliminated duplicates and ensured consistency.
- **Reasoning:** A data orchestration layer allows for modular, repeatable workflows and simplifies managing dependencies between tasks.

### Step 5: Data Storage in BigQuery
- **Process:** Uploaded the processed tables to BigQuery as follows:
  - Fact Table: Contains metrics for analysis.
  - Dimension Tables: Contains metadata like location details, payment types, and ride distances.
- **Reasoning:** BigQuery enables high-performance SQL queries and integrates seamlessly with Tableau for visualization.

### Step 6: Visualization in Tableau
- **Process:** Created an interactive Tableau dashboard (PLACEHOLDER_FOR_DASHBOARD_LINK) to visualize key insights, including:
  - Popular pickup and drop-off locations.
  - Hourly and daily ride patterns.
  - Analysis of trip distances and fare distribution.
- **Reasoning:** Tableau simplifies sharing and exploring insights through intuitive dashboards.

---

## Architecture Diagram
![Architecture](images/architecture.jpg)

---

## Why Use a Data Orchestration Layer?
### Benefits:
1. **Automation:** Mage AI automates repetitive tasks and simplifies scheduling.
2. **Scalability:** Modular pipelines can be scaled as data size increases.
3. **Maintainability:** Makes it easy to modify workflows without impacting the entire system.
4. **Monitoring:** Provides insights into pipeline performance and potential bottlenecks.

### Drawbacks:
1. **Learning Curve:** Requires familiarity with orchestration tools.
2. **Complexity for Small Projects:** May introduce overhead if project scope is limited.
3. **Resource Usage:** Additional compute resources may be required for orchestration.

---

## Future Enhancements
1. **Real-time Data Integration:** Stream real-time trip data into BigQuery for live dashboards.
2. **Advanced Analytics:** Incorporate machine learning models to predict ride demand.
3. **Scalability:** Explore more efficient storage formats (e.g., Parquet) for larger datasets.
4. **Additional Data Sources:** Integrate weather or event data for deeper insights.

---

## References
- NYC Taxi Data: PLACEHOLDER_FOR_LINK_TO_DATA_SOURCE
- Google Cloud Storage: PLACEHOLDER_FOR_BUCKET_LINK
- Tableau Dashboard: PLACEHOLDER_FOR_DASHBOARD_LINK
