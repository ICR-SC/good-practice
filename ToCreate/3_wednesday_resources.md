# Wednesday Resources: Python for Reproducible Research

## Key References

- **The Turing Way: Code Reuse Guide:**
  https://book.the-turing-way.org/reproducible-research/code-reuse
  - Practical tips for making research code transparent, ethical, and reusable.

- **VSCode Documentation:**
  https://code.visualstudio.com/docs
  - Getting started, integrated terminal, extensions, and project setup.

- **Python Virtual Environments:**
  https://docs.python.org/3/tutorial/venv.html
  - How to create and use virtual environments for reproducibility.

- **Python unittest Documentation:**
  https://docs.python.org/3/library/unittest.html
  - Writing and running basic tests for your code.

## Example Commands Used in Session

```bash
# Create and activate a virtual environment
python3 -m venv environment
source environment/bin/activate

# Install a package
pip install pandas

# Initialize git and make a commit
git init
git add .
git commit -m "Initial project setup"

# Add Python exclusions to .gitignore
echo "__pycache__/\n*.pyc\nenvironment/" >> .gitignore

# Run a test
python tests/test_analysis.py
```

## Additional Reading

- **Why Reproducibility Matters:**
  https://www.nature.com/articles/d41586-019-00067-3

- **Best Practices for Research Code:**
  https://www.turing.ac.uk/research/research-projects/best-practices-collaborative-coding

---

*This resource list supports the Wednesday session and provides links for further exploration and practice.*
