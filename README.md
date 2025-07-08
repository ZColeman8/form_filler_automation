# 🧾 Selenium Form Filler Automation

This project automates form submission on [DemoQA's Practice Form](https://demoqa.com/automation-practice-form) using Selenium WebDriver with Pytest and Python.

## ✅ Features

- Full form automation (text fields, gender, hobbies, state/city, etc.)
- Test parameterization for multiple users
- Page Object Model (POM) design pattern
- Screenshots on failure and successful confirmation
- Logging using Python’s `logging` module
- HTML reporting via `pytest-html`
- Auto WebDriver management via `webdriver-manager`
- Ad-block workaround using JavaScript injection

## 🧪 Technologies

- Python 3.11+
- Selenium 4.x
- Pytest
- Webdriver-Manager
- Pytest-HTML

## 📁 Project Structure

```
form_filler_automation/
├── assets/
│   └── image1.JPG
├── reports/
├── logs/
    └── form_test.log
├── screenshots/
├── src/
│   ├── pages/
│   │   └── form_page.py
│   └── utils/
│       ├── logger.py
│       └── test_data.py
├── tests/
│   └── test_fill_form.py
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## ▶️ Run Tests

```bash
pytest --html=reports/report.html -s
```

## 📸 Screenshots

- On **failure**, saved in `screenshots/`
- On **success**, confirmation screenshot also saved

## 🔧 Future Enhancements

- Add negative test scenarios (e.g., missing data)
- Use Faker to generate randomized data
- CI integration (GitHub Actions, Jenkins)
- Capture dynamic form states
- Export submission data to reports

## 👨‍💻 Author

Zach Coleman  
QA Automation Engineer in Training

## 🪪 License

This project is for educational and portfolio use.
