Project Statement: BMI Manager System

1. Problem Statement

In the current digital health landscape, most Body Mass Index (BMI) calculators available online are "stateless" tools. They perform a single calculation and discard the data immediately. This forces users who wish to monitor their weight trends over weeks or months to manually record their results in separate notebooks or spreadsheets, a process that is tedious and prone to data loss. There is a distinct lack of simple, offline-capable tools that not only calculate health metrics but also persist the data automatically for future reference.

2. Scope of the Project

The BMI Manager System is a desktop-based Command Line Interface (CLI) application designed to solve this data persistence issue.

Domain: Personal Health Informatics.

Tech Scope: The project utilizes Python for logic processing and SQLite for relational database management.

Boundaries: The system is designed for single-machine usage (local storage) and focuses specifically on BMI (Weight/Height ratio) rather than comprehensive medical diagnostics.

3. Target Users

Health-Conscious Individuals: People actively trying to gain, lose, or maintain weight who need to track progress over time.

Medical Patients: Individuals advised by doctors to monitor their BMI regularly due to conditions like obesity or underweight issues.

Fitness Enthusiasts: Users who prefer lightweight, terminal-based tools over complex mobile apps with ads or paywalls.

4. High-Level Features

BMI Computation Engine: Accurately calculates BMI using the metric system (Weight in kg / Height in meters squared).

Health Categorization: Automatically classifies the calculated BMI into standard WHO categories (Underweight, Normal Weight, Overweight, Obese) to provide immediate context to the raw number.

Persistent History Logging: Saves every calculation transaction into a secure, local SQL database with a timestamp.

Historical Data Retrieval: Allows the user to view a formatted, chronological table of all past entries to visualize their health journey.