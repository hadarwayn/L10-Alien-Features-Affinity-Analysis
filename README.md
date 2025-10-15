# Alien Features Affinity Analysis Tool v2.0

This project generates a synthetic dataset of alien characteristics and performs an Affinity Analysis to discover significant relationships between those characteristics. The entire analysis is built from scratch using only the NumPy library.

## Project Goals

* **Interactive Dataset Generation**: Create a binary dataset of alien features where the dimensions (number of aliens and number of features) are configurable by the user.
* **From-Scratch Analysis**: Implement the core metrics of Affinity Analysis (Support, Confidence, and Lift) without relying on pre-built machine learning libraries to understand the underlying algorithms.
* **Guaranteed Results**: Ensure that the randomly generated data will always produce at least one meaningful association rule that meets the specified criteria (Support ≥ 30%, Confidence ≥ 70%).
* **Clear & Actionable Insights**: Present the discovered rules in a clean, tabular format, sorted to highlight the most statistically significant relationships.

## Files in this Project

* `alien_analysis_v2.py`: The main Python script that runs the entire analysis.
* `prd_aliens_affinity_v2.md`: The Product Requirements Document outlining the project's features and constraints.
* `tasks_v2.json`: A JSON file describing the development tasks for this project.
* `README.md`: This file.

## Installation and Setup

This project is designed to be simple to run. The only prerequisite is Python 3 and the NumPy library.

1.  **Prerequisites**: Ensure you have Python 3 installed.
2.  **Install NumPy**: If you do not have NumPy installed, open your terminal and run:
    ```bash
    pip install numpy
    ```
3.  **Place Files**: Place all the project files (`alien_analysis_v2.py`, etc.) into a single directory.

## How to Run

1.  Navigate to the project directory in your terminal.
2.  Run the script using the Python 3 interpreter:
    ```bash
    python3 alien_analysis_v2.py
    ```
3.  The script will prompt you to enter the number of records (aliens) and features. You can either:
    * Enter a number and press `Enter`.
    * Simply press `Enter` to accept the default values (5000 records, 6 features).
4.  The script will then run. If the first randomly generated dataset doesn't produce a valid rule, it will automatically try again until it succeeds, printing its progress.

## Understanding the Results

The script outputs two tables:

1.  **Filtered Rules**: This is the main result, showing only the rules that are strong enough to meet both the Support (>30%) and Confidence (>70%) thresholds.
2.  **All combinations from popular itemsets**: This is a longer reference list. It shows *all* the rules that were generated from feature groups that passed the Support threshold, even if their Confidence was too low.

### Key Metrics
* **Support (%)**: How often the features in the rule appear together in the entire dataset. A high support means the combination is common.
* **Confidence (%)**: How often the rule is correct. A 75% confidence in `A -> B` means that 75% of the time that feature `A` is present, feature `B` is also present.
* **Lift**: The most important measure of a rule's significance.
    * **Lift > 1**: The features appear together *more often* than expected by chance. This indicates a positive correlation.
    * **Lift = 1**: The features are independent. There is no correlation.
    * **Lift < 1**: The features appear together *less often* than expected. This indicates a negative correlation (the presence of one makes the other less likely).
