import requirments.txt

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="🌾 Crop Health Monitoring System",
    page_icon="🌾",
    layout="wide"
)

# ---------------- CONFIG ---------------- #
NDVI_LOW = 0.2
NDVI_HIGH = 0.5

# ---------------- TITLE ---------------- #
st.title("🌾 Crop Health Monitoring System")
st.markdown(
    """
    This dashboard analyzes crop health using **NDVI (Normalized Difference Vegetation Index)**  
    and classifies crop regions into **Healthy, Moderate, and Unhealthy** categories.
    """
)

st.divider()

# ---------------- FILE UPLOAD ---------------- #
st.subheader("📂 Upload Crop Health Dataset")
st.caption("Upload the CSV dataset containing NDVI and crop health related parameters.")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # ---------------- LOAD DATA ---------------- #
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully ✅")

    st.subheader("1️⃣ Dataset Preview")
    st.caption("Displays the first 5 rows of the uploaded dataset.")
    st.dataframe(df.head())

    st.divider()

    # ---------------- COLUMN CHECK ---------------- #
    st.subheader("2️⃣ Dataset Information")
    st.caption("Shows dataset size and available columns.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.write("### Available Columns")
    st.write(list(df.columns))

    st.divider()

    # ---------------- NDVI CHECK ---------------- #
    if "NDVI" not in df.columns:
        st.error("❌ NDVI column not found in dataset.")
        st.stop()

    # ---------------- MISSING VALUES ---------------- #
    st.subheader("3️⃣ Missing Value Analysis")
    st.caption("Checks for null values before processing.")

    missing_values = df.isnull().sum()
    st.dataframe(missing_values)

    st.divider()

    # ---------------- HEATMAP ---------------- #
    st.subheader("4️⃣ Correlation Heatmap")
    st.caption(
        "Shows relationships between crop health features like NDVI, temperature, soil moisture, etc."
    )

    numeric_df = df.select_dtypes(include=np.number)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=False, cmap="viridis", ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    st.pyplot(fig)

    st.divider()

    # ---------------- NDVI DISTRIBUTION ---------------- #
    st.subheader("5️⃣ NDVI Distribution")
    st.caption(
        "NDVI helps measure vegetation health. Higher NDVI indicates healthier crops."
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["NDVI"], bins=30)
    ax.set_title("NDVI Distribution")
    ax.set_xlabel("NDVI Value")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    st.divider()

    # ---------------- BILATERAL FILTER ---------------- #
    st.subheader("6️⃣ Bilateral Filtering")
    st.caption(
        "Reduces noise while preserving important boundaries in NDVI values."
    )

    ndvi_array = df["NDVI"].values.astype(np.float32)
    ndvi_img = ndvi_array.reshape(-1, 1)

    import cv2
    filtered_ndvi = cv2.bilateralFilter(ndvi_img, 9, 75, 75)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(ndvi_array[:200], label="Original NDVI")
    ax.plot(filtered_ndvi[:200], label="Filtered NDVI")
    ax.set_title("Bilateral Filter on NDVI")
    ax.legend()
    st.pyplot(fig)

    st.divider()

    # ---------------- CLASSIFICATION ---------------- #
    st.subheader("7️⃣ Crop Health Classification")
    st.caption(
        "Classifies crop regions based on NDVI values."
    )

    df["Health_Status"] = "Moderate"

    df.loc[df["NDVI"] < NDVI_LOW, "Health_Status"] = "Unhealthy"
    df.loc[df["NDVI"] >= NDVI_HIGH, "Health_Status"] = "Healthy"

    st.dataframe(df[["NDVI", "Health_Status"]].head(15))

    st.info(
        """
        Classification Rules:
        - NDVI < 0.2 → Unhealthy
        - 0.2 to 0.5 → Moderate
        - NDVI > 0.5 → Healthy
        """
    )

    st.divider()

    # ---------------- PERCENTAGE ANALYSIS ---------------- #
    st.subheader("8️⃣ Percentage Analysis")
    st.caption(
        "Calculates the percentage of Healthy, Moderate, and Unhealthy crop regions."
    )

    result = df["Health_Status"].value_counts(normalize=True) * 100

    for label, value in result.items():
        st.metric(label, f"{value:.2f}%")

    st.divider()

    # ---------------- SUMMARY TABLE ---------------- #
    st.subheader("9️⃣ Summary Table")
    st.caption(
        "Final summary of crop health categories for reporting and printout."
    )

    summary = pd.DataFrame({
        "Health Category": result.index,
        "Percentage (%)": result.values
    })

    st.dataframe(summary)

    st.divider()

    # ---------------- PIE CHART ---------------- #
    st.subheader("🔟 Crop Health Distribution")
    st.caption(
        "Pie chart showing final crop health distribution."
    )

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        result.values,
        labels=result.index,
        autopct="%1.1f%%"
    )
    ax.set_title("Crop Health Distribution")
    st.pyplot(fig)

    st.divider()

    # ---------------- FINAL RECOMMENDATION ---------------- #
    st.subheader("📌 Final Recommendation")

    unhealthy_percent = result.get("Unhealthy", 0)

    if unhealthy_percent > 30:
        st.error(
            "⚠ High unhealthy crop percentage detected. Immediate irrigation and soil inspection recommended."
        )
    else:
        st.success(
            "✅ Crop health is stable. Regular monitoring is sufficient."
        )

    st.divider()

    # ---------------- CONCLUSION ---------------- #
    st.subheader("📘 Conclusion")
    st.write(
        """
        This system uses NDVI analysis, bilateral filtering, and classification
        to monitor crop health efficiently.

        It helps identify unhealthy crop regions early and supports
        precision agriculture and smart farming decisions.
        """
    )

else:
    st.info("Please upload a CSV dataset to begin analysis 🌾")
