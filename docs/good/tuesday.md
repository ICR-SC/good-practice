# Tuesday Session Summary (For Researchers)

## What We Covered

- Introduction to version control and why it matters for research
- Setting up Git and configuring your identity
- Initializing a repository and tracking changes
- Basic Git commands: `git add`, `git commit`, `git status`, `git log`
- Creating and switching branches for collaborative work
- Merging branches and resolving merge conflicts
- Using GitHub and ICR GitLab for remote collaboration
- Integrating Git with VSCode and GitHub Desktop
- Best practices for team coding and project management

## Key Takeaways

- Version control helps you track changes, collaborate, and ensure reproducibility
- Branching and merging are essential for team workflows
- Remote repositories (GitHub, GitLab) enable sharing and backup
- Resolving merge conflicts is a normal part of collaboration
- VSCode and GitHub Desktop make Git easier to use for beginners

## Homework

- Practice basic Git commands on your project
- Try creating and merging branches
- Set up a remote repository and push your changes
- Review the version control section in The Turing Way handbook

---

*This summary provides a quick reference to the main skills and concepts introduced in Tuesday's session.*

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

```bash
# Configure git
git config --global user.name "Your Name"
git config --global user.email "your.email@domain.com"

# Initialize repository
git init

# Add and commit files
git add README.md
git commit -m "Initial commit"

# Create and switch branches
git branch feature-branch
git checkout feature-branch

# Merge branches
git checkout main
git merge feature-branch

# Clone repository
git clone <repo_url>

# Push to remote
git remote add origin <repo_url>
git push -u origin main
```

## Merge Conflict Demo

- **Resolving Merge Conflicts:**
  https://book.the-turing-way.org/reproducible-research/vcs/vcs-conflicts.html
  - Step-by-step guide to understanding and resolving merge conflicts in Git.

## Additional Reading

- **Why Version Control Matters:**
  https://www.nature.com/articles/d41586-019-02035-0

- **Collaborative Coding Best Practices:**
  https://www.turing.ac.uk/research/research-projects/best-practices-collaborative-coding

---

*This resource list supports the Tuesday session and provides links for further exploration and practice.*

# Tuesday Homework: Version Control Practice

## Practice Tasks

- Practice basic Git commands in your project:
  - `git init` (initialize repository)
  - `git add <file>` (stage changes)
  - `git commit -m "message"` (save changes)
  - `git status` (check repository status)
  - `git log` (view commit history)

- Create and switch branches:
  - `git branch experiment`
  - `git checkout experiment`
  - Make a change, commit it, and merge back to main

- Try resolving a merge conflict (optional):
  - Follow the steps from today's merge conflict demo

- Set up a remote repository (GitHub or ICR GitLab):
  - `git remote add origin <repo_url>`
  - `git push -u origin main`

## Reflection

- How does version control help you track changes and collaborate?
- What challenges did you encounter with branching or merging?
- How will you use Git in your future research projects?

---

*Complete these tasks before the next session to build confidence with version control and collaboration tools.*
