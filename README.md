# Student Analyzer

A Python-based tool designed to analyze and visualize student academic performance from CSV data. This is my final project for the Introductory Python course.

## Features
- **Data Loading:** Automatically reads student metrics from `students.csv`.
- **Performance Metrics:** Calculates average scores across multiple subjects (Math, Science).
- **Automated Insights:** - Identifies the top-performing student.
  - Detects students requiring additional support (Average < 60).
  - Categorizes overall class performance (Low, Moderate, Excellent).
- **Visualization:** Generates a bar chart showing score distributions using `matplotlib`.

## Installation
Ensure you have `uv` installed, then run:
```bash
uv pip install -e .