# Tuesday Live Coding Script: Good-Practices in Research Coding
[instructor home](overview.md)

## Monday Session Timings (Instructor Guide)

| Section                                      | Suggested Time | Running Total |
|----------------------------------------------|:--------------:|:-------------:|
| Opening & Welcome                           |    5 min       |      5 min    |
| Reference to The Turing Way (Version Control)|    2 min       |      7 min    |
| Pre-Session Setup                           |    3 min       |     10 min    |
| Introduction to Version Control Concepts     |    5 min       |     15 min    |
| Setting Up Git & Configuring Identity        |    5 min       |     20 min    |
| Initializing a Repository & Tracking Changes |    8 min       |     28 min    |
| Basic Git Commands (add, commit, status, log)|    7 min       |     35 min    |
| Branching & Collaboration                   |    8 min       |     43 min    |
| Merge Demo & Resolving Conflicts            |   10 min       |     53 min    |
| Using GitHub, GitLab, VSCode, GitHub Desktop|    5 min       |     58 min    |
| Best Practices & Team Coding                |    4 min       |     62 min    |
| Session Wrap-up & Homework                  |    3 min       |     65 min    |
| **Total**                                   |   **65 min**   |     65 min    |

---

## 

*Duration: 60 minutes | Format: Participatory live coding*
*Homework: Short session consolidation*

# Reference
For more on version control and reproducible research, see [The Turing Way handbook: Version Control](https://book.the-turing-way.org/reproducible-research/vcs). This resource explains why version control is essential for collaborative, transparent, and reproducible research.

## Pre-Session Setup

**[ASIDE: Have terminal, VSCode, and browser tabs open for GitHub and ICR GitLab. Make sure yesterday's biomarkers project is available. Check that participants have Git installed.]**

>"Good morning! Yesterday we set up our project folders and learned some command line basics. Today, we're going to learn about git, the tool that helps us keep track of changes and work together on research code. We'll use examples from our own institution, ICR."

---

## Part 2.1 (starts at 0 min, takes 5 min): What is Git?

>"Git is a tool that helps you save versions of your code and documents, so you can go back in time, undo mistakes, and work with others. It's like a super-powered undo button for your research project."

---

## Part 2.2 (starts at 5 min, takes 5 min): Setting Up Git for Your Project

>"Let's check if git is installed and set up your name and email."

#### What I Type (Live Coding):
```bash
git --version
git config --list
git config --global user.name "Your Name"
git config --global user.email "your.email@icr.ac.uk"
git config --global init.defaultBranch main
git config --list
```

---

## Part 2.3 (starts at 10 min, takes 8 min): Basic Git Commands

>Let's turn our biomarkers project into a git repository and learn the basic commands.  
>I am going to do this from the VSCode command line terminal.

#### What I Type (Live Coding):
```bash
cd biomarkers_project
code .
git init
git status
git add README.md
git commit -m "Add README for biomarkers project"
git status
```
---

## Part 2.4 (starts at 18 min, takes 5 min): Using Git at ICR

>At ICR, we use both GitHub and our internal GitLab for sharing code.

**GitHub organisation:** https://github.com/enterprises/icr/organizations
**ICR GitLab:** https://git.icr.ac.uk/

>You can create a repository on either platform. For sensitive or internal work, use ICR GitLab. For public or collaborative projects, GitHub is also available.


## Setting up keys for GitLab
> You need to set up an ssh key for GitLab. You can follow the instructions here: https://git.icr.ac.uk/help/ssh/README

```bash
ssh-keygen -t ecdsa -C ""
```

>This will create a key file ~/.ssh/id_ecdsa.pub. Copy the content of this file to gitlab (via web interface) in User/Preference/SSH Keys > Add new key

` ~/.ssh/config`
```text
# Private GitLab instance
Host <your_usernames>.git.icr.ac.uk
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_ecdsa

```

## Using the gitlab repository for your project

> I am going to use GitLab for this example. I am now going to go to GitLab and create a project somewhere I think is sensible:
https://git.icr.ac.uk/ralcraft/biomarkers_project
> Follow the instructions when I created an empty proect

```bash
git init --initial-branch=main
git remote add origin git@git.icr.ac.uk:ralcraft/biomarkers_project.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
```
---

## Part 2.5 (starts at 23 min, takes 5 min): Using Git in IDEs

>You can use git inside VSCode or RStudio. Both have built-in tools to help you see changes, commit, and push without using the command line.

**[ASIDE: Show VSCode Source Control panel.]**
**[Show a change to the readme file being made and how it looks]**

---

## Part 2.6 (starts at 28 min, takes 5 min): Using GitHub Desktop

>GitHub Desktop is a simple app for managing git visually. You can use it with both GitHub and GitLab repositories. It also can give you a colsolidated visual overview if you use multiple different apps like jpyter, vscode and rsudio.

**[ASIDE: Show GitHub Desktop or screenshots. Demonstrate opening the biomarkers project show how it looks with the waiting commit, which we will do from VSCode.]**

---

## Part 2.7 (starts at 33 min, takes 8 min): Working with Branches

>Branches let you try new ideas without breaking your main code. 
>Branches and the flow are a big topic and there are many ways to use them for different project types.  An example of 6 different methods is here: https://dev.to/juniourrau/6-types-of-git-branching-strategy-g54
Here I will just show a simple example of making a branch, switching to it, making a change and then merging it back to main.

```bash
git branch experiment
git checkout experiment
echo "# Testing a new analysis" > test.txt
git add test.txt
git commit -m "Add test analysis file"
git checkout main
git merge experiment
```

**[Aside Look at how this looks in the tool I have used]**
---

## Part 2.8a (starts at 41 min, takes 10 min): Forgetting a commit message
>Forgetting a commit message is something that happens to everyone. Here are some ways to fix it.
>I create a change to the test.sh file then visually commit it without a message.
> I type the commit at the top and simply close the file down

? DO it again and this time through the command line, make another change

```bash
# Make a commit without a message
git add .
git commit
```
>Nano pops up and I do the same thing as I did, enter and close

## Part 2.8b (starts at 41 min, takes 10 min): Resolving a Merge Conflict

>Merge conflicts are one of the most common fears in git, but they're just git's way of asking for your help when two people change the same part of a file. Let's see how to create and fix a simple conflict.

#### What I Type (Live Coding):
```bash
# On main branch, edit README.md in vscode
git add README.md
git commit -m "Edit README on main branch"

# Create and switch to a new branch
git checkout -b conflict-demo
# Edit the same line in README.md in vscode
git add README.md
git commit -m "Edit README on conflict-demo branch"

# Switch back to main
git checkout main
# edit readme  in vscode
git add README.md
git commit -m "Another edit on main branch"

# Try to merge conflict-demo into main
git merge conflict-demo
# Git will report a conflict in README.md
```

>Git will stop and show a conflict in README.md. Open the file and you'll see both versions marked like this
```text
<<<<<<< HEAD
Another change on main branch.
=======
This is the conflict-demo branch version.
>>>>>> conflict-demo
```
>Edit the file to keep what you want (or combine both), then save it."

```bash
# After editing README.md to resolve the conflict:
git add README.md
git commit -m "Resolve merge conflict in README.md"
```

>That's it! Merge conflicts are normal and just mean git needs your help. Take your time, read the markers, and choose what you want to keep.

---

## Part 2.9 (starts at 51 min, takes 5 min): Collaborating with Others

>To work with others, you can clone a repository, pull changes, and push your own updates.

#### What I Type (Live Coding):
```bash
# Clone a repository (example)
git clone https://git.icr.ac.uk/yourusername/biomarkers_project.git
# Pull latest changes
git pull
# Push your changes
git push
```

## Part 2.10 gitignore files
> You may remember that when we created the csv files I observed that we should not put raw data files in git. We can do this by using a .gitignore file. This is a simple text file called .gitignore that lists patterns for files and folders that git should ignore.

```text
# Ignore all CSV files
*.csv   
```bash

## Part 2.11 Project boards
>ICR GitLab and GitHub both have project boards and issues to help you manage tasks and issues. You can create cards for tasks, assign them to team members, and track progress.
**[ASIDE: Show GitHub or GitLab project board examples.]**

---

## Part 2.12 (starts at 56 min, takes 4 min): Best Practices for Research Projects

>- Commit often with clear messages
>- Don't put raw data or sensitive files in git
>- Use branches for new ideas, there are many ways to use brances for different projject types
>- Always pull before you push
>- Use .gitignore to keep your repository clean

---


## Session Wrap-up & Homework (starts at 60 min, takes 3 min)

### What I Say:
"Great job today! You've learned the basics of git, how to use it at ICR, and how to work with others. Next time, we'll build on this with more coding and analysis."

### Homework (Session Consolidation):
- Practice the basic git commands (`init`, `add`, `commit`, `status`) in your biomarkers project
- Try making a branch and merging it
- Explore the ICR GitLab or GitHub organisation

**See you next session!**