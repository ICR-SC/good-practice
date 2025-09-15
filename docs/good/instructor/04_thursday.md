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

>Let's review our project folder structure and talk about data privacy. It's important to keep sensitive data out of version control.

```bash
ls
cat .gitignore
```

>We use a `.gitignore` file to protect sensitive data and keep our code clean. Let's add some common R exclusions.

```bash
echo -e ".Rhistory\n.RData\n.Rproj.user/\nrenv/" >> .gitignore
cat .gitignore
```

>The difference between `>` and `>>` is that `>` overwrites the file, while `>>` appends to it. Always use `>>` when adding to `.gitignore`. Or you could ammend in the editor of VSCode too.

>We also want to make sure we have the folders for R.

```bash
mkdir -p src/R tests/R
ls
```

---

>Open rstudio (use the command line) and then create a new project in the current directory. Now we can see the files we have created. If you have not already initiaised git from the git session do `git init`


## Part 3.2 (starts at 10 min, takes 5 min): Setting Up Git in RStudio

>Now let's make sure our project is tracked with git. RStudio makes this easy.

**[EDIT: Open the Git tab in RStudio. Show the tracking]**

#### What I Type (Live Coding):
```bash
git status
```

---

## Part 3.3 (starts at 15 min, takes 5 min): Creating an R Environment

>A reproducible environment keeps your project dependencies organized. Let's use `renv` to manage packages.

```r
# Using the r console in RStudio
install.packages("renv")
renv::init()
install.packages(c("tidyverse", "testthat"))
renv::snapshot()
```

>Remember to add `renv/` to your `.gitignore` so it doesn't get tracked by git.

>renv::snapshot() saves the current state of your R project's package environment. It records all the packages (and their versions) you have installed into a file called renv.lock. This makes your project reproducible: anyone else (or you in the future) can use renv::restore() to recreate the exact same package environment from that lock file.

>When you open your project you see something like:
```r
- Project '~/good-practice/biomarkers_project' loaded. [renv 1.1.5]
[Workspace loaded from ~/good-practice/biomarkers_project/.RData]
```

---

## Part 3.4 (starts at 20 min, takes 15 min): Writing Simple, Reproducible R Code
> Let's download a public dataset so that we have something a little meaningful to work with. We can use bash to do this and download from cBioPortal here: https://www.cbioportal.org/datasets. We will use this set: Acute Myeloid Leukemia (TARGET GDC, 2025) which is 66MB.

```bash
# Using bash
mkdir -p data/raw
wget -O data/raw/aml_tcga_gdc.tar.gz https://cbioportal-datahub.s3.amazonaws.com/aml_tcga_gdc.tar.gz
tar -xzvf data/raw/aml_tcga_gdc.tar.gz -C data/raw
```
>This has extracted a fair amount of data. We won't use all of it but we can use some for our examples, let's use the file: `data/raw/aml_tcga_gdc/data_mutatations.txt`. You can see now how important it was that we added all the files in raw to our .gitognore as I don't need to worry that I might accidentally commit them all to the GitLab cloud.

>Let's write a simple function to load data. Clear function names and documentation help others understand your code. Create `src/R/analysis.R`:


**MOVE TO VIDEO 2**


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

**MOVE to VIDEO 3**

>If we uncomment out the Exaple usage section it will run through a test

---

## Part 3.5 (starts at 35 min, takes 10 min): Basic Testing

>Testing helps catch mistakes and ensures your code works as expected. Let's write a simple test.

Create `tests/R/test_analysis.R`:
```r
library(testthat)
source("../../src/R/analysis.R")

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
# In the R console
testthat::test_file("tests/R/test_analysis.R")
```

---

## Part 3.6 (starts at 45 min, takes 5 min): Ethical Coding & Documentation

>Ethical coding means documenting your work and making it reusable. The Turing Way has a great checklist for code reuse:
>https://book.the-turing-way.org/reproducible-research/overview/overview-definitions
>One important aspect is documentation. Let's add a README to our analysis folder.

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