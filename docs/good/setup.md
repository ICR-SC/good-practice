# 5-Session Coding Good Practices Course
## Prerequisites and Setup Guide

*Complete these setup steps before the first session to ensure a smooth learning experience.*  
*If you have any problems, please contact the RSE team for help!*

---

## Overview

This course will teach you coding good practices for reproducible research referencing The Turing Way framework. To participate fully, you'll need several tools installed and accounts configured. Please complete all setup steps below.

For any of the elements that you do not have access to, you can go back and do the session again following the recording, or the RSE team will help you in a drop-in session in the RSE office.  

The summary of the requirements is broken down for each day, with links to fuller instructions below.

---

## Monday's Session
- [Install VSCode]()
- [Access a terminal]()
- [Have an HPC Alma account]()
- [Optionally set up Alma ssh keys]()
- [Optionally setup remote-ssh for VSCode](https://code.visualstudio.com/docs/remote/ssh) [AlmaCookBook link](https://almacookbook.github.io/ides/remote/)


## Tuesday's Session
- [Install VSCode]()
- [Install and configure Git]()
- [Install GitHub Desktop (Windows/Mac)]()
- [Set up GitLab access (SSO)]()
- [Set up GitHub access (institutional account)]()

---

## 💻 Software Installation

### 1. Visual Studio Code (VSCode)
**Purpose:** Code editor for Monday's session and throughout the course

**Installation:**
- **Windows/Mac/Linux:** Download from [https://code.visualstudio.com/](https://code.visualstudio.com/)
- **Installation notes:** Accept all default options during installation
- **Test:** Open VSCode and verify it launches successfully

**VSCode Extensions:**
All essential and recommended extensions will be demonstrated and installed during Monday's session and assigned as homework. No need to pre-install extensions.

**Pre-Course Requirement:**
- [ ] VSCode opens successfully and you can access the Extensions panel

### 2. Git Version Control
**Purpose:** Essential for Tuesday's version control session

**Installation:**
- **Windows:** Download Git for Windows from [https://git-scm.com/download/win](https://git-scm.com/download/win)
  - ✅ **Important:** During installation, select "Git Bash Here" and "Git GUI Here"
  - ✅ **Important:** Choose "Use Git from the Windows Command Prompt"
- **Mac:** Install using Homebrew: `brew install git` or download from [https://git-scm.com/download/mac](https://git-scm.com/download/mac)
- **Linux:** Install via package manager: `sudo apt install git` (Ubuntu/Debian) or `sudo yum install git` (CentOS/RHEL)

**Test Installation:**
```bash
git --version
```
You should see output like: `git version 2.x.x`

### 3. GitHub Desktop
**Purpose:** Visual Git interface for Tuesday's session

**Installation:**
- **Windows/Mac:** Download from [https://desktop.github.com/](https://desktop.github.com/)
- **Linux:** GitHub Desktop is not officially supported on Linux. Use command line Git instead.
- **Installation notes:** Accept all default options

**Test:** Open GitHub Desktop and verify it launches successfully

**Note:** GitHub Desktop setup and configuration will be covered in Tuesday's session. For now, just ensure it installs and opens correctly.

### 4. Python Environment (Anaconda/Miniconda) + JupyterLab
**Purpose:** Python programming for Wednesday's session, environment management for Friday, and interactive analysis throughout

**Recommended Installation Option 1: Anaconda (Full Installation)**
- **All platforms:** Download from [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
- **Includes:** Python, conda, JupyterLab, and 250+ data science packages
- **Size:** ~3GB download, ~5GB installed
- **Best for:** Users who want everything pre-installed

**Recommended Installation Option 2: Miniconda (Minimal Installation)**
- **All platforms:** Download from [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- **Includes:** Python and conda package manager only
- **Size:** ~400MB download, ~1GB installed
- **Best for:** Users who prefer to install packages as needed

**Installation Steps:**

**For Anaconda:**
1. Download the installer for your operating system
2. **Windows:** Run the installer and check "Add Anaconda to PATH" during installation
3. **Mac/Linux:** Follow the installer prompts, allow it to initialize conda
4. **All platforms:** Choose "Install for all users" if you have admin rights

**For Miniconda:**
1. Download the installer for your operating system
2. **Windows:** Run the installer and check "Add conda to PATH" during installation
3. **Mac/Linux:** Run the installer script and allow it to initialize conda
4. After installation, install JupyterLab:
   ```bash
   conda install -c conda-forge jupyterlab
   ```

**Installation Notes:**
- ✅ **Windows:** Check "Add Anaconda/Miniconda to PATH" during installation (crucial for command line access)
- ✅ **All platforms:** Allow the installer to initialize conda for your shell
- ✅ **Mac users:** You may need to restart your terminal after installation

**Post-Installation Setup:**
```bash
# Update conda to latest version
conda update conda

# Create your research environment using the step-by-step recipe (see Friday session):
conda create --name biomarker-analysis python=3.9
conda activate biomarker-analysis
conda install pandas=1.5.3 numpy=1.24.3 matplotlib=3.7.1 scikit-learn=1.3.0 jupyter=1.0.0
conda install r-base=4.3.1 r-tidyverse=2.0.0 r-ggplot2=3.4.2 git=2.40.1 pip=23.1.2
pip install umap-learn==0.5.3

# Export your environment for sharing (recommended):
conda env export --no-builds > biomarker-env.yml

# (Optional) Install Docker for containerized reproducibility
# Docker installation will be demonstrated in Friday's session

# Verify JupyterLab installation
jupyter lab --version
```

**Test Installation:**
```bash
# Test conda
conda --version

# Test Python
python --version

# Test JupyterLab (optional - will be covered in Wednesday's session)
jupyter lab --version

# Start JupyterLab (optional test - should open in browser)
jupyter lab
```

**Expected Output:**
- `conda --version` should show: `conda 23.x.x` or similar
- `python --version` should show: `Python 3.x.x`
- `jupyter lab --version` should show: `4.x.x` or similar (if installed)
- `jupyter lab` should open a web browser with JupyterLab interface (if installed)

**Troubleshooting:**
- **"conda not found"**: Restart terminal/command prompt after installation
- **PATH issues**: Add conda installation directory to your system PATH
- **Permission errors**: Run installer as administrator (Windows) or use `sudo` (Mac/Linux)

### 5. R and RStudio
**Purpose:** Statistical analysis for Thursday's session

**Install R first:**
- **All platforms:** Download from [https://cran.r-project.org/](https://cran.r-project.org/)
- Choose the latest version for your operating system

**Then install RStudio:**
- **All platforms:** Download RStudio Desktop from [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)

**Test Installation:**
- Open RStudio
- In the console, type: `R.version.string`
- Verify R version appears

**Note:** Detailed R configuration and package setup will be covered in Thursday's session and homework.

---

## 🔐 Account Setup and Authentication

### 1. GitLab Access (Primary platform for the course)
**Purpose:** Main version control platform for Tuesday's session

**Setup Steps:**
1. **No account creation needed** - uses institutional SSO
2. **Access the platform:** Navigate to your institutional GitLab URL
3. **Login:** Use your institutional credentials (same as email/network login)
4. **Verify access:** You should see the GitLab dashboard

**Configuration Note:** Detailed GitLab setup, repository creation, and collaboration workflows will be covered in Tuesday's session.

**If you have trouble:**
- Ensure you're connected to the institutional network or VPN
- Contact IT support if SSO authentication fails

### 2. GitHub Access (Institutional account)
**Purpose:** Alternative platform knowledge and broader research community access

**Setup Steps:**
1. **Request access:** Send an email to `schelpdesk@icr.ac.uk` with:
   ```
   Subject: GitHub Enterprise Account Request
   
   Dear ICR Help Desk,
   
   I am participating in the Coding Good Practices course and need access to the institutional GitHub Enterprise account.
   
   My institutional email: [your.email@icr.ac.uk]
   My preferred GitHub username: [desired-username]
   
   Thank you,
   [Your name]
   ```

2. **Wait for invite:** You'll receive an invitation email (usually within 1-2 business days)
3. **Accept invitation:** Follow the link in the email to complete account setup
4. **Verify access:** Log in to the institutional GitHub instance

**Note:** This setup is optional for the core course sessions but recommended for ongoing research collaboration. GitHub workflows and advanced features will be covered in Tuesday's session.

---

## ⚙️ Configuration Steps

### 1. Configure Git Identity
**Purpose:** Essential for version control sessions

**Setup Commands:**
```bash
# Set your name (use your real name for research collaboration)
git config --global user.name "Your Full Name"

# Set your email (use institutional email)
git config --global user.email "your.email@icr.ac.uk"

# Set default branch name to 'main'
git config --global init.defaultBranch main

# Configure line ending handling (important for cross-platform collaboration)
# Windows users:
git config --global core.autocrlf true

# Mac/Linux users:
git config --global core.autocrlf input
```

**Verify Configuration:**
```bash
git config --global --list
```

**Note:** Advanced Git configuration, SSH key setup, and authentication will be covered in Tuesday's session. This basic identity configuration is sufficient to get started.

### 2. Set Up Authentication Tokens

**Note:** Authentication token setup will be covered in detail during Tuesday's session. The basic configuration below is sufficient for getting started.

#### For GitLab (if needed for command line access):
1. **Log in to GitLab** via SSO
2. **Go to User Settings** → Access Tokens
3. **Create Personal Access Token:**
   - Name: "Course Development Token"
   - Expiration: Set to after course completion
   - Scopes: `read_repository`, `write_repository`
4. **Save the token** securely (you won't see it again)

#### For GitHub (after account approval):
1. **Log in to institutional GitHub**
2. **Go to Settings** → Developer settings → Personal access tokens → Tokens (classic)
3. **Generate new token:**
   - Note: "Course Development Token"
   - Expiration: Set to after course completion
   - Scopes: `repo`, `workflow`
4. **Save the token** securely

**Important:** Never share or commit these tokens to repositories! Detailed security practices will be covered in Tuesday's session.

---

## 🧪 Testing Your Setup

### Complete System Test
Run these commands to verify your basic setup is working:

```bash
# Test VSCode (should open VSCode)
code --version

# Test Git
git --version

# Test Python and Conda
python --version
conda --version

# Test R (in R console or RStudio)
# R.version.string

# Create a test directory
mkdir coding-course-test
cd coding-course-test

# Initialize Git repository
git init

# Create a test file
echo "# Test Repository" > README.md

# Add and commit
git add README.md
git commit -m "Test commit"

# Check status
git status

# Clean up
cd ..
rm -rf coding-course-test
```

**Additional Tests (Optional):**
```bash
# Test JupyterLab (if installed)
jupyter lab --version

# Test VSCode Extensions (will be covered in Monday's homework)
code --list-extensions

# Test Jupyter integration (will be covered in Wednesday's session)
jupyter lab --generate-config
```

If the basic commands work without errors, you're ready for the course! Advanced configurations and reproducibility practices will be covered in each session's homework.

---

## 📁 Recommended Folder Structure

Create this folder structure before the course starts:

```
~/research-course/
├── projects/          # For your course projects
├── examples/          # For following along with examples
└── resources/         # For course materials and references
```

**Commands to create:**
```bash
mkdir -p ~/research-course/{projects,examples,resources}
```

---

## 🆘 Troubleshooting Common Issues

### Git and SSH Issues
- **"Permission denied" for SSH**: Check that SSH keys are properly set up and added to services
- **SSH key not working**: Verify public key is correctly copied to GitLab/GitHub/HPC
- **Multiple SSH keys**: Use SSH config file to manage different keys
- **HPC connection issues**: Contact ICR IT support for account access problems

### Python/Conda Issues
- **"conda not found"**: Restart terminal or source your shell profile
- **Permission errors**: Don't use `sudo` with conda, check installation directory permissions
- **Environment conflicts**: Use `conda clean --all` to clear package cache

### VSCode Issues
- **Extensions not installing**: Check internet connection and VS Code marketplace access
- **Terminal not working**: Restart VS Code after installing Git

### Platform Access Issues
- **GitLab SSO fails**: Verify VPN connection and institutional credentials
- **GitHub access denied**: Ensure you've received and accepted the invitation email

---

## 📞 Getting Help

**Before the course:**
- **Technical issues:** Contact `schelpdesk@icr.ac.uk`
- **Course questions:** Contact the course instructors
- **Installation problems:** Try the troubleshooting steps above first

**During the course:**
- Raise your hand for immediate help
- Use the shared chat/document for questions
- Don't hesitate to ask - we're here to help!

---

## 📚 Optional Preparation

If you want to get a head start:

1. **Browse The Turing Way:** [https://book.the-turing-way.org/](https://book.the-turing-way.org/)
2. **Review basic command line:** [Software Carpentry Unix Shell lesson](https://swcarpentry.github.io/shell-novice/)
3. **Python refresher:** [Software Carpentry Python lesson](https://swcarpentry.github.io/python-novice-inflammation/)
4. **R refresher:** [Software Carpentry R lesson](https://swcarpentry.github.io/r-novice-gapminder/)

---

## ✅ Final Checklist

Before Monday's session, confirm:

**Essential Requirements:**
- [ ] VSCode opens and you can create/edit files
- [ ] Git commands work in terminal
- [ ] Python and conda commands work
- [ ] R and RStudio open and function
- [ ] You can log in to institutional GitLab via SSO
- [ ] You've configured Git with your name and email
- [ ] You've created the recommended folder structure

**Additional Checks (Optional but Recommended):**
- [ ] VSCode Extensions panel is accessible (detailed setup in Monday's homework)
- [ ] GitHub Desktop launches successfully
- [ ] JupyterLab starts and opens in browser (`jupyter lab`)
- [ ] You can connect to HPC cluster: `ssh username@alma.icr.ac.uk`
- [ ] SSH keys are set up and working (no password prompts)

**Notes:**
- VSCode extension configuration will be covered in Monday's homework
- Advanced Git workflows and authentication will be covered in Tuesday's session  
- Jupyter notebook setup will be covered in Wednesday's session
- R package management will be covered in Thursday's session
- Environment management and sharing via conda recipe (not manual YAML) and Docker will be covered in Friday's session

**If any essential requirement above fails, please seek help before the course begins!**

---

*This setup ensures everyone can participate in all five 60-minute live sessions. Detailed configurations and advanced setups are part of each session's homework, allowing us to focus on core concepts during the live sessions while providing comprehensive hands-on practice afterward.*