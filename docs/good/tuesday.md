# Tuesday Session Summary (For Researchers)

## Summaty

- Introduction to version control and why it matters for research
- Setting up Git and configuring your identity
- Initializing a repository and tracking changes
- Basic Git commands: `git add`, `git commit`, `git status`, `git log`
- Creating and switching branches for collaborative work
- Merging branches and resolving merge conflicts
- Using GitHub and ICR GitLab for remote collaboration
- Integrating Git with VSCode and GitHub Desktop
- Best practices for team coding and project management



---

# Tuesday Resources: Version Control and Collaboration in Research Coding

## Key References

- **The Turing Way: Version Control Guide:**
  https://book.the-turing-way.org/reproducible-research/vcs
  - Essential reading for understanding version control in reproducible research.

- **The Turing Way Handbook (General):**
  https://the-turing-way.netlify.app/
  - Principles of reproducible, ethical, and collaborative research.

## Institutional Resources

- **ICR GitLab:**
  - [ICR GitLab](https://gitlab.icr.ac.uk/) *(internal access required)*
  - Guides for project setup, collaboration, and best practices.

- **GitHub:**
  https://github.com/
  - Public repositories, collaboration, and open science.

## Git Basics and Tutorials

- **Git Official Documentation:**
  https://git-scm.com/doc
  - Getting started, commands, and workflows.

- **GitHub Desktop:**
  https://desktop.github.com/
  - GUI for managing repositories and collaboration.

- **VSCode Git Integration:**
  https://code.visualstudio.com/docs/sourcecontrol/overview
  - Using Git within VSCode for version control and collaboration.

## Example Commands Used in Session

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
- [**GitHub organisation:**]) https://github.com/enterprises/icr/organizations)  
- [**ICR GitLab:** ](https://git.icr.ac.uk/)  

### Setting up keys for GitLab
```bash
ssh-keygen -t ecdsa -C ""
```
` ~/.ssh/config`
```text
# Private GitLab instance
Host <your_usernames>.git.icr.ac.uk
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_ecdsa
```

### Using the gitlab repository for your project
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
