# 🎭 Playwright Automation Demo

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green?style=for-the-badge&logo=playwright&logoColor=white)

## 📌 Project Overview
This repository contains a **comprehensive test automation suite** designed using **Python** and **Playwright**.
The project validates both **Positive (Happy Path)** and **Negative (Error Handling)** scenarios on the [SauceDemo](https://www.saucedemo.com/) e-commerce platform.

## 🧪 Test Scenarios Covered
The script (`main.py`) executes the following test cases:

| ID | Scenario Type | Description | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC01** | 🔴 Negative Testing | Login with invalid credentials | System displays error message |
| **TC02** | 🟢 Positive Testing | Login with valid credentials | User redirected to Inventory page |

## 🚀 Key Features
* **Dual Scenario Execution:** Runs both success and failure paths in a single execution.
* **Error Validation:** Dynamically checks if the correct error message ("Epic sadface...") is displayed.
* **Robust Selectors:** Implements stable CSS selectors for maintainability.
* **Auto-Screenshots:** Captures screenshots automatically if a test fails.
* **Clean Code:** Follows PEP-8 naming conventions with detailed docstrings.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Library:** Playwright (Sync API)
* **Browser Engine:** Chromium

## ⚙️ How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ted1905/Playwright-Python-Demo.git](https://github.com/Ted1905/Playwright-Python-Demo.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install playwright
    playwright install
    ```
3.  **Run the test suite:**
    ```bash
    python main.py
    ```

## soon Future Improvements
* Implement **Page Object Model (POM)** design pattern.
* Migrate to **Pytest** framework for HTML reporting.
* Add **CI/CD** pipeline (GitHub Actions).
