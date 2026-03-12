import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "dataset", "kotlin_courses.csv")

data = pd.read_csv(file_path)

print("Total entries:", len(data))

print("\nCourses by platform:")
print(data["platform"].value_counts())

# create charts folder
charts_dir = os.path.join(base_dir, "analysis", "charts")
os.makedirs(charts_dir, exist_ok=True)

# platform chart
data["platform"].value_counts().plot(kind="bar")

plt.title("Kotlin Education Resources by Platform")
plt.xlabel("Platform")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig(os.path.join(charts_dir, "platform_distribution.png"))
plt.close()