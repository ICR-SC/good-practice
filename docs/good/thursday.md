# Thursday Overview: R for Reproducible Research

**Goal:**  
Learn how to set up a reproducible research project in R, manage your code and data responsibly, and build a simple, tested analysis pipeline using RStudio.

---

### What We Cover

- **Project Setup & Data Privacy:**  
  - Reviewed a sensible folder structure for research projects.
  - Discussed the importance of `.gitignore` to keep sensitive or unnecessary files (like raw data and environment folders) out of version control.

- **Version Control with Git & RStudio:**  
  - Used Git (with RStudio or command line) to track project changes and collaborate safely.

- **Reproducible R Environments:**  
  - Used `renv` to manage project-specific R packages, ensuring reproducibility.

- **Downloading and Preparing Data:**  
  - Downloaded a real-world dataset from cBioPortal.
  - Used bash commands to organize and extract data into the project.

- **Building a Simple R Pipeline:**  
  - Wrote clear, well-documented R functions to:
    - Load tabular data
    - Clean/filter relevant columns
    - Save processed data
    - Analyze and plot the top 10 mutated genes
  - Saved results and plots to the appropriate folders.

- **Testing Your Code:**  
  - Wrote a basic test (using testthat) to check that the pipeline runs end-to-end and produces expected outputs.
  - Discussed the value of both unit and smoke tests for research code.

- **Ethical Coding & Documentation:**  
  - Emphasized the importance of documentation and code reuse.
  - Added a README to the analysis folder to explain what each script does.

---

### Key Takeaways

- Organize your project folders and use `.gitignore` to protect sensitive data.
- Use version control (Git) for all your code and documentation.
- Always use a reproducible environment for R projects (e.g., renv).
- Write modular, well-documented code for each step of your analysis.
- Test your code to catch errors early and ensure reproducibility.
- Document your scripts and results for yourself and others.

---

**Homework:**  
- Practice writing a simple R function for data loading or analysis.
- Write a short test to check your function works.
- Add a brief README or comments to explain your code.
- Explore The Turing Way’s code reuse checklist for more ideas.

---

## Session Cheat Sheet: Thursday

### Bash/Terminal and RStudio Commands

```bash
# List files and check .gitignore
ls
cat .gitignore

# Add common R exclusions to .gitignore
echo ".Rhistory\n.RData\n.Rproj.user/\nrenv/" >> .gitignore
cat .gitignore

# Create folders for R code and tests
mkdir -p src/R tests/R
ls

# Check git status
git status
```

### R Environment Setup

```r
# Using the R console in RStudio
install.packages("renv")
renv::init()
install.packages(c("tidyverse", "testthat"))
renv::snapshot()
```

### Data Download and Extraction
```bash
# Using the bash terminal in R Studio or your system terminal
mkdir -p data/raw
wget -O data/raw/aml_tcga_gdc.tar.gz https://cbioportal-datahub.s3.amazonaws.com/aml_tcga_gdc.tar.gz
tar -xzvf data/raw/aml_tcga_gdc.tar.gz -C data/raw
```

---

### R Code Snippets

#### src/R/analysis.R

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
# df <- load_data("data/raw/aml_tcga_gdc/data_mutations.txt")
# cleaned_df <- clean_data(df)
# save_data(cleaned_df, "data/processed/cleaned_mutations.csv")
# p <- analyze_data(cleaned_df)
# ggsave("results/top10_mutated_genes.png", plot = p, width = 8, height = 5)
```

---

#### tests/R/test_analysis.R

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

---

#### Add a README to your analysis folder

`bash`
```bash
echo -e "# Analysis Scripts\nThis folder contains R scripts for data analysis. Each script is documented and tested." > src/R/README.md
cat src/R/README.md
```
---  

## References
- Cerami et al. The cBio Cancer Genomics Portal: An Open Platform for Exploring Multidimensional Cancer Genomics Data. Cancer Discovery. May 2012; 401. [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/22588877)
- Gao et al. Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal. Sci. Signal. 6, pl1 (2013). [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/23550210)
- de Bruijn et al. Analysis and Visualization of Longitudinal Genomic and Clinical Data from the AACR Project GENIE Biopharma Collaborative in cBioPortal. Cancer Res (2023). [PubMed](https://pubmed.ncbi.nlm.nih.gov/37668528/)
- DataSet: https://www.cbioportal.org/study/plots?id=aml_tcga_gdc
