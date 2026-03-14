import yaml
import pandas as pd

INPUT_FILE = "data/raw/ktcourses.yml"
OUTPUT_FILE = "data/processed/kotlin_courses_dataset.csv"

rows = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    universities = yaml.safe_load(f)

for uni in universities:

    institution = uni.get("title", "")
    location = uni.get("location", "")
    country = location.split(",")[-1].strip()

    geo = uni.get("geo", {})
    lat = geo.get("lat", None)
    lng = geo.get("lng", None)

    for course in uni.get("courses", []):

        course_name = course.get("name", "")

        name_lower = course_name.lower()

        if "android" in name_lower:
            category = "Android"
        elif "kotlin" in name_lower:
            category = "Kotlin"
        elif "mobile" in name_lower:
            category = "Mobile Development"
        else:
            category = "Software Engineering"

        rows.append({
            "institution": institution,
            "country": country,
            "course_name": course_name,
            "category": category,
            "platform": "University",
            "source": "https://kotlinlang.org/education/courses/",
            "lat": lat,
            "lng": lng
        })

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_FILE, index=False)

print("Dataset regenerated with coordinates.")