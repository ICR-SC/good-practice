# Monday Overview: Good-Practices in Research Coding

**Goal:**  
Learn how to use the command line, log into the Alma HPC cluster, and set up a sensible, reproducible project folder for your research.

---

## What We Cover

- How to open and use the command line (Windows, Mac, Linux)
- Basic navigation and file/folder creation: `ls`, `cd`, `pwd`, `mkdir`, `touch`
- Editing files with `nano` and viewing them with `cat`
- Logging into the Alma HPC cluster using SSH
- Understanding login nodes vs compute nodes on Alma
- Running interactive jobs with `srun`
- Creating a simple, organized project folder for your research
- Opening and using VSCode for coding and project management

---

## Key Takeaways

- The command line is a powerful tool for navigating, creating, and managing files and folders.
- Use [`.gitignore`](.gitignore ) to keep sensitive or unnecessary files out of version control.
- Organize your project folders for clarity and reproducibility.
- Use VSCode’s built-in terminal and editor to streamline your workflow.
- Practice makes perfect—try these commands on your own!

---

## Videos of session

Link to video [Good Practice-Session 01 Part 01](https://youtu.be/UetHMph6iQo)  
Link to video [Good Practice-Session 01 Part 02](https://youtu.be/ckdpX6D-fdk)  
Link to video [Good Practice-Session 01 Part 03](https://youtu.be/eZOjNbW5KYQ)  

## Session Cheat Sheet: Monday

### Basic Command Line

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

### Editing and Viewing Files

```bash
nano example.txt
# (Type your text, then Ctrl+O to save, Ctrl+X to exit)

cat example.txt
```

### More Advanced Command Line

```bash
# See hidden files
ls -la

# Make several folders at once
mkdir -p data/{raw,processed}

# Remove a file
rm example.txt

# Go up a folder
cd ..
```

### Logging into Alma

```bash
ssh <username>@alma.icr.ac.uk
```

### Compute Nodes

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

### Adding and Running a Script

```bash
touch process_data.sh
chmod +x process_data.sh
./process_data.sh
```

---

## Homework

- Practice basic command line commands
- Try logging into Alma if you have access
- Create and organize a simple project folder, and open it in VSCode

---

## Reflection

- What did you find easy or challenging about using the command line?
- Were you able to log into Alma? If not, what issues did you encounter?
- How does organizing your project folder help your research?