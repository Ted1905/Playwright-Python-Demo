# 🎭 Playwright Automation Framework (Python & POM)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-yellow?style=for-the-badge&logo=pytest&logoColor=white)

This repository demonstrates a **robust, scalable, and modular** test automation framework built using **Python** and **Playwright**. It implements the **Page Object Model (POM)** design pattern to ensure code reusability and maintainability.

The project tests the [SauceDemo](https://www.saucedemo.com/) e-commerce website, covering login scenarios, inventory validation, and error handling.

---

## 🏗️ Project Structure

The project follows a strict **Page Object Model (POM)** architecture:

```text
Playwright-Python-Demo/
├── pages/                 # 📂 Page Objects (UI Logic)
│   ├── base_page.py       # Base methods (Click, Fill, Navigate)
│   ├── login_page.py      # Login page specific selectors & actions
│   └── inventory_page.py  # Inventory page verification
├── tests/                 # 🧪 Test Scenarios
│   ├── conftest.py        # Pytest Fixtures (Browser setup/teardown)
│   └── test_login.py      # Login test cases (Positive & Negative)
├── pytest.ini             # ⚙️ Configuration for reporting
├── README.md              # 📄 Project documentation
└── .gitignore             # 🙈 Git ignore file

```

---

## 🚀 Key Features

* **Page Object Model (POM):** UI logic is separated from test logic.
* **Pytest Fixtures:** Efficient browser lifecycle management in `conftest.py`.
* **HTML Reporting:** Automatically generates detailed test reports.
* **Cross-Browser Support:** Ready for Chromium, Firefox, and WebKit.
* **Headless Mode:** Configurable for CI/CD pipelines.

---

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone [https://github.com/Ted1905/Playwright-Python-Demo.git](https://github.com/Ted1905/Playwright-Python-Demo.git)
cd Playwright-Python-Demo

```


2. **Install dependencies:**
```bash
pip install pytest-playwright pytest-html
playwright install

```



---

## ▶️ How to Run Tests

Since the project uses **Pytest**, you don't need to run a python file directly. Just use the following command:

### Run all tests

```bash
pytest

```

### Run with HTML Report

```bash
pytest --html=report.html

```

### Run in Headless Mode (No UI)

To run without opening the browser, edit `tests/conftest.py` and set `headless=True`, then run `pytest`.

---

## 📊 Test Scenarios Covered

| ID | Scenario | Description | Expected Result |
| --- | --- | --- | --- |
| **TC01** | ✅ Valid Login | Login with standard user | Redirect to Inventory Page |
| **TC02** | ❌ Invalid Password | Login with wrong password | Error: "Username and password do not match" |
| **TC03** | 🔒 Locked User | Login with locked-out user | Error: "Sorry, this user has been locked out" |

---

## 👨‍💻 Author

**Mehmet Taskin**

* **Role:** QA Automation Engineer
* **Tech Stack:** Python, Playwright, C++, CI/CD
