# Thursday Resources: R for Reproducible Research

## Key References

- **The Turing Way: Code Reuse Guide:**
  https://book.the-turing-way.org/reproducible-research/code-reuse
  - Practical tips for making research code transparent, ethical, and reusable.

- **RStudio Documentation:**
  https://docs.posit.co/ide/user/
  - Getting started, integrated terminal, Git integration, and project setup.

- **renv Package Documentation:**
  https://rstudio.github.io/renv/
  - How to create and use R virtual environments for reproducibility.

- **testthat Package Documentation:**
  https://testthat.r-lib.org/
  - Writing and running basic tests for your R code.

## Example Commands Used in Session

```r
# Create and activate a virtual environment
install.packages("renv")
renv::init()

# Initialize git and make a commit
system('git init')
system('git add .')
system('git commit -m "Initial project setup"')

# Add R exclusions to .gitignore
writeLines(c(".Rhistory", ".RData", "environment/", "renv/"), ".gitignore", append=TRUE)

# Run a test
library(testthat)
testthat::test_file('tests/test_analysis.R')
```

## Additional Reading

- **Why Reproducibility Matters:**
  https://www.nature.com/articles/d41586-019-00067-3

- **Best Practices for Research Code:**
  https://www.turing.ac.uk/research/research-projects/best-practices-collaborative-coding

---

*This resource list supports the Thursday session and provides links for further exploration and practice.*
