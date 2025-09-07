# Monday Session Summary (For Researchers)
{[*Return to home*](overview.md)} - {[*Instructor script*](instructor/monday.md)}

## Summary

- How to open and use the command line (Windows, Mac, Linux)
- Basic navigation and file/folder creation: `ls`, `cd`, `pwd`, `mkdir`, `touch`
- Logging into the Alma HPC cluster using SSH
- Understanding login nodes vs compute nodes on Alma
- Running interactive jobs with `srun`
- Creating a simple project folder for your research
- Opening and using VSCode for coding and project management
- Setting up a basic folder structure for a research project

## Homework

- Practice basic command line commands
- Try logging into Alma if you have access
- Create and organize a simple project folder, and open it in VSCode

---

# Monday Resources: Good-Practices in Research Coding

## Key References

- **The Turing Way Handbook (General):**
  [https://the-turing-way.netlify.app/](https://the-turing-way.netlify.app/)

- **The Turing Way: Reproducible Research Guide:**
  [https://book.the-turing-way.org/reproducible-research/reproducible-research](https://book.the-turing-way.org/reproducible-research/reproducible-research)
  
## Institutional Resources
  - Contact [Scientific Computing help desk](mailto:schelpdesk@icr.ac.uk) for questions
  - [Alma Documentation](https://almacookbook.github.io/)
  - SSH access: `ssh <username>@alma.icr.ac.uk` *(internal - vpn or network)*
  - [Alma docs on nexus](https://nexus.icr.ac.uk/strategic-initiatives/sc/hpc/Pages/New-Users-Guide.aspx)

## External Resources
- **VSCode Documentation:**
  [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)  
- **Linux Command Line Tutorial from the carpentries:**
  [https://swcarpentry.github.io/shell-novice/aio.html](https://swcarpentry.github.io/shell-novice/aio.html)
  
## Example Commands Used in Session

### Basic Local Command Line
```bash
# Where am I?
pwd
# List files and folders
ls
# Make a new folder for practice
mkdir test_folder
# Go into it
cd test_folder
# Make a file
touch example.txt
# See the file
ls
```

### Editing a File with nano
```bash
nano example.txt
```
>This opens the file in a simple editor. Type your text, then press `Ctrl+O` to save and `Ctrl+X` to exit.

```bash
cat example.txt
```

### More Advanced Command Line

```bash
# See hidden files
ls -la
# Make several folders at once
mkdir -p data/{raw,processed}
# See your folder structure
ls
# Remove a file
rm example.txt
# Go up a folder
cd ..
```

### Logging into Alma
```bash
ssh <username>@alma.icr.ac.uk
```

### Login Nodes vs Compute Nodes
```bash
srun --pty -t 12:00:00 --cpus-per-task 1 --mem-per-cpu 4021 --partition interactive bash
squeue -u $USER
```

### Project Folder and VSCode
```bash
cd ..
rm -rf test_folder
mkdir biomarkers_project
cd biomarkers_project
code .
```

### Making a Sensible Project Structure
```bash
mkdir -p data/{raw,processed} src docs results notebooks environment
```

### Adding a file
Let's create a file amd ,ale it executable
```bash
touch process_data.sh
```
Make the script executable and run it:
```bash
chmod +x process_data.sh
./process_data.sh
```











## Additional Reading

- **Why Reproducibility Matters:**
  [https://www.nature.com/articles/d41586-019-00067-3](https://www.nature.com/articles/d41586-019-00067-3)

- **VSCode for Research:**
  [https://www.r-bloggers.com/2021/03/vscode-for-research/](https://www.r-bloggers.com/2021/03/vscode-for-research/)

---

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

---  

## Reflection

- What did you find easy or challenging about using the command line?
- Were you able to log into Alma? If not, what issues did you encounter?
- How does organizing your project folder help your research?

---

*Complete these tasks before the next session to consolidate your skills and prepare for working with version control.*
