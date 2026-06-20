# 🎬 IMDb Search Automation & Validation Framework

A robust, data-driven UI Automation framework built to validate the functionality and data integrity of IMDb's Advanced Search features. 

This project demonstrates core SDET (Software Development Engineer in Test) principles, including the Page Object Model (POM) design pattern, dynamic waits, and handling complex UI behaviors like lazy loading and element interception.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Automation Tool:** Selenium WebDriver
* **Test Framework:** PyTest
* **Design Pattern:** Page Object Model (POM)

## 🚀 Key Features & Automation Challenges Solved
* **Page Object Model (POM):** Complete separation of UI locators/actions from the test logic for easy maintenance.
* **Complex DOM Handling:** Engineered solutions to bypass `ElementClickInterceptedException` using JavaScript Executors.
* **Lazy Loading Bypass:** Implemented automated vertical scrolling to dynamically load hidden DOM elements (e.g., IMDb Ratings accordion) before interaction.
* **Explicit Waits (WebDriverWait):** Eliminated flaky tests by utilizing strict synchronization (waiting for URLs to change and specific elements to render) instead of hardcoded sleeps.
* **Text Assertion:** Reliable verification logic to ensure the expected movie data is displayed on the results screen based on applied filters.

## 📂 Project Architecture

```text
imdb_qa_project/
│
├── pages/                  
│   └── imdb_search_page.py  # Contains all locators and Web UI action methods
│
├── tests/                  
│   └── test_movies.py       # Contains PyTest assertions and test scenarios
│
├── conftest.py              # PyTest fixtures for WebDriver setup and teardown
├── .gitignore               # Git ignore file for cache and environments
└── README.md                # Project documentation
