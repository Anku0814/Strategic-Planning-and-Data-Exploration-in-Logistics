# Strategic Planning and Data Exploration in Logistics

## Internship – Task 1

**Author:** Ankush Ramola  
**Program:** Master of Computer Applications (MCA)  
**Project Area:** Logistics Data Analytics  
**Primary Focus:** Indian Rail Freight Movement  
**Dataset:** Inter/Intra-State Movements/Flows of Goods by Rail, River and Air – 2024–25

## Project Overview

This project focuses on the strategic planning and initial data exploration phase of a logistics data analysis project.

The objective is to understand how freight movement data can be used to identify logistics patterns, define useful performance indicators, and support planning and resource allocation.

The analysis is based on the official **Inter/Intra-State Movements/Flows of Goods by Rail, River and Air – 2024–25** publication released by the **Directorate General of Commercial Intelligence & Statistics (DGCIS), Government of India**.

The main focus of this task is **rail freight movement in India**.

## Objectives

- Understand the structure of Indian rail freight movement.
- Identify important logistics KPIs.
- Study state-wise and commodity-wise freight patterns.
- Explore inter-state origin-destination movements.
- Identify applications of data science in logistics planning.
- Develop a Python-based roadmap for further analysis.
- Explore clustering, forecasting and optimization methods.

## Key Performance Indicators

| KPI | Purpose |
|---|---|
| Total Rail Freight | Measures overall freight movement |
| Outward Freight | Identifies major freight-origin states |
| Inward Freight | Identifies major destination states |
| Internal Freight | Measures movement within states |
| Inter-State Freight Share | Measures cross-state freight dependence |
| Commodity Share | Measures concentration of major commodities |
| Year-on-Year Growth | Tracks changes in freight movement |

## Data Science Approach

### Descriptive Analytics
Used to summarize freight movement and establish the overall logistics profile.

### Exploratory Data Analysis
Used to identify freight distribution, state-level patterns, commodity concentration and major origin-destination flows.

### Clustering
States can be grouped according to freight characteristics such as total, inward, outward and internal movement.

### Forecasting
Historical DGCIS datasets can be combined with the 2024–25 data to study future freight-demand trends.

### Optimization
A later stage can model allocation of limited freight capacity among high-demand corridors while considering demand and capacity constraints.

## Project Roadmap

```text
Data Collection
      ↓
Data Extraction
      ↓
Data Cleaning & Validation
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
KPI Analysis
      ↓
State & Commodity Analysis
      ↓
Origin-Destination Analysis
      ↓
Clustering
      ↓
Forecasting
      ↓
Optimization
      ↓
Logistics Insights & Recommendations
```

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Microsoft Excel / Spreadsheet tools
- GitHub

## Repository Contents

- **`Ankush_Ramola_Task_1.pdf`** – Complete Task 1 strategic planning report.
- **`exploratory_analysis.py`** – Python starter workflow for data loading, validation, exploration and analysis.
- **`README.md`** – Project documentation and methodology.
- **`.gitignore`** – Files excluded from version control.

## Python Analysis

The Python script demonstrates the proposed workflow for:

- Loading the dataset
- Standardizing column names
- Checking missing values
- Calculating state-level freight
- Calculating freight shares
- Visualizing top states
- Creating an origin-destination matrix
- Visualizing freight flows
- Performing basic K-Means clustering

The exact column names will be adjusted after the detailed DGCIS statistical tables are downloaded and inspected.

## Dataset and Official Source

**DGCIS Inland Trade Statistics:**  
https://www.dgciskol.gov.in/pub_inland.aspx

**DGCIS 2024–25 Publication:**  
https://www.dgciskol.gov.in/writereaddata/Downloads/20260227120851IT%20REPORT_2024_25_Final.pdf

The project uses the official Government of India source. The complete government dataset is not duplicated in this repository; the relevant detailed tables should be obtained from the original DGCIS source.

## Expected Outcomes

- A structured KPI framework for Indian rail freight.
- State-wise freight insights.
- Commodity-level freight insights.
- Identification of major freight corridors.
- A framework for state-level clustering.
- A foundation for freight-demand forecasting.
- A conceptual approach to capacity and resource allocation.
- A reproducible Python-based analysis workflow.

## Limitations

- The public data does not provide real-time train locations.
- Transit time and detailed operational information may not be available.
- Wagon availability and terminal capacity are outside the scope of this dataset.
- Freight quantity alone does not represent transportation cost or profitability.
- Forecasting depends on the availability of comparable historical datasets.
- Optimization would require additional operational assumptions.

## Task 1 Deliverable

This repository contains the completed **Week 1 – Strategic Planning and Data Exploration in Logistics** deliverable, covering:

- Background research
- Project definition
- Logistics scenario
- KPIs
- Dataset research
- Data science methodologies
- Strategic roadmap
- Python code illustration
- Risks and limitations
- Expected outcomes
- Conclusion

## Author

**Ankush Ramola**  
Master of Computer Applications (MCA)

**GitHub Repository:**  
https://github.com/Anku0814/Strategic-Planning-and-Data-Exploration-in-Logistics
