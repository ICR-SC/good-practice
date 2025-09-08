# Thursday Overview: R for Reproducible Research

**Goal:**  
Learn how to set up a reproducible research project in R, manage your code and data responsibly, and build a simple, tested analysis pipeline using RStudio.

---

### What We Covered

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
