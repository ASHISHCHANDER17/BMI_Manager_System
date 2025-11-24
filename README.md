BMI Manager System

1. Project Overview

A lightweight Python CLI application designed for long-term health tracking. Unlike standard calculators, this system persists data using an SQLite database, allowing users to monitor their Body Mass Index (BMI) trends over time without needing internet access.

2. Features

Core Calculation: Computes BMI (Weight/Height²) with precision.

Auto-Categorization: Classifies results (e.g., Normal, Obese) based on WHO standards.

Data Persistence: Automatically saves records to a local bmi_database.db file.

History Log: Displays a formatted table of all past entries with timestamps.

Error Safety: Prevents crashes from invalid non-numeric inputs.

3. Tech Stack

Language: Python 3.x

Database: SQLite3 (Embedded)

Libraries: sqlite3, datetime

4. Installation & Usage

Run: Open a terminal in the project folder.

python bmi_manager.py


Database: The bmi_database.db file is created automatically on the first run.

5. Testing

Calculate: Enter 70 (kg) and 175 (cm). Result should be ~22.86 (Normal).

Save: Choose "Yes" to save. Restart app to verify data persistence.

History: Select "View History" to see the saved record table.

Validation: Enter text (e.g., "abc") as weight; ensure the app catches the error.