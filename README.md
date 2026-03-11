# 🧮 Python Calculator with CI/CD Pipeline

A simple Python calculator project built to practice CI/CD with GitHub Actions.

---

## 📁 Project Structure

```
python-calculator/
│
├── calculator.py            ← Main calculator code
├── test_calculator.py       ← All the tests
├── requirements.txt         ← Python packages needed
└── .github/
    └── workflows/
        └── ci-cd.yml        ← CI/CD Pipeline
```

---

## ⚙️ CI/CD Pipeline

Every time you push code, the pipeline automatically:

1. ✅ **Runs all tests** (on Python 3.10, 3.11, 3.12)
2. ✅ **Checks code quality** with flake8
3. ✅ **Builds and verifies** the app works

---

## 🚀 How to Run Locally

### Run the calculator:
```bash
python calculator.py
```

### Run the tests:
```bash
pip install -r requirements.txt
pytest test_calculator.py -v
```

---

## 🧪 What's Tested

| Function | Tests |
|----------|-------|
| `add()` | positive, negative, zero, decimals |
| `subtract()` | basic, negative result, zero |
| `multiply()` | positive, zero, negative |
| `divide()` | basic, decimals, divide by zero error |

---

## 📊 Pipeline Status

Check the **Actions** tab in GitHub to see pipeline results!