# 🎭 Playwright Automation Demo

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green?style=for-the-badge&logo=playwright&logoColor=white)

## 📌 Project Overview
This repository demonstrates a **test automation script** designed using **Python** and **Playwright**.
The project focuses on modern web automation techniques, ensuring reliability and speed in UI testing.

The target application for this demo is [SauceDemo](https://www.saucedemo.com/), a standard e-commerce practice site.

## 🚀 Key Features
* **Browser Automation:** Uses Playwright's Sync API for fast and reliable execution.
* **Robust Selectors:** Implements stable CSS selectors for maintainability.
* **Assertions:** Validates successful login via URL verification.
* **Error Handling:** Includes `try-except` blocks and automatic screenshot capture on failure (`login_error.png`).
* **Clean Code:** Follows PEP-8 naming conventions and includes detailed docstrings.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Library:** Playwright
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
3.  **Run the test:**
    ```bash
    python main.py
    ```

## 🔜 Future Improvements
* Implement **Page Object Model (POM)** design pattern.
* Integrate **Pytest** for advanced reporting.
* Add **CI/CD** pipeline (GitHub Actions) for automated testing.
