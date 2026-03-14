import pandas as pd
import folium
import os

# -----------------------------
# Configuration
# -----------------------------

DATA_PATH = "data/processed/kotlin_courses_dataset.csv"
OUTPUT_MAP = "visuals/kotlin_world_map.html"

# create visuals folder if not exists
os.makedirs("visuals", exist_ok=True)

# -----------------------------
# Load dataset
# -----------------------------

df = pd.read_csv(DATA_PATH)

print("Dataset loaded")
print("Total rows:", len(df))

# -----------------------------
# Remove rows without coordinates
# -----------------------------

df = df.dropna(subset=["lat", "lng"])

print("Rows with coordinates:", len(df))

# -----------------------------
# Create world map
# -----------------------------

world_map = folium.Map(
    location=[20, 0],
    zoom_start=2,
    tiles="cartodbpositron"
)

# -----------------------------
# Add markers
# -----------------------------

for _, row in df.iterrows():

    popup_text = f"""
    <b>{row['institution']}</b><br>
    {row['course_name']}<br>
    {row['country']}
    """

    folium.CircleMarker(
        location=[row["lat"], row["lng"]],
        radius=5,
        popup=popup_text,
        color="blue",
        fill=True,
        fill_opacity=0.7
    ).add_to(world_map)

# -----------------------------
# Save map
# -----------------------------

world_map.save(OUTPUT_MAP)

print("World map created successfully!")
print("File saved at:", OUTPUT_MAP)