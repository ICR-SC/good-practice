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

### What I Say:
"Welcome! Today we’ll use R to analyze data in a way that’s reproducible and ethical. We’ll keep things simple and practical, with tips for both beginners and those wanting a refresher."

---

## Part 4.1 (starts at 0 min, takes 10 min): Project Setup & Data Privacy

### What I Say:
"Let's review our project folder structure and talk about data privacy. It's important to keep sensitive data out of version control."

#### What I Show (Live Coding):
```r
list.files()
readLines('.gitignore')
```

### What I Say:
"We use a `.gitignore` file to protect sensitive data and keep our code clean. Let's add some common R exclusions."

#### What I Type (Live Coding):
```r
writeLines(c(".Rhistory", ".RData", "environment/"), ".gitignore", append=TRUE)
readLines('.gitignore')
```

---

## Part 4.2 (starts at 10 min, takes 5 min): Setting Up Git in RStudio

### What I Say:
"Now let's make sure our project is tracked with git. RStudio makes this easy."

#### What I Show (Live Coding):
- Open the Git tab in RStudio.

#### What I Type (Live Coding):
```bash
git init
git add .
git commit -m "Initial project setup"
git status
```

---

## Part 4.3 (starts at 15 min, takes 5 min): Creating an R Virtual Environment

### What I Say:
"An R environment keeps your project dependencies organized and reproducible. Let's create one using renv."

#### What I Type (Live Coding):
```r
install.packages("renv")
renv::init()
```

### What I Say:
"Remember to add `environment/` and `renv/` to your `.gitignore` so they don't get tracked by git."

---

## Part 4.4 (starts at 20 min, takes 15 min): Writing Simple, Reproducible R Code

### What I Say:
"Let's write a simple function to load data. Clear function names and documentation help others understand your code."

#### What I Type (Live Coding):
Create `src/r/analysis.R`:
```r
load_data <- function(filepath) {
  # Load a CSV file and return a data frame
  read.csv(filepath)
}
```

### What I Say:
"Let's run our function in an R script or R Markdown document."

#### What I Type (Live Coding):
```r
source('src/r/analysis.R')
df <- load_data('data/processed/example.csv')
head(df)
```

---

## Part 4.5 (starts at 35 min, takes 10 min): Basic Testing

### What I Say:
"Testing helps catch mistakes and ensures your code works as expected. Let's write a simple test using testthat."

#### What I Type (Live Coding):
Create `tests/test_analysis.R`:
```r
library(testthat)
source('src/r/analysis.R')

test_that("load_data works", {
  df <- load_data('data/processed/example.csv')
  expect_true(nrow(df) > 0)
})
```

### What I Say:
"Let's run our test."

#### What I Type (Live Coding):
```r
testthat::test_file('tests/test_analysis.R')
```

---

## Part 4.6 (starts at 45 min, takes 5 min): Ethical Coding & Documentation

### What I Say:
"Ethical coding means documenting your work and making it reusable. The Turing Way has a great checklist for code reuse. Let's add a README to our analysis folder."

#### What I Type (Live Coding):
```r
writeLines("# Analysis Scripts\nThis folder contains R scripts for data analysis. Each script is documented and tested.", "src/r/README.md")
readLines("src/r/README.md")
```

---

## Session Wrap-up & Homework (starts at 50 min, takes 5 min)

### What I Say:
"Great work today! You set up your project, protected sensitive data, used git in RStudio, created an R environment, wrote and tested simple R code, and documented your work."

### Homework (Session Consolidation, ~30 min):
- Review today's steps by:
    - Creating a simple R function for data loading or analysis (use your own or example data)
    - Writing a short test to check your function works
    - Adding a brief README or comments to explain your code
- Spend a few minutes exploring The Turing Way’s code reuse checklist for ideas on making your code more reusable

**See you next session!**