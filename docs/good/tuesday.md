# Tuesday Overview: Version Control and Collaboration in Research Coding

**Goal:**  
Understand the basics of version control with Git, set up repositories, collaborate using GitHub and GitLab, and integrate version control into your research workflow.

---

## What We Cover

- Introduction to version control and why it matters for research
- Setting up Git and configuring your identity
- Initializing a repository and tracking changes
- Basic Git commands: `git add`, `git commit`, `git status`, `git log`
- Creating and switching branches for collaborative work
- Merging branches and resolving merge conflicts
- Using GitHub and ICR GitLab for remote collaboration
- Integrating Git with VSCode and GitHub Desktop
- Best practices for team coding and project management
- Choosing a license in GitLab and GitHub

---

## Key Takeaways

- Version control helps you track changes, collaborate, and avoid losing work.
- Git is the most widely used version control system in research and industry.
- Branching and merging allow for safe experimentation and teamwork.
- Remote repositories (GitHub, GitLab) enable collaboration and backup.
- Integrating Git with editors like VSCode streamlines your workflow.

---

## Videos of session

Link to video [Good Practice-Session 02 Part 01](https://youtu.be/aLvv7utZYbA)  
Link to video [Good Practice-Session 02 Part 02](https://youtu.be/J2FkQRxtatY)  
Link to video [Good Practice-Session 02 Part 03](https://youtu.be/uPKRqBp-Av8)  

---  

## Session Cheat Sheet: Tuesday

### Setting Up Git for Your Project

```bash
git --version
git config --list
git config --global user.name "Your Name"
git config --global user.email "your.email@icr.ac.uk"
git config --global init.defaultBranch main
git config --list
```

### Basic Git Commands

```bash
cd biomarkers_project
code .
git init
git status
git add README.md
git commit -m "Add README for biomarkers project"
git status
```

### Using Git at ICR

- [GitHub organisation:](https://github.com/enterprises/icr/organizations)
- [ICR GitLab:](https://git.icr.ac.uk/)

### Setting up keys for GitLab

```bash
ssh-keygen -t ecdsa -C ""
```

`~/.ssh/config`
```text
# Private GitLab instance
Host <your_usernames>.git.icr.ac.uk
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_ecdsa
```

### Using the GitLab repository for your project

```bash
git init --initial-branch=main
git remote add origin git@git.icr.ac.uk:ralcraft/biomarkers_project.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
```

### Working with Branches

```bash
git branch experiment
git checkout experiment
echo "# Testing a new analysis" > test.txt
git add test.txt
git commit -m "Add test analysis file"
git checkout main
git merge experiment
# To merge in changes from main
git pull origin main
git merge origin/main
# Resolve conflicts if needed
git push
```

### Collaborating with Others

```bash
# Clone a repository (example)
git clone https://git.icr.ac.uk/yourusername/biomarkers_project.git
# Pull latest changes
git pull
# Push your changes
git push
```

---

## Homework

- Practice basic Git commands on your project
- Try creating and merging branches
- Set up a remote repository and push your changes
- Review the version control section in The Turing Way handbook

---

## Reflection

- How does version control help you track changes and collaborate?
- What challenges did you encounter with branching or merging?
- How will you use Git in your future research projects?

---

*Complete these tasks before the next session to build confidence with version control and collaboration tools.*