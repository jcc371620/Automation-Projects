# 🧪 Test Automation Framework

A scalable automation testing framework built with **Python + Pytest + Requests + Playwright + SQL**.

---

## 🚀 Overview

This project is a full-stack automation testing framework that covers:

- API Testing
* UI Automation Testing
* Database Validation
* Test Reporting
* CI/CD Integration

It is designed based on real-world enterprise testing architecture.

---

## 目录（Table of Contents）
- [简介](#简介)
- [功能](#功能)
- [项目架构](#项目架构)
- [安装](#安装)
- [使用方法](#使用方法)
- [示例](#示例)
- [技术栈](#技术栈)
- [贡献](#贡献)
- [许可](#许可)
- [联系方式](#联系方式)

---

## 🧱 Tech Stack

* Python
* Pytest
* Requests
* Playwright
* SQL (MySQL / PostgreSQL)
* Allure Report

---

## 📂 Project Structure

<!-- TREE_START -->
```markdown
├─ README.md                # 项目总说明 | 8188 bytes | 2026-03-17 15:34
├─ api                      # API 接口模块 | 目录
│   ├─ README.md            # 11 bytes | 2026-03-17 14:33
│   ├─ login_api.py         # 0 bytes | 2026-03-17 14:33
│   ├─ test.py              # 0 bytes | 2026-03-16 21:46
│   └─ user_api.py          # 0 bytes | 2026-03-17 14:33
├─ config                   # 配置文件目录 | 目录
│   ├─ README.md            # 14 bytes | 2026-03-17 14:31
│   ├─ config.yaml          # 0 bytes | 2026-03-17 14:31
│   ├─ env.yaml             # 0 bytes | 2026-03-17 14:31
│   └─ test.py              # 0 bytes | 2026-03-17 14:24
├─ data                     # 测试数据目录 | 目录
│   ├─ README.md            # 14 bytes | 2026-03-17 14:31
│   ├─ login.json           # 0 bytes | 2026-03-17 14:31
│   ├─ test.py              # 0 bytes | 2026-03-17 14:24
│   └─ users.json           # 0 bytes | 2026-03-17 14:32
├─ generate_ASCII_tree.py   # 生成树状结构脚本并插入到README.md | 6645 bytes | 2026-03-17 15:35
├─ pages                    # 页面对象模块 | 目录
│   ├─ README.md            # 16 bytes | 2026-03-17 14:33
│   ├─ dashboard_page.py    # 0 bytes | 2026-03-17 14:33
│   ├─ login_page.py        # 0 bytes | 2026-03-17 14:33
│   └─ test.py              # 0 bytes | 2026-03-17 14:24
├─ pytest.ini               # Pytest 配置文件 | 0 bytes | 2026-03-17 14:39
├─ reports                  # 测试报告目录 | 目录
│   ├─ README.md            # 14 bytes | 2026-03-17 14:38
│   └─ test.py              # 0 bytes | 2026-03-17 14:24
├─ requirements.txt         # 依赖列表 | 0 bytes | 2026-03-17 14:39
├─ tests                    # 测试用例目录 | 目录
│   ├─ README.md            # 11 bytes | 2026-03-17 14:34
│   ├─ api_validation       # 目录
│   │   ├─ README.md        # 0 bytes | 2026-03-16 21:47
│   │   └─ test.py          # 0 bytes | 2026-03-16 21:46
│   ├─ database_validation  # 目录
│   │   ├─ README.md        # 0 bytes | 2026-03-16 21:48
│   │   └─ test.py          # 0 bytes | 2026-03-17 14:24
│   └─ ui_validation        # 目录
│       ├─ README.md        # 0 bytes | 2026-03-16 21:48
│       └─ test.py          # 0 bytes | 2026-03-16 21:47
└─ utils                    # 工具函数目录 | 目录
    ├─ README.md            # 11 bytes | 2026-03-17 14:32
    ├─ config_util.py       # 0 bytes | 2026-03-17 14:32
    ├─ db_util.py           # 0 bytes | 2026-03-17 14:32
    ├─ logger.py            # 0 bytes | 2026-03-17 14:32
    ├─ request_util.py      # 0 bytes | 2026-03-17 14:32
    └─ test.py              # 0 bytes | 2026-03-17 14:24
```
<!-- TREE_END -->

---

## ⚙️ Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/test-framework.git
cd test-framework
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```
playwright install
```

---

## ▶️ Run Tests

Run all tests:

```
pytest
```

Run specific test:

```
pytest tests/api_tests/test_login.py
```

---

## 📊 Generate Report (Allure)

```
pytest --alluredir=reports
allure serve reports
```

---

## 🧪 Example Test Cases

### API Test

* Login API validation
* Response status check
* JSON data validation

### UI Test

* Login page automation
* Form submission
* Navigation validation

### DB Test

* Verify user creation in database
* Validate data consistency

---

## 🔄 CI/CD Integration

This framework can be integrated with:

* Jenkins
* GitHub Actions
* GitLab CI

Pipeline flow:

```
Code Push → Run Tests → Generate Report → Notify Results
```

---

## 📌 Features

* Modular design
* Reusable components
* Data-driven testing
* Cross-browser UI testing
* Easy integration with CI/CD

---

## 📈 Future Improvements

* Docker support
* Parallel test execution
* Test data management system
* API mocking

---

## 👤 Author

陈诗洁 | Jessy Chen

---

## ⭐️ Tips

* Follow naming conventions (lowercase folders)
* Keep tests independent
* Use fixtures for setup/teardown
* Separate test data from code

---
