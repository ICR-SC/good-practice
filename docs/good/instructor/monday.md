# Monday Session: Good-Practices in Research Coding (Beginner Edition)
[instructor home](overview.md)

## Monday Session Timings (Instructor Guide)

| Section                                      | Suggested Time |
|----------------------------------------------|:--------------:|
| 1.0 Opening & Welcome                           |    5 min       |
| 1.1 What is The Turing Way?                     |    5 min       |
| 1.2 Starting a Command Line                     |    5 min       |
| 1.3 Basic Local Command Line Functionality      |   10 min       |
| 1.4 More Advanced Command Line Tools & Techniques|   10 min       |
| 1.5 Logging into Alma (HPC Cluster)             |    5 min       |
| 1.6 Login Nodes vs Compute Nodes                |    5 min       |
| 1.7 Navigating Locally, Creating Project Folder, Opening VSCode | 5 min |
| 1.8 Making a Sensible Project Structure         |    5 min       |
| 1.9 Practical Exercise (Individual)             |   15 min       |
| 1.10 Session Wrap-up & Homework                  |    5 min       |
| **Total**                                   |   **60 min**   |

---

## Pre-Session Setup

**[ASIDE: Have terminal and VSCode open. Share screen showing both. Have a clean desktop/folder structure visible.]**


## Part 1.0 Opening & Welcome

**What I Say:**
"Good morning everyone! Welcome to our first session in the 'good-practices in research coding' series. Today we're going to get started with the command line and VSCode. This session is designed for beginners, but even if you have experience, you'll get a refresher and see how things work at our institution."

---

## Part 1.1 (starts at 0 min, takes 5 min)
### What is The Turing Way?

**What I Say:**
"The Turing Way is an open-source guide to reproducible, ethical, and collaborative research. It helps us make our work understandable and reusable by others. We will refer to these principles as we go through our sessions this week."

---

## Part 1.2 (starts at 5 min, takes 5 min)
### Starting a Command Line

**What I Say:**
"Let's open a command line. I'll be using Windows, with a mix of WSL2 and Powershell. If you're on Mac or Linux, you can use the built-in Terminal."

**How to open a terminal:**
- **Windows:** Search for 'WSL' or 'Powershell' in the Start menu
- **Mac:** Use Spotlight (Cmd+Space), type 'Terminal'
- **Linux:** Ctrl+Alt+T or search for 'Terminal'

**[ASIDE: Show your terminal. Wait for participants to open theirs. Troubleshoot any issues quickly.]**

---

## Part 1.3 (starts at 10 min, takes 10 min)
### Basic Local Command Line Functionality

**What I Say:**
"Let's try some very basic commands. Type what I type."

**What I Type (Live Coding):**
```bash
# Where am I?

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

**What I Say:**
"These commands help you navigate and create files and folders. If you get lost, use `pwd` to see where you are."

---

## Part 1.4 (starts at 20 min, takes 10 min)
### More Advanced Command Line Tools & Techniques

**What I Say:**
"Let's try a few more useful commands. Don't worry if you haven't seen these before!"

**What I Type (Live Coding):**
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

---

## Part 1.5 (starts at 30 min, takes 5 min)
### Logging into Alma (HPC Cluster)

**What I Say:**
"Now let's log into our HPC cluster, Alma. This is where we run big analyses."

**What I Type (Live Coding):**
```bash
ssh <username>@alma.icr.ac.uk
```

**What I Say:**
"You'll need your username and password. If you have trouble, let us know."

---

## Part 1.6 (starts at 35 min, takes 5 min)
### Login Nodes vs Compute Nodes

**What I Say:**
"On Alma, there are login nodes (for connecting and setting up) and compute nodes (for running jobs). To access a compute node for interactive work, use this command:"

**What I Type (Live Coding):**
```bash
srun --pty -t 12:00:00 --cpus-per-task 1 --mem-per-cpu 4021 --partition interactive bash
```

**What I Say:**
"Now you're on a compute node and can run your analysis."

---

## Part 1.7 (starts at 40 min, takes 5 min)
### Navigating Locally, Creating a Project Folder, and Opening VSCode

**What I Say:**
"Let's go back to our own computer and make a folder for a reproducible project. We'll use VSCode to work in it."

**What I Type (Live Coding):**
```bash
mkdir biomarkers_project
cd biomarkers_project
code .
```

**What I Say:**
"VSCode will open in your project folder. You can use the built-in terminal to run the same commands we've just learned."

---

## Part 1.8 (starts at 45 min, takes 5 min)
### Making a Sensible Project Structure

**What I Say:**
"Let's quickly make a sensible folder structure for a biomarkers project. We'll talk more about project structure and data sensitivity next time."

**What I Type (Live Coding):**
```bash
mkdir -p data/{raw,processed} src docs results notebooks environment
ls
```

---

## Part 1.9 Practical Exercise (starts at 50 min, takes 15 min)

### Individual Exercise

**What I Say:**
"Now it's your turn! I want you to practice what we've learned by creating a project structure for your own research."

#### Exercise Instructions:

**Core Tasks:**
1. Create a new project directory for your research area
2. Set up the folder structure we learned today (use the mkdir -p command)
3. Create a basic README.md with your project description
4. Create a .gitignore appropriate for your research
5. Open the project in VSCode

**Example command sequence:**
```bash
mkdir my_research_project
cd my_research_project
mkdir -p data/{raw,processed} src/{python,r} docs results/{figures,tables} notebooks environment
touch README.md .gitignore
code .
```

**Focus on:**
- Clear project organization
- Meaningful directory names
- Basic documentation


**[ASIDE: Circulate and help participants. Focus on ensuring everyone can complete the basic directory structure.]**

---

## Part 1.10 Session Wrap-up & Homework (starts at 65 min, takes 5 min)

**What I Say:**
"Great job today! You've learned how to use the command line, log into Alma, and set up a basic project folder. Next time, we'll go deeper into project structure and data sensitivity."

#### Homework (Session Consolidation):
- Practice opening your terminal and running the basic commands (`pwd`, `ls`, `mkdir`, `cd`)
- Try logging into Alma if you have access
- Create a simple project folder and open it in VSCode

**See you next session!**
