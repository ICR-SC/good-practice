# Monday Session Summary (For Researchers)

## What We Cover

- How to open and use the command line (Windows, Mac, Linux)
- Basic navigation and file/folder creation: `ls`, `cd`, `pwd`, `mkdir`, `touch`
- Logging into the Alma HPC cluster using SSH
- Understanding login nodes vs compute nodes on Alma
- Running interactive jobs with `srun`
- Creating a simple project folder for your research
- Opening and using VSCode for coding and project management
- Setting up a basic folder structure for a research project

## Key Takeaways

- Command line skills help you work efficiently and reproducibly
- Alma HPC is used for large-scale analyses; know how to log in and run jobs
- VSCode is a powerful tool for coding, documentation, and project organization
- A clear folder structure makes your research easier to manage and share

## Homework

- Practice basic command line commands
- Try logging into Alma if you have access
- Create and organize a simple project folder, and open it in VSCode

---

*This summary provides a quick reference to the main skills and concepts introduced in Monday's session.*

# Monday Resources: Good-Practices in Research Coding

## Key References

- **The Turing Way Handbook (General):**
  https://the-turing-way.netlify.app/
  - Principles of reproducible, ethical, and collaborative research.

- **The Turing Way: Reproducible Research Guide:**
  https://book.the-turing-way.org/reproducible-research/reproducible-research
  - Sections referenced throughout the week for best practices in reproducible research.

## Institutional Resources

- **Alma HPC Cluster (ICR):**
  - [Alma Documentation](https://alma.icr.ac.uk/) *(internal access required)*
  - SSH access: `ssh <username>@alma.icr.ac.uk`

- **VSCode Documentation:**
  https://code.visualstudio.com/docs
  - Getting started, integrated terminal, extensions, and project setup.

## Command Line Basics

- **Linux Command Line Tutorial:**
  https://ryanstutorials.net/linuxtutorial/
  - Navigation, file/folder creation, and basic commands.

## Example Commands Used in Session

```bash
# Open terminal and navigate
ls
cd <folder>
pwd

# Create folders and files
mkdir test_folder
cd test_folder
touch example.txt
ls

# Advanced folder creation
mkdir -p data/{raw,processed}

# Remove file and move up
rm example.txt
cd ..

# Open VSCode in project folder
code .
```

## Additional Reading

- **Why Reproducibility Matters:**
  https://www.nature.com/articles/d41586-019-00067-3

- **VSCode for Research:**
  https://www.r-bloggers.com/2021/03/vscode-for-research/

---

*This resource list supports the Monday session and provides links for further exploration and practice.*

# Monday Homework: Session Consolidation

## Practice Tasks

- Open your terminal and run the basic commands:
  - `pwd` (print working directory)
  - `ls` (list files and folders)
  - `mkdir` (make new folder)
  - `cd` (change directory)
  - `touch` (create a new file)

- Try logging into Alma (if you have access):
  - `ssh <username>@alma.icr.ac.uk`

- Create a simple project folder for your research:
  - `mkdir my_research_project`
  - `cd my_research_project`
  - `mkdir -p data/{raw,processed} src docs results notebooks environment`
  - `touch README.md .gitignore`
  - `code .` (open in VSCode)

## Reflection

- What did you find easy or challenging about using the command line?
- Were you able to log into Alma? If not, what issues did you encounter?
- How does organizing your project folder help your research?

---

*Complete these tasks before the next session to consolidate your skills and prepare for working with version control.*
