# Crop Health Monitoring System

A data-driven crop monitoring project that uses NDVI-based analysis to classify crop health and visualize agricultural conditions.

This workspace contains:
- A large agriculture dataset (`agriculture_dataset.csv`)
- An interactive Streamlit dashboard (`app.py`)
- An exploratory notebook workflow (`MantraJain_DIVP_PBL.ipynb`)

## Project Goals

- Monitor crop health with NDVI and related environmental features.
- Classify crop regions into **Unhealthy**, **Moderate**, and **Healthy** classes.
- Provide visual analytics (correlation heatmap, NDVI distribution, pie chart).
- Support precision agriculture decisions with summary metrics and recommendations.

## Repository Structure

- `app.py`: Streamlit app for uploading CSV data and running full analysis interactively.
- `agriculture_dataset.csv`: Primary dataset used for crop health analysis.
- `MantraJain_DIVP_PBL.ipynb`: Notebook pipeline (originally Colab-style) showing step-by-step data loading, plotting, filtering, and classification.

## Dataset Summary (`agriculture_dataset.csv`)

- File size: **75,859,560 bytes** (~75.9 MB)
- Number of rows: **212,019**
- Number of columns: **32**

### Columns

1. High_Resolution_RGB
2. Multispectral_Images
3. Thermal_Images
4. Temporal_Images
5. Spatial_Resolution
6. GPS_Coordinates
7. Field_Boundaries
8. Elevation_Data
9. Canopy_Coverage
10. NDVI
11. SAVI
12. Chlorophyll_Content
13. Leaf_Area_Index
14. Crop_Stress_Indicator
15. Temperature
16. Humidity
17. Rainfall
18. Wind_Speed
19. Soil_Moisture
20. Soil_pH
21. Organic_Matter
22. Pest_Hotspots
23. Weed_Coverage
24. Pest_Damage
25. Crop_Growth_Stage
26. Expected_Yield
27. Crop_Type
28. Ground_Truth_Segmentation
29. Bounding_Boxes
30. Water_Flow
31. Drainage_Features
32. Crop_Health_Label

### Quick Profile

- Crop type distribution:
  - Wheat: 126,991
  - Maize: 63,785
  - Rice: 21,243
- Crop_Health_Label distribution:
  - 0: 63,821
  - 1: 148,198
- NDVI statistics:
  - Min: -0.1653
  - Max: 1.1580
  - Mean: 0.5003

## Streamlit Application (`app.py`)

The app provides an end-to-end workflow after CSV upload:

1. Dataset preview (`head()`)
2. Row/column count and column listing
3. Missing value inspection
4. Correlation heatmap for numeric columns
5. NDVI histogram
6. Bilateral filter smoothing on NDVI sequence
7. Rule-based crop health classification
8. Percentage distribution of classes
9. Summary table for reporting
10. Pie chart for class distribution
11. Final recommendation based on unhealthy percentage

### Classification Rules Used

- NDVI < 0.2 -> Unhealthy
- 0.2 <= NDVI < 0.5 -> Moderate
- NDVI >= 0.5 -> Healthy

## Notebook Workflow (`MantraJain_DIVP_PBL.ipynb`)

The notebook demonstrates a similar workflow in exploratory format:

- Imports data and libraries (OpenCV, NumPy, Pandas, Matplotlib, Seaborn)
- Downloads data using KaggleHub in Colab context
- Loads CSV and inspects shape/columns
- Plots correlation heatmap
- Plots NDVI histogram
- Applies bilateral filtering to NDVI
- Classifies health status by NDVI thresholds
- Builds percentage summary and pie chart

### Notebook Environment Note

The notebook includes Colab-specific and KaggleHub-based loading logic. In local Jupyter usage, update data-loading cells to point to local file paths if needed.

## Installation

Create and activate a virtual environment, then install dependencies.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install streamlit pandas numpy matplotlib seaborn opencv-python kagglehub jupyter
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install streamlit pandas numpy matplotlib seaborn opencv-python kagglehub jupyter
```

## Run the Streamlit Dashboard

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`) and upload a CSV file with an `NDVI` column.

## Expected Input Requirements

For the dashboard to work correctly:
- File format must be CSV.
- Dataset must include `NDVI` column.
- Numeric columns are required for meaningful correlation heatmap output.

## Output and Interpretation

The system outputs:
- Health status label per record
- Category percentages (Healthy/Moderate/Unhealthy)
- Visual diagnostics for NDVI and correlations
- Recommendation:
  - If Unhealthy > 30%: immediate action recommended
  - Else: monitoring considered stable

## Known Limitations

- Classification is rule-based and depends only on NDVI thresholds.
- No supervised model training is performed in `app.py`.
- Bilateral filtering is applied to reshaped 1D NDVI values, which is useful for smoothing but is not a full spatial image operation.
- Results quality depends on sensor data quality and feature calibration.

## Suggested Enhancements

- Add model-based classification (e.g., Random Forest/XGBoost) and compare against NDVI rules.
- Add validation metrics if ground-truth classes are available.
- Add geospatial visualization if GPS coordinates are meaningful.
- Add export options for summary reports.

## License

No license file is currently included in this repository. Add a `LICENSE` file if you plan to distribute the project.
