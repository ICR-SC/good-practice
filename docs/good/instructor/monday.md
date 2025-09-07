# Monday Live Coding Script: Good-Practices in Research Coding
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
| 1.9 Adding a file to the Project Structure      |     min        | 60 |
| 1.10 Writing some bash code                     |     min        | 65 |
| 1.11 Session Wrap-up & Homework                 |    5 min       | 70 |
| **Total**                                       |   **70 min**   | 70 |

---

## Pre-Session Setup

**[ASIDE: Have open and visible:
1) Prerequusites: https://icr-sc.github.io/good-practice/good/setup/  
2) Summary: https://icr-sc.github.io/good-practice/good/overview/  
3) Monday: https://icr-sc.github.io/good-practice/good/monday/  
4) Turing Way: https://book.the-turing-way.org/  
5) Have terminal  
6) VSCode open  
Have a clean desktop/folder structure visible.]**  


## Part 1.0 Opening & Welcome

>Good morning everyone! Welcome to our first session in the 'good-practices in research coding' series. Today we're going to get started with the command line and VSCode. This session is designed for beginners, but even if you have experience, you'll get a refresher and see how things work at our institution.

>Introduce yourself and the RSE team members present.

>These sessions are designed as follow-along sessions, a form of participatory live coding. Realistically you may not be following along now as they are designed also for your lunch break. The sessions >are recorded, so you can watch back and follow along when it is most convenient for you.  If you are following along live, type any questions in the chat and one of the RSE team members will do their best to help you as it goes.  We are happy to help you with any of these sessions afterwards, just get in touch or come along to one of >our drop in sessions on Monday or Tuesday lunch times.

---

## Part 1.1 (0 min-5 min)
### What is The Turing Way?

>The Turing Way is an open-source guide to reproducible, ethical, and collaborative research. It helps us make our work understandable and reusable by others. We will >refer to these principles as we go through our sessions this week."


---

## Part 1.2 (5 min-5 min)
### Starting a Command Line

>Let's open a command line. I'll be using Windows, with a mix of WSL2 and Powershell. If you're on Mac or Linux, you can use the built-in Terminal."

>**How to open a terminal:**
>- **Windows:** Search for 'WSL' or 'Powershell' in the Start menu
>- **Mac:** Use Spotlight (Cmd+Space), type 'Terminal'
>- **Linux:** Ctrl+Alt+T or search for 'Terminal'

**[ASIDE: Show your terminal. Wait for participants to open theirs. Troubleshoot any issues quickly.]**

---

## Part 1.3 (10 min-10 min)
### Basic Local Command Line

>Let's try some very basic commands. Type what I type."

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
>If you want to quickly edit a file from the command line, you can use the `nano` editor. For example, after creating a file with `touch example.txt`, type:
>
```bash
nano example.txt
```
>This opens the file in a simple editor. Type your text, then press `Ctrl+O` to save and `Ctrl+X` to exit.
>You can then type:
```bash
cat example.txt
```
>to see the contents of your file printed in the terminal.
>These commands help you navigate and create files and folders. If you get lost, use `pwd` to see where you are.

---

## Part 1.4 (20 min-10 min)
### More Advanced Command Line

>Let's try a few more useful commands. Don't worry if you haven't seen these before!

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

>Now let's log into our HPC cluster, Alma. This is where we run big analyses.


```bash
ssh <username>@alma.icr.ac.uk
```

>You'll need your username and password. If you have trouble, let us know.
>I have an ssh key set up in windows but not WSL2, you cans ee that in windows I can log straight in but in Ubuntu I need a password.

---

## Part 1.6 (35 min-5 min)
### Login Nodes vs Compute Nodes

>On Alma, there are login nodes (for connecting and setting up) and compute nodes (for running jobs). To access a compute node for interactive work, use this command:

```bash
srun --pty -t 12:00:00 --cpus-per-task 1 --mem-per-cpu 4021 --partition interactive bash
```

>Now you're on a compute node and can run your analysis.
>I am going to type exit to return to the login node and exit again to return to my local computer.
---

## Part 1.7 (40 min-5 min)
### Project Folder and VSCode

>Let's go back to our own computer and make a folder for a reproducible project. We'll use VSCode to work in it.

```bash
mkdir biomarkers_project
cd biomarkers_project
code .
```

>VSCode will open in your project folder. You can use the built-in terminal to run the same commands we've just learned.

---

## Part 1.8 (45 min-5 min)
### Making a Sensible Project Structure

>Let's quickly make a sensible folder structure for a biomarkers project. We'll talk more about project structure and data sensitivity next time.

```bash
mkdir -p data/{raw,processed} src docs results notebooks environment
ls
```
## Part 1.9 (50 min-5 min)
### Adding a file

>Let's add a README file to our project to describe it.

```bash
touch README.md
ls
```
Now you can see that I don't need to use nano to edit this file as I can use VSCode to do that.

---


## Part 1.10 (55 min-5 min)
### Writing some bash code
>Let’s create some very simple data files in our `data/raw` directory, and then write a bash script to “process” them into `data/processed`.
>I could crate the visually but it is easier to do it from the command line so I will do that.

```bash
# Make sure you are in your project folder
cd biomarkers_project

# Create the raw and processed directories if they don't exist
mkdir -p data/raw data/processed

# Create a simple data file in data/raw
echo -e "id,value\n1,10\n2,20" > data/raw/data1.csv
```
>This is a bash command that creates a new CSV file called data1.csv in the data/raw directory. It >writes two rows of data (with a header row) into the file. The -e flag allows interpretation >of the \n as newlines. We can see the file in VSCode.:

>If I arrow up I get the last command and I can edit it to quickly create 3 more files
```bash
echo -e "id,value\n3,30\n4,40" > data/raw/data2.csv
echo -e "id,value\n5,50\n6,60" > data/raw/data3.csv
echo -e "id,value\n7,70\n8,80" > data/raw/data4.csv
```

>Now let’s write a very simple bash script that “processes” these files. For now, it will just print a message for each file (you could also copy them if you want):

```bash
# Create a script called process_data.sh
touch src/process_data.sh
```

>Paste the following into the script:

```bash
#!/bin/bash
for file in data/raw/*.csv; do
	echo "Processing $file"	
    # Uncomment the next line to actually copy the files
    # cp "$file" data/processed/	
done
```

>The first line is called a "shebang" (or hashbang) line. It should be the very first line in a script file. It tells the operating system to use the Bash shell to interpret and run the script that follows. This ensures that when you execute the script (e.g., with ./process_data.sh), it will be run using Bash, regardless of your default shell.

>Make the script executable and run it:

```bash
chmod +x process_data.sh
./process_data.sh
```

>You should see a message for each file. If you want, you can uncomment the `cp` line in the script to actually copy the files to `data/processed`.



## Part 1.11 (65 min-5 min)
### Session Wrap-up & Homework

>You've learned how to use the command line, log into Alma, and set up a basic project folder. Next time, we'll go deeper into project structure and data sensitivity.

#### Homework (Session Consolidation):
- Practice opening your terminal and running the basic commands (`pwd`, `ls`, `mkdir`, `cd`)
- Try logging into Alma if you have access
- Create a simple project folder and open it in VSCode

**See you next session!**
