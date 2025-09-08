# Thursday Session: R for Reproducible Research (Beginner Edition)
## Live Coding Script for Instructors

*Duration: 60 minutes | Format: Participatory live coding*  
*Homework: Build a simple, reproducible analysis pipeline in R*

---

# Reference
This session builds on principles from [The Turing Way: Code Reuse](https://book.the-turing-way.org/reproducible-research/code-reuse), a guide to making research code transparent, ethical, and reusable.

---

## Pre-Session Setup

**[ASIDE: Open RStudio in your project folder from Monday/Tuesday. Ensure R is installed and available. Have a terminal ready.]**

---

## Opening & Welcome

>Welcome! Today we’ll use R to analyze data in a way that’s reproducible and ethical. We’ll keep things simple and practical, with tips for both beginners and those wanting a refresher.

---

## Part 3.1 (starts at 0 min, takes 10 min): Project Setup & Data Privacy

>"Let's review our project folder structure and talk about data privacy. It's important to keep sensitive data out of version control."

```bash
ls
cat .gitignore
```

>"We use a `.gitignore` file to protect sensitive data and keep our code clean. Let's add some common R exclusions."

```bash
echo ".Rhistory\n.RData\n.Rproj.user/\nrenv/" >> .gitignore
cat .gitignore
```
---

## Part 3.2 (starts at 10 min, takes 5 min): Setting Up Git in RStudio

>Now let's make sure our project is tracked with git. RStudio makes this easy."

**[EDIT: Open the Git tab in RStudio. Show the tracking]**

#### What I Type (Live Coding):
```bash
git status
```

---

## Part 3.3 (starts at 15 min, takes 5 min): Creating an R Environment

>A reproducible environment keeps your project dependencies organized. Let's use `renv` to manage packages."

```r
install.packages("renv")
renv::init()
install.packages(c("tidyverse", "testthat"))
renv::snapshot()
```

>Remember to add `renv/` to your `.gitignore` so it doesn't get tracked by git.

---

## Part 3.4 (starts at 20 min, takes 15 min): Writing Simple, Reproducible R Code

> Let's download a public dataset so that we have something meaningful to work with. We can use bash to do this and download from cBioPortal here: https://www.cbioportal.org/datasets. We will use this set: Acute Myeloid Leukemia (TARGET GDC, 2025).

```bash
mkdir -p data/raw
wget -O data/raw/aml_tcga_gdc.tar.gz https://cbioportal-datahub.s3.amazonaws.com/aml_tcga_gdc.tar.gz
tar -xzvf data/raw/aml_tcga_gdc.tar.gz -C data/raw
```
>This has extracted a fair amount of data. We won't use all of it but we can use some for our examples, let's use the file: `data/raw/aml_tcga_gdc/data_mutations.txt`.

>Let's write a simple function to load data. Clear function names and documentation help others understand your code. Create `src/R/analysis.R`:

```r
#!/usr/bin/env Rscript

library(readr)
library(dplyr)
library(ggplot2)

load_data <- function(filepath) {
    df <- read_tsv(filepath, skip = 2)
    return(df)
}

clean_data <- function(df) {
    df <- df %>%
        select(Hugo_Symbol, Variant_Classification, Tumor_Sample_Barcode) %>%
        na.omit()
    return(df)
}

save_data <- function(df, output_path) {
    write_csv(df, output_path)
}

analyze_data <- function(df) {
    summary <- df %>%
        count(Hugo_Symbol, sort = TRUE) %>%
        head(10)
    print("Top 10 mutated genes:")
    print(summary)
    p <- ggplot(summary, aes(x = reorder(Hugo_Symbol, -n), y = n)) +
        geom_bar(stat = "identity") +
        xlab("Gene") +
        ylab("Mutation Count") +
        ggtitle("Top 10 Mutated Genes") +
        theme(axis.text.x = element_text(angle = 45, hjust = 1))
    return(p)
}

# Example usage
df <- load_data("data/raw/aml_tcga_gdc/data_mutations.txt")
cleaned_df <- clean_data(df)
save_data(cleaned_df, "data/processed/cleaned_mutations.csv")
p <- analyze_data(cleaned_df)
ggsave("results/top10_mutated_genes.png", plot = p, width = 8, height = 5)
```

---

## Part 3.5 (starts at 35 min, takes 10 min): Basic Testing

>Testing helps catch mistakes and ensures your code works as expected. Let's write a simple test.

Create `tests/test_analysis.R`:
```r
library(testthat)
source("src/R/analysis.R")

test_that("pipeline smoke test", {
    df <- data.frame(
        Hugo_Symbol = c("TP53", "BRCA1", "TP53", "EGFR"),
        Variant_Classification = c("Missense", "Nonsense", "Missense", "Silent"),
        Tumor_Sample_Barcode = c("S1", "S2", "S3", "S4")
    )
    cleaned <- clean_data(df)
    expect_true(nrow(cleaned) > 0)
    expect_true(all(c("Hugo_Symbol", "Variant_Classification", "Tumor_Sample_Barcode") %in% colnames(cleaned)))
})
```

>Let's run our test.

```r
testthat::test_file("tests/test_analysis.R")
```

---

## Part 3.6 (starts at 45 min, takes 5 min): Ethical Coding & Documentation

>"Ethical coding means documenting your work and making it reusable. The Turing Way has a great checklist for code reuse:
>https://book.the-turing-way.org/reproducible-research/overview/overview-definitions
>One important aspect is documentation. Let's add a README to our analysis folder."

#### What I Type (Live Coding):
```bash
echo -e "# Analysis Scripts\nThis folder contains R scripts for data analysis. Each script is documented and tested." > src/R/README.md
cat src/R/README.md
```
---

## Session Wrap-up & Homework (starts at 50 min, takes 5 min)

>Great work today! You set up your project, protected sensitive data, used git in RStudio, created a reproducible environment, wrote and tested simple R code, and documented your work.

### Homework (Session Consolidation, ~30 min):
- Review today's steps by:
        - Creating a simple R function for data loading or analysis (use your own or example data)
        - Writing a short test to check your function works
        - Adding a brief README or comments to explain your code
- Spend a few minutes exploring The Turing Way’s code reuse checklist for ideas on making your code more reusable

**See you next session!**


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

>Welcome! Today we’ll use Python to analyze data in a way that’s reproducible and ethical. We’ll keep things simple and practical, with tips for both beginners and those wanting a refresher."

---

## Part 3.1 (starts at 0 min, takes 10 min): Project Setup & Data Privacy

>"Let's review our project folder structure and talk about data privacy. It's important to keep sensitive data out of version control."

```bash
ls
cat .gitignore
```

>"We use a `.gitignore` file to protect sensitive data and keep our code clean. Let's add some common Python exclusions."

```bash
echo "__pycache__/\n*.pyc\nenvironment/" >> .gitignore
cat .gitignore
```
---

## Part 3.2 (starts at 10 min, takes 5 min): Setting Up Git in VSCode

>Now let's make sure our project is tracked with git. VSCode makes this easy."

**[EDIT: Open the Source Control panel in VSCode. Show the tracking]**

#### What I Type (Live Coding):
```bash
git status
```

---

## Part 3.3 (starts at 15 min, takes 5 min): Creating a Python Virtual Environment

>A virtual environment keeps your project dependencies organized and reproducible. Let's create one."

```bash
python3 -m venv environment
source environment/bin/activate
pip install pandas pytest matplotlib
pip freeze > environment/requirements.txt
```

>Remember to add `environment/` to your `.gitignore` so it doesn't get tracked by git."

---

## Part 3.4 (starts at 20 min, takes 15 min): Writing Simple, Reproducible Python Code
> Let's download a public dataset so that we have something a little meaningful to work with. We can use bash to do this and download from cBioPortal here: https://www.cbioportal.org/datasets. We will use this set: Acute Myeloid Leukemia (TARGET GDC, 2025) which is 66MB.
```bash
mkdir -p data/raw
wget -O data/raw/aml_tcga_gdc.tar.gz https://cbioportal-datahub.s3.amazonaws.com/aml_tcga_gdc.tar.gz
tar -xzvf data/raw/aml_tcga_gdc.tar.gz -C data/raw
```
>This has extracted a fair amount of data. We won't use all of it but we can use some for our examples, let's use the file: `data/raw/aml_tcga_gdc/data_mutatations.txt`. You can see now how important it was that we added all the files in raw to our .gitognore as I don't need to worry that I might accidentally commit them all to the GitLab cloud.

>Let's write a simple function to load data. Clear function names and documentation help others understand your code. Create `src/python/analysis.py`:

```python
import pandas as pd

def load_data(filepath):
    """Load a tab-delimited file and return a DataFrame."""
    df = pd.read_csv(filepath, sep='\t', header=2)
    return df

if __name__ == "__main__":
    # Example usage
    df = load_data("data/raw/aml_tcga_gdc/data_mutations.txt")
    print(df.head())
```
>We can run this script directly from VSCode or in the terminal Use the Play button on the menu, or from the terminal type:
```bash
python src/python/analysis.py
```
>If I add a python shebang I don't need to specify python
```python
#!/usr/bin/env python3
```
## Let is make this a simple pipeline
>In a simple pipeline we migth load the data, clean the data, save the data analyse the data and create results. Let is create a function for each of these steps. We will keep it simple and just filter the data to a some fields and save that filtered data.

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
    # plot the data    
    fig, ax = plt.subplots()
    summary.plot(kind='bar', ax=ax)
    ax.set_xlabel('Gene')
    ax.set_ylabel('Mutation Count')
    ax.set_title('Top 10 Mutated Genes')
    return fig

if __name__ == "__main__":
    # Example usage
    df = load_data("data/raw/pancan_pcawg_2020/data_mutations.txt")
    cleaned_df = clean_data(df)
    save_data(cleaned_df, "data/processed/cleaned_mutations.csv")
    fig = analyze_data(cleaned_df)
    fig.savefig('results/top10_mutated_genes.png')        
    
```
## Part 3.5 (starts at 35 min, takes 10 min): Basic Testing

>Testing helps catch mistakes and ensures your code works as expected. Let's write a simple test.

Create `tests/test_analysis.py`:
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
    # Append the DataFrame below the comments
    df.to_csv(input_file, sep='\t', index=False, mode='a')
    return input_file


def test_pipeline_smoke(tmp_path=Path(".")):    
    # Create test data
    input_file = create_test_data(tmp_path)        
    # Run pipeline steps
    loaded = load_data(input_file)    
    cleaned = clean_data(loaded)
    output_file = tmp_path / 'cleaned.csv'
    save_data(cleaned, output_file)
    fig = analyze_data(cleaned)
    plot_file = tmp_path / 'plot.png'
    fig.savefig(plot_file)

    # Check outputs
    assert os.path.exists(output_file)
    out_df = pd.read_csv(output_file)
    assert not out_df.empty
    assert set(['Hugo_Symbol', 'Variant_Classification', 'Tumor_Sample_Barcode']).issubset(out_df.columns)
    assert os.path.exists(plot_file)

test_pipeline_smoke()
```

>Let's run our test.

```bash
pytest
```

---

## Part 3.6 (starts at 45 min, takes 5 min): Ethical Coding & Documentation

>"Ethical coding means documenting your work and making it reusable. The Turing Way has a great checklist for code reuse:
>https://book.the-turing-way.org/reproducible-research/overview/overview-definitions
>One important aspect documentation, let's add a README to our analysis folder."

#### What I Type (Live Coding):
```bash
echo -e "# Analysis Scripts\nThis folder contains Python scripts for data analysis. Each script is documented and tested." > src/python/README.md
cat src/python/README.md
```
---

## Session Wrap-up & Homework (starts at 50 min, takes 5 min)

>Great work today! You set up your project, protected sensitive data, used git in VSCode, created a virtual environment, wrote and tested simple Python code, and documented your work."

### Homework (Session Consolidation, ~30 min):
- Review today's steps by:
    - Creating a simple Python function for data loading or analysis (use your own or example data)
    - Writing a short test to check your function works
    - Adding a brief README or comments to explain your code
- Spend a few minutes exploring The Turing Way’s code reuse checklist for ideas on making your code more reusable

**See you next session!**