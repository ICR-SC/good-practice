

# Wednesday Session: Python for Reproducible Research (Beginner Edition)
## Live Coding Script for Instructors

*Duration: 60 minutes | Format: Participatory live coding*
*Homework: Build a simple, reproducible analysis pipeline in Python*

---

# Reference
This session builds on principles from [The Turing Way: Code Reuse](https://book.the-turing-way.org/reproducible-research/code-reuse), a guide to making research code transparent, ethical, and reusable.

---

## Pre-Session Setup

**[ASIDE: Open VSCode in your project folder from Monday/Tuesday. Ensure Python is installed and available. Have a terminal ready.]**

---

## Opening & Welcome

### What I Say:
"Welcome! Today we’ll use Python to analyze data in a way that’s reproducible and ethical. We’ll keep things simple and practical, with tips for both beginners and those wanting a refresher."

---

## Part 3.1 (starts at 0 min, takes 10 min): Project Setup & Data Privacy

### What I Say:
"Let's review our project folder structure and talk about data privacy. It's important to keep sensitive data out of version control."

#### What I Show (Live Coding):
```bash
ls
cat .gitignore
```

### What I Say:
"We use a `.gitignore` file to protect sensitive data and keep our code clean. Let's add some common Python exclusions."

#### What I Type (Live Coding):
```bash
echo "__pycache__/\n*.pyc\nenvironment/" >> .gitignore
cat .gitignore
```

---

## Part 3.2 (starts at 10 min, takes 5 min): Setting Up Git in VSCode

### What I Say:
"Now let's make sure our project is tracked with git. VSCode makes this easy."

#### What I Show (Live Coding):
- Open the Source Control panel in VSCode.

#### What I Type (Live Coding):
```bash
git init
git add .
git commit -m "Initial project setup"
git status
```

---

## Part 3.3 (starts at 15 min, takes 5 min): Creating a Python Virtual Environment

### What I Say:
"A virtual environment keeps your project dependencies organized and reproducible. Let's create one."

#### What I Type (Live Coding):
```bash
python3 -m venv environment
source environment/bin/activate
pip install pandas
```

### What I Say:
"Remember to add `environment/` to your `.gitignore` so it doesn't get tracked by git."

---

## Part 3.4 (starts at 20 min, takes 15 min): Writing Simple, Reproducible Python Code

### What I Say:
"Let's write a simple function to load data. Clear function names and documentation help others understand your code."

#### What I Type (Live Coding):
Create `src/python/analysis.py`:
```python
import pandas as pd

        bias_scores = {}
    """Load a CSV file and return a DataFrame."""
    return pd.read_csv(filepath)
```

### What I Say:
"Let's run our function in a Python script or notebook."

#### What I Type (Live Coding):
```python
# In a notebook or script
from src.python.analysis import load_data
df = load_data('data/processed/example.csv')
df.head()
```

---

## Part 3.5 (starts at 35 min, takes 10 min): Basic Testing

### What I Say:
"Testing helps catch mistakes and ensures your code works as expected. Let's write a simple test."

#### What I Type (Live Coding):
Create `tests/test_analysis.py`:
```python
import unittest
from src.python.analysis import load_data

class TestAnalysis(unittest.TestCase):
    def test_load_data(self):
        # Use a small example CSV for testing
        df = load_data('data/processed/example.csv')
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
```

### What I Say:
"Let's run our test."

#### What I Type (Live Coding):
```bash
python tests/test_analysis.py
```

---

## Part 3.6 (starts at 45 min, takes 5 min): Ethical Coding & Documentation

### What I Say:
"Ethical coding means documenting your work and making it reusable. The Turing Way has a great checklist for code reuse. Let's add a README to our analysis folder."

#### What I Type (Live Coding):
```bash
echo "# Analysis Scripts\nThis folder contains Python scripts for data analysis. Each script is documented and tested." > src/python/README.md
cat src/python/README.md
```

---

## Session Wrap-up & Homework (starts at 50 min, takes 5 min)

### What I Say:
"Great work today! You set up your project, protected sensitive data, used git in VSCode, created a virtual environment, wrote and tested simple Python code, and documented your work."

### Homework (Session Consolidation, ~30 min):
- Review today's steps by:
    - Creating a simple Python function for data loading or analysis (use your own or example data)
    - Writing a short test to check your function works
    - Adding a brief README or comments to explain your code
- Spend a few minutes exploring The Turing Way’s code reuse checklist for ideas on making your code more reusable

**See you next session!**