# 🛴 Yandex Scooter UI & API Tests

Automated test suite for [Yandex Scooter](https://qa-scooter.praktikum-services.ru/) service

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pytest](https://img.shields.io/badge/Pytest-7.4%2B-orange)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-yellowgreen)
![Allure](https://img.shields.io/badge/Allure_Report-supported-ff69b4)

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Chrome/Firefox browser

### Installation
```bash
pip install -r requirements.txt
Run Tests
bash
pytest tests/ --alluredir=allure_results
View Report
bash
allure serve allure_results

