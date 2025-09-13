# Wednesday Overview: Python for Reproducible Research

**Goal:**  
Learn how to set up a reproducible research project in Python, manage your code and data responsibly, and build a simple, tested analysis pipeline.

---

### What We Cover

- **Project Setup & Data Privacy:**  
  - Reviewed a sensible folder structure for research projects.
  - Discussed the importance of `.gitignore` to keep sensitive or unnecessary files (like raw data and environment folders) out of version control.

- **Version Control with Git & VSCode:**  
  - Used Git (with VSCode or command line) to track project changes and collaborate safely.

- **Python Virtual Environments:**  
  - Created a virtual environment to manage project-specific Python packages, ensuring reproducibility.

- **Downloading and Preparing Data:**  
  - Downloaded a real-world dataset from cBioPortal.
  - Used bash commands to organize and extract data into the project.

- **Building a Simple Python Pipeline:**  
  - Wrote clear, well-documented Python functions to:
    - Load tabular data
    - Clean/filter relevant columns
    - Save processed data
    - Analyze and plot the top 10 mutated genes
  - Saved results and plots to the appropriate folders.

- **Testing Your Code:**  
  - Wrote a basic test (using pytest) to check that the pipeline runs end-to-end and produces expected outputs.
  - Discussed the value of both unit and smoke tests for research code.

- **Ethical Coding & Documentation:**  
  - Emphasized the importance of documentation and code reuse.
  - Added a README to the analysis folder to explain what each script does.

---

### Key Takeaways

- Organize your project folders and use `.gitignore` to protect sensitive data.
- Use version control (Git) for all your code and documentation.
- Always use a virtual environment for Python projects.
- Write modular, well-documented code for each step of your analysis.
- Test your code to catch errors early and ensure reproducibility.
- Document your scripts and results for yourself and others.

---

## Videos of session

Link to video [Good Practice-Session 03 Part 01](https://youtu.be/pgwfC7wSRls)- 21.19  
Link to video [Good Practice-Session 03 Part 02](https://youtu.be/R7VAxLVDsv0)- 15.06  
Link to video [Good Practice-Session 03 Part 03](https://youtu.be/-PgKyz9yLwY)- 19.43  

---

**Homework:**  
- Practice writing a simple Python function for data loading or analysis.
- Write a short test to check your function works.
- Add a brief README or comments to explain your code.
- Explore The Turing Way’s code reuse checklist for more ideas.

---

## Session Cheat Sheet: Wednesday

### Bash/Terminal Commands

```bash
# List files and check .gitignore
ls
cat .gitignore

# Add common Python exclusions to .gitignore
echo "__pycache__/\n*.pyc\nenvironment/" >> .gitignore
cat .gitignore

# Create folders for Python code and tests
mkdir -p src/python tests/python
ls

# Check git status
git status

# Create and activate a Python virtual environment
python3 -m venv environment
source environment/bin/activate

# Install required Python packages
pip install pandas pytest matplotlib
pip freeze > environment/requirements.txt

# Download and extract a dataset from cBioPortal
mkdir -p data/raw
wget -O data/raw/aml_tcga_gdc.tar.gz https://cbioportal-datahub.s3.amazonaws.com/aml_tcga_gdc.tar.gz
tar -xzvf data/raw/aml_tcga_gdc.tar.gz -C data/raw

# Run your analysis script
python src/python/analysis.py

# Run your tests
pytest
```

---

### Python Code Snippets

#### src/python/analysis.py

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def load_data(filepath):
    """Load a tab-delimited file and return a DataFrame."""
    df = pd.read_csv(filepath, sep='\t', header=2)
    return df

def clean_data(df):    
    df = df[['Hugo_Symbol', 'Variant_Classification', 'Tumor_Sample_Barcode']]
    df = df.dropna()        
    return df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)

def analyze_data(df):
    summary = df['Hugo_Symbol'].value_counts().head(10)
    print("Top 10 mutated genes:")
    print(summary)
    fig, ax = plt.subplots()
    summary.plot(kind='bar', ax=ax)
    ax.set_xlabel('Gene')
    ax.set_ylabel('Mutation Count')
    ax.set_title('Top 10 Mutated Genes')
    return fig

if __name__ == "__main__":
    df = load_data("data/raw/aml_tcga_gdc/data_mutations.txt")
    cleaned_df = clean_data(df)
    save_data(cleaned_df, "data/processed/cleaned_mutations.csv")
    fig = analyze_data(cleaned_df)
    fig.savefig('results/top10_mutated_genes.png')
```

---

#### tests/python/test_analysis.py

```python
import os
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.python.analysis import load_data, clean_data, save_data, analyze_data

def create_test_data(tmp_path):
    df = pd.DataFrame({
        'Hugo_Symbol': ['TP53', 'BRCA1', 'TP53', 'EGFR'],
        'Variant_Classification': ['Missense', 'Nonsense', 'Missense', 'Silent'],
        'Tumor_Sample_Barcode': ['S1', 'S2', 'S3', 'S4']
    })
    input_file = tmp_path / 'test_mutations.txt'
    with open(input_file, 'w') as f:
        f.write("# The cBioPortalFiles\n")
        f.write("# Have 2 comment rows before the dataframe\n")        
    df.to_csv(input_file, sep='\t', index=False, mode='a')
    return input_file

def test_pipeline_smoke(tmp_path=Path(".")):    
    input_file = create_test_data(tmp_path)        
    loaded = load_data(input_file)    
    cleaned = clean_data(loaded)
    output_file = tmp_path / 'cleaned.csv'
    save_data(cleaned, output_file)
    fig = analyze_data(cleaned)
    plot_file = tmp_path / 'plot.png'
    fig.savefig(plot_file)
    assert os.path.exists(output_file)
    out_df = pd.read_csv(output_file)
    assert not out_df.empty
    assert set(['Hugo_Symbol', 'Variant_Classification', 'Tumor_Sample_Barcode']).issubset(out_df.columns)
    assert os.path.exists(plot_file)
```

---

#### Add a README to your analysis folder

```bash
echo -e "# Analysis Scripts\nThis folder contains Python scripts for data analysis. Each script is documented and tested." > src/python/README.md
cat src/python/README.md
```

---

