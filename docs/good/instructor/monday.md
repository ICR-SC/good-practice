# Monday Session: Good-Practices in Research Coding (Beginner Edition)
[instructor home](overview.md)

## Monday Session Timings (Instructor Guide)

| Section                                      | Suggested Time | Running Time |
|----------------------------------------------|:--------------:|:------------:|
| 1.0 Opening & Welcome                           |    5 min       | 5  |
| 1.1 What is The Turing Way?                     |    5 min       | 10 |
| 1.2 Starting a Command Line                     |    5 min       | 15 |
| 1.3 Basic Local Command Line Functionality      |   10 min       | 25 |
| 1.4 More Advanced Command Line Tools            |   10 min       | 35 |
| 1.5 Logging into Alma (HPC Cluster)             |    5 min       | 40 |
| 1.6 Login Nodes vs Compute Nodes                |    5 min       | 45 |
| 1.7 Navigating Locally, Projects, VSCode        |    5 min       | 50 |
| 1.8 Making a Sensible Project Structure         |    5 min       | 55 |
| 1.9 Session Wrap-up & Homework                  |    5 min       | 60 |
| **Total**                                       |   **60 min**   | 60 |

---

## Pre-Session Setup

**[ASIDE: Have terminal and VSCode open. Share screen showing both. Have a clean desktop/folder structure visible.]**


## Part 1.0 Opening & Welcome

**What I Say:**
>Good morning everyone! Welcome to our first session in the 'good-practices in research coding' series. Today we're going to get started with the command line and VSCode. >This session is designed for beginners, but even if you have experience, you'll get a refresher and see how things work at our institution.

>These sessions are designed as follow-along sessions, but realistically you may not be following along now as they are designed also for your lunch break. The sessions >are recorded, so you can watch back and follow along when it is most convenient for you.  If you are following along live, type any questions in the chat and one of the >RFSE team memebrs will do their best to help you as it goes.  We are happy to help you with any of these sessions afterwards, just get in touch or come along to one of >our drop in sessions on Monday or Tuesday lunch times.

---

## Part 1.1 (0 min-5 min)
### What is The Turing Way?

**What I Say:**

>The Turing Way is an open-source guide to reproducible, ethical, and collaborative research. It helps us make our work understandable and reusable by others. We will >refer to these principles as we go through our sessions this week."


---

## Part 1.2 (5 min-5 min)
### Starting a Command Line

**What I Say:**

>Let's open a command line. I'll be using Windows, with a mix of WSL2 and Powershell. If you're on Mac or Linux, you can use the built-in Terminal."

>**How to open a terminal:**
>- **Windows:** Search for 'WSL' or 'Powershell' in the Start menu
>- **Mac:** Use Spotlight (Cmd+Space), type 'Terminal'
>- **Linux:** Ctrl+Alt+T or search for 'Terminal'

**[ASIDE: Show your terminal. Wait for participants to open theirs. Troubleshoot any issues quickly.]**

---

## Part 1.3 (10 min-10 min)
### Basic Local Command Line

**What I Say:**
>Let's try some very basic commands. Type what I type."

**What I Type (Live Coding):**
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

**What I Say:**
>These commands help you navigate and create files and folders. If you get lost, use `pwd` to see where you are.

---

## Part 1.4 (20 min-10 min)
### More Advanced Command Line

**What I Say:**
>Let's try a few more useful commands. Don't worry if you haven't seen these before!

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

## Part 1.5 (30 min-5 min)
### Logging into Alma

**What I Say:**
>Now let's log into our HPC cluster, Alma. This is where we run big analyses.


**What I Type (Live Coding):**
```bash
ssh <username>@alma.icr.ac.uk
```

**What I Say:**
>You'll need your username and password. If you have trouble, let us know.

---

## Part 1.6 (35 min-5 min)
### Login Nodes vs Compute Nodes

**What I Say:**
>On Alma, there are login nodes (for connecting and setting up) and compute nodes (for running jobs). To access a compute node for interactive work, use this command:

**What I Type (Live Coding):**
```bash
srun --pty -t 12:00:00 --cpus-per-task 1 --mem-per-cpu 4021 --partition interactive bash
```

**What I Say:**
>Now you're on a compute node and can run your analysis.

---

## Part 1.7 (40 min-5 min)
### Project Folder and VSCode

**What I Say:**
>Let's go back to our own computer and make a folder for a reproducible project. We'll use VSCode to work in it.

**What I Type (Live Coding):**
```bash
mkdir biomarkers_project
cd biomarkers_project
code .
```

**What I Say:**
>VSCode will open in your project folder. You can use the built-in terminal to run the same commands we've just learned.

---

## Part 1.8 (45 min-5 min)
### Making a Sensible Project Structure

**What I Say:**
>Let's quickly make a sensible folder structure for a biomarkers project. We'll talk more about project structure and data sensitivity next time.

**What I Type (Live Coding):**
```bash
mkdir -p data/{raw,processed} src docs results notebooks environment
ls
```

---

## Part 1.9 (65 min-5 min)
### Session Wrap-up & Homework

**What I Say:**
>You've learned how to use the command line, log into Alma, and set up a basic project folder. Next time, we'll go deeper into project structure and data sensitivity.

#### Homework (Session Consolidation):
- Practice opening your terminal and running the basic commands (`pwd`, `ls`, `mkdir`, `cd`)
- Try logging into Alma if you have access
- Create a simple project folder and open it in VSCode

**See you next session!**
