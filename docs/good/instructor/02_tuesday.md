# Tuesday Live Coding Script: Good-Practices in Research Coding
[instructor home](overview.md)

## Monday Session Timings (Instructor Guide)

| Part | Section(s) Covered                                                                 | Suggested Time | Running Time |
|------|------------------------------------------------------------------------------------|:--------------:|:------------:|
| 1    | Opening, Welcome & Introduction to Version Control                                 |    10 min      |     10       |
| 2    | Setting Up Git & Basic Commands (config, init, add, commit, status, log)           |    15 min      |     25       |
| 3    | Remote Repositories & Collaboration (GitHub, GitLab, SSH keys, pushing, pulling)   |    15 min      |     40       |
| 4    | Branching, Merging & Conflict Resolution                                           |    15 min      |     55       |
| 5    | Best Practices, Project Boards, Wrap-up & Homework                                 |    10 min      |     65       |

---

## Pre-Session Setup

**[ASIDE: Have terminal, VSCode, and browser tabs open for GitHub and ICR GitLab. Make sure yesterday's biomarkers project is available. Check that participants have Git installed.]**

1) Prerequsites: [https://icr-sc.github.io/good-practice/good/setup/](https://icr-sc.github.io/good-practice/good/setup/)
2) Summary: [https://icr-sc.github.io/good-practice/good/overview/](https://icr-sc.github.io/good-practice/good/overview/)
3) Tuesday: [https://icr-sc.github.io/good-practice/good/tuesday/](https://icr-sc.github.io/good-practice/good/tuesday/)
4) Turing Way: [https://book.the-turing-way.org/](https://book.the-turing-way.org/)
5) Have terminal  
6) VSCode open  
Have a clean desktop/folder structure visible.]**  

---

## Part 1: Opening, Welcome and Introduction to Version Control

>"Good morning! Yesterday we set up our project folders and learned some command line basics. Today, we're going to learn about git, the tool that helps us keep track of changes and work together on research code. We'll use examples from our own institution, ICR."


>"Git is a tool that helps you save versions of your code and documents, so you can go back in time, undo mistakes, and work with others. It's like a super-powered undo button for your research project."

---

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

>Let's turn our biomarkers project into a git repository and learn the basic commands.  
>I am going to do this from the VSCode command line terminal.

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

## Part 2: Setting Up Git & Basic Commands

>At ICR, we use both GitHub and our internal GitLab for sharing code.

**GitHub organisation:** https://github.com/enterprises/icr/organizations
**ICR GitLab:** https://git.icr.ac.uk/

>You can create a repository on either platform. For sensitive or internal work, use ICR GitLab. For public or collaborative projects, GitHub is also available.


### Setting up keys for GitLab
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

### Using the gitlab repository for your project

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

> I could have done this a different way but first creating the project in gitlab and cloning it, which is the way I would usually work. One of the reasons for this is that when I create a project through the GitLab or GitHub web interface it will create some of the skepeketin that I want such as a readme and .gitiognore file. Another important file I want is the LICENSE.md file. This is a text file that describes the license under which I am sharing my code. There are many different licenses, and you can find out more about them here: https://choosealicense.com/. I am going to go to main page in GitLab and create a LICENSE.md file, this will automatically give me the license picker.I will choose the MIT license as it is simple and permissive. A license is necessary if you want to share your code with others.

---

### Using Git in IDEs

>You can use git inside VSCode or RStudio. Both have built-in tools to help you see changes, commit, and push without using the command line.

**[ASIDE: Show VSCode Source Control panel.]**
**[Show a change to the readme file being made and how it looks]**

---

### Using GitHub Desktop

>GitHub Desktop is a simple app for managing git visually. You can use it with both GitHub and GitLab repositories. It also can give you a colsolidated visual overview if you use multiple different apps like jpyter, vscode and rsudio.

**[ASIDE: Show GitHub Desktop or screenshots. Demonstrate opening the biomarkers project show how it looks with the waiting commit, which we will do from VSCode.]**

---

## Part 3: Remote Repositories & Collaboration

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

### Forgetting a commit message
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

### Resolving a Merge Conflict

>Merge conflicts are one of the most common fears in git, but they're just git's way of asking for your help when two people change the same part of a file. Let's see how to create and fix a simple conflict.

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

## Part 5: Good Practices for Research Projects

>To work with others, you can clone a repository, pull changes, and push your own updates.

```bash
# Clone a repository (example)
git clone https://git.icr.ac.uk/yourusername/biomarkers_project.git
# Pull latest changes
git pull
# Push your changes
git push
```

### gitignore files
> You may remember that when we created the csv files I observed that we should not put raw data files in git. We can do this by using a .gitignore file. This is a simple text file called .gitignore that lists patterns for files and folders that git should ignore.

```text
# Ignore all CSV files
*.csv   
```bash

### Project boards
>ICR GitLab and GitHub both have project boards and issues to help you manage tasks and issues. You can create cards for tasks, assign them to team members, and track progress.
**[ASIDE: Show GitHub or GitLab project board examples.]**

---

### Summary

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