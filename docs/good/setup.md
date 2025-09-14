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
- [**Install VSCode**](#install-vscode)
- [**Access a terminal**](#access-a-terminal)
- [**Have an HPC Alma account**](#have-an-hpc-alma-account)
- [**Optionally set up Alma ssh keys**](#set-up-alma-ssh-keys)
- [**Optionally setup remote-ssh for VSCode**](#setup-remote-ssh-for-vscode)


## Tuesday's Session
- [Install VSCode](#install-vscode)
- [**Install and configure Git**](#install-and-configure-git)
- [**Install GitHub Desktop (Windows/Mac)**](#install-github-desktop)
- [**Set up (internal) GitLab access**](#set-up-gitlab-access)
- [**Set up GitHub access (institutional account)**](#set-up-github-access)

## Wednesday's Session
- [Install VSCode](#install-vscode)
- [Install Python](#install-python)
- [Install and configure Git](#install-and-configure-git)
- [Set up GitLab access (SSO)](#set-up-gitlab-access)

## Thursday's Session
- [Install VSCode](#install-vscode)
- [Install and configure Git](#install-and-configure-git)
- [Set up GitLab access](#set-up-gitlab-access)
- [**R and RStudio**](#r-and-rstudio)

## Friday's Session
- [Install VSCode](#install-vscode)
- [**Install Conda (Anaconda)**](#install-conda-anaconda)
- [**Install Docker**](#install-docker)

---

## Software Installation
For all software installations at the ICR it is recommended to check with servicedesk@icr.ac.uk. There has beeen a process of centralising installations for Windows 11 machines, and the installations ought to be available through Company POrtal. Always check this first as when installed here you do not need admin rights. Otherwise you will probably need assistance for any installs. Mac users will need admin rights for most installs but it is changing rapidly so please check. In general the links are given to open source software installs but first check Company Portal and ask servicedesk@icr.ac.uk

---  

### Install VSCode
#### Windows
For Windows The application can be installed from Company Portal.  
<img src="../imgs/vscode-image.png" alt="VSCode" width="400"/>

#### Mac
For Mac the application can be downloaded and installed from here [code.visualstudio.com/Download](https://code.visualstudio.com/Download).  
Choose the User Installer for your system (Apple Silicon or Intel).

---  

### Access a terminal
#### Windows
Use PowerShell or Command Prompt. But install WSL2 (Windows Subsystem for Linux) for a better experience. This can be installed from Windows Store:  
<img src="../imgs/wsl2-image.png" alt="WSL2" width="400"/>  

Alternatively you can use GitBash for a linux-like terminal experience. This is also available on company portal.  
<img src="../imgs/git-image.png" alt="GitHub Desktop" width="400"/>

#### Mac
Use the built-in Terminal application.

---  

### Have an HPC Alma account
[Alma Pages on Nexus](https://nexus.icr.ac.uk/strategic-initiatives/sc/hpc/Pages/Getting-Started.aspx) have information on getting started with Alma, or contact [schelpdesk.icr.ac.uk](mailto:schelpdesk.icr.ac.uk).

---  

### Set up Alma ssh keys
[ALmaCookBook instructions](https://almacookbook.github.io/first_steps/#1-setting-up-ssh-key-for-alma-credits-to-vscode-and-blissweb-on-stackoverflow)

---  

### Setup remote-ssh for VSCode
[code.visualstudio.com/docs/remote/ssh](https://code.visualstudio.com/docs/remote/ssh)  
[AlmaCookBook link](https://almacookbook.github.io/ides/remote/)  

---  

### Install and configure Git
#### Windows
Install Git from the Company Portal:  
<img src="../imgs/git-image.png" alt="Git-Install" width="400"/>

#### Mac
Use HomeBrew, the mac store, or download from [git-scm.com](https://git-scm.com/download/mac).

---  

### Install GitHub Desktop
#### Windows
For Windows The application can be installed from Company Portal.  
<img src="../imgs/github-desktop-image.png" alt="GitHub Desktop" width="400"/>

#### Mac
For Mac the application can be downloaded and installed from here [desktop.github.com](https://desktop.github.com/).

---  

### Set up GitLab access
We will walk through this in the *git* session: [docs.gitlab.com/user/ssh](https://docs.gitlab.com/user/ssh/)

### Set up GitHub access
Send an email to [schelpdesk.icr.ac.uk](mailto:schelpdesk.icr.ac.uk) to request an institutional GitHub account.  You will receieve an invite to your icr email address.  

---  

### Install Python

#### Windows
For Windows The application can be installed from Company Portal.  
<img src="../imgs/code-image.png" alt="VSCode" width="400"/>

#### Mac
Python should be pre-installed. You can check by running `python3 --version` in the terminal. If not, install it from [python.org](https://www.python.org/downloads/macos/).

---  

### R and RStudio
#### Windows
<img src="../imgs/code-image.png" alt="Code" width="400"/>

#### For WSL2
To use RStudio from WSL2 as if native install it in linux. This command worked for me:  
`sudo snap install rstudio --classic`

#### Mac
Install R from [CRAN](https://cran.r-project.org/bin/macosx/) and RStudio from [RStudio](https://www.rstudio.com/products/rstudio/download/#download).

---  

### Install Conda (Anaconda)
Install Anaconda from the Company Portal:  
<img src="../imgs/anaconda-image.png" alt="Anaconda" width="400"/>

#### Mac
Install Anaconda from [anaconda.com](https://www.anaconda.com/products/distribution#download-section):

---  

### Install Docker
#### Windows
For Windows The application can be installed from Company Portal.  
<img src="../imgs/docker-image.png" alt="Docker" width="400"/>

#### Mac
For Mac the application can be downloaded and installed from here [docker.com](https://www.docker.com/products/docker-desktop/).


