# 🧾 Form Filler Automation with Selenium & Pytest

Automates a full form submission on [DemoQA Practice Form](https://demoqa.com/automation-practice-form) using:

- Selenium WebDriver
- Pytest
- Page Object Model
- Parameterized test data
- Screenshot on failure & confirmation
- Pytest HTML report
- Logging for traceability
- GitHub Actions CI

---

## 📁 Project Structure

```
form_filler_automation/
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions workflow
├── assets/                       # Test assets (images)
├── reports/                      # Pytest HTML reports (.gitkeep included)
├── screenshots/                  # Screenshots on failure/success (.gitkeep included)
├── src/
│   ├── pages/
│   │   ├── form_page.py          # Page Object for form
│   │   └── __init__.py
│   └── utils/
│       ├── test_data.py          # Parameterized test data
│       ├── logger.py             # Centralized logger
│       └── __init__.py
├── tests/
│   ├── test_fill_form.py         # Parametrized form test
│   └── __init__.py
├── .gitignore
├── conftest.py                   # Pytest fixtures and screenshot on failure
├── pytest.ini                    # Pytest default config
├── requirements.txt
└── README.md                     # This file
```

---

## ▶️ Run Tests

### Locally:
```bash
pytest
```

### With HTML Report:
```bash
pytest --html=reports/report.html -s
```

---

## ✅ Key Features

- **Full Form Automation** on demoqa.com
- **Parameterized Testing** with multiple user inputs
- **Screenshot on Failure & Confirmation**
- **HTML Report Generation**
- **Custom Logging** with `logger.py`
- **CI/CD Pipeline** via GitHub Actions
- **Ad Removal** to avoid test interference
- **Page Object Model** design

---

## 🔍 Sample Logs

```
2025-07-10 00:10:00 [INFO] Starting test for: Zach Coleman
✅ Confirmation screenshot saved to: screenshots/confirmation_Zach_Coleman_2025-07-10_00-10-03.png
2025-07-10 00:10:04 [INFO] Test passed for: Zach Coleman
```

---

## 🧪 HTML Report Example

After test execution:
- Find report at `reports/report.html`
- Open in browser to view pass/fail breakdown and captured logs

---

## 🔁 Continuous Integration (CI)

GitHub Actions workflow runs automatically on each push to `main`. View test status in the **Actions** tab.

Includes:
- ✅ Pytest execution
- ✅ HTML report saved as artifact
- ✅ Screenshot upload on failure

---

## 📸 Screenshots

- Stored in `/screenshots/`
- Named using timestamp and test name
- Saved on both failure (automatically) and form submission (confirmation)

---

## 📌 Future Enhancements

- [ ] Negative test cases (e.g., blank fields, invalid email)
- [ ] Browser compatibility testing (Firefox, Edge)
- [ ] Dockerized setup for consistency
- [ ] Parallel test execution with `pytest-xdist`
- [ ] Test data loaded from JSON/CSV
- [ ] Better handling of flaky ad popups

---

## 👨‍💻 Author

**Zach Coleman**  
QA Automation Engineer in Training

---

## 🏁 License

This project is for educational and portfolio purposes. Feel free to fork or clone it for learning and demonstration.

---
