# Kotlin Education Landscape Report (GSoC 2026)

This project analyzes how **Kotlin is taught across universities and online learning platforms worldwide**.  
The goal is to understand the **global adoption of Kotlin in computer science education**.

---

# Project Goals

- Identify institutions teaching Kotlin
- Categorize Kotlin-related courses (Android, Kotlin programming, mobile development, etc.)
- Analyze global adoption trends of Kotlin education
- Create a clean dataset for further research and analysis
- Visualize Kotlin education distribution globally

---

# Data Sources

The dataset was collected from:

- Kotlin Official Education Page  
  https://kotlinlang.org/education/courses/

- Online learning platforms (MOOCs)

The dataset includes:

- University courses
- Online courses
- Bootcamps

---

# Dataset Structure

The final dataset contains the following fields:

```
institution
country
course_name
category
platform
source
lat
lng
```

Example entry:

```
Harvard University,US,CS50x Introduction to Computer Science,Software Engineering,University,https://kotlinlang.org/education/courses/,42.3576808,-71.1288621
```

---

# Repository Structure

```
kotlin-education-analysis
│
├ README.md
├ requirements.txt
│
├ data
│   ├ raw
│   │   └ ktcourses.yml
│   │
│   └ processed
│       └ kotlin_courses_dataset.csv
│
├ scripts
│   ├ convert_yaml_to_csv.py
│   ├ merge_datasets.py
│   ├ analysis.py
│   └ kotlin_world_map.py
│
├ visuals
│   ├ country_distribution.png
│   ├ category_distribution.png
│   ├ platform_distribution.png
│   ├ top_institutions.png
│   └ kotlin_world_map.html
│
└ docs
```

---

# Data Analysis

The project generates several visual insights including:

## Country Distribution
Shows countries with the highest number of Kotlin-related courses.

## Category Distribution
Breakdown of courses by category:
- Android Development
- Kotlin Programming
- Mobile Development
- Software Engineering

## Platform Distribution
Comparison between:
- Universities
- MOOCs
- Bootcamps

## Top Institutions
Universities offering the highest number of Kotlin-related courses.

---

# Global Kotlin Education Map

An interactive world map visualizes institutions offering Kotlin courses.

Open the map:

```
visuals/kotlin_world_map.html
```

Each marker represents a university or institution offering Kotlin-related courses.

---

# How to Reproduce the Analysis

Install dependencies:

```
pip install -r requirements.txt
```

Run data analysis:

```
python scripts/analysis.py
```

Generate the global map:

```
python scripts/kotlin_world_map.py
```

---

# Key Findings

Preliminary observations from the dataset:

- Kotlin education is concentrated in **North America and Europe**
- Many Kotlin courses focus on **Android development**
- Universities provide the majority of Kotlin education
- Kotlin is often integrated into **mobile development and programming language courses**

---

# Future Work

Possible extensions of this project include:

- Studying Kotlin adoption trends over time
- Comparing Kotlin education with Java education
- Expanding the dataset with more training programs and bootcamps

---

# License

This dataset and analysis are intended for **educational and research purposes**.

# Data Source

Some data used in this project was collected from the Kotlin
official education page:

https://kotlinlang.org/education/courses/

This project analyzes publicly available information and is
not affiliated with JetBrains or the Kotlin Foundation.