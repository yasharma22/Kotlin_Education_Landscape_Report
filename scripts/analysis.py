import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


 
# Configuration
DATA_PATH = "data/processed/kotlin_courses_dataset.csv"
VISUALS_DIR = "visuals"

os.makedirs(VISUALS_DIR, exist_ok=True)


 
# Load Dataset
df = pd.read_csv(DATA_PATH)
print("\nDataset Loaded Successfully\n")
print("Total courses:", len(df))
print("Total institutions:", df["institution"].nunique())
print("Countries covered:", df["country"].nunique())



# Country Distribution
plt.figure(figsize=(10,6))
country_counts = df["country"].value_counts().head(10)
sns.barplot(
    x=country_counts.values,
    y=country_counts.index
)
plt.title("Top Countries Teaching Kotlin")
plt.xlabel("Number of Courses")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(f"{VISUALS_DIR}/country_distribution.png")
plt.close()



# Category Distribution
plt.figure(figsize=(8,8))
category_counts = df["category"].value_counts()
plt.pie(
    category_counts,
    labels=category_counts.index,
    autopct="%1.1f%%"
)
plt.title("Kotlin Course Categories")
plt.tight_layout()
plt.savefig(f"{VISUALS_DIR}/category_distribution.png")
plt.close()


 
# Platform Distribution
plt.figure(figsize=(8,6))
platform_counts = df["platform"].value_counts()
sns.barplot(
    x=platform_counts.index,
    y=platform_counts.values
)
plt.title("Platform Distribution of Kotlin Courses")
plt.xlabel("Platform")
plt.ylabel("Number of Courses")
plt.tight_layout()
plt.savefig(f"{VISUALS_DIR}/platform_distribution.png")
plt.close()

 

# Top Institutions
plt.figure(figsize=(10,6))
top_institutions = df["institution"].value_counts().head(10)
sns.barplot(
    x=top_institutions.values,
    y=top_institutions.index
)
plt.title("Top Institutions Offering Kotlin Courses")
plt.xlabel("Number of Courses")
plt.ylabel("Institution")
plt.tight_layout()
plt.savefig(f"{VISUALS_DIR}/top_institutions.png")
plt.close()
print("\nVisualizations generated successfully!")
print("Check the 'visuals/' folder.\n")