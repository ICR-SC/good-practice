# Research Software Good Practice

Research software development differs from standard software development [in some core ways](about.md). This guide aims to provide a set of good practices that can be applied to research software development to ensure that the software is of high quality, maintainable, reusable and importantly - reproducible.

Click on the resources below for more information, or browse the resources in the sidebar.

**Keys:**  
``` mermaid
flowchart LR
  EX[External resource]  --- IN[Internal article];
  IN --- HOW[Internal how-to guides];
  HOW --- TRAIN[Internal Training];  
  style EX fill:#bbf,stroke:#f66,stroke-width:1px,color:#33334d
  style IN fill:#ffcce6,stroke:#ff6600,stroke-width:1px,color:#33334d
  style HOW fill:#b3ffb3,stroke:#ff6600,stroke-width:1px,color:#33334d
  style TRAIN fill:#ffff99,stroke:#ff6600,stroke-width:1px,color:#33334d
```

``` mermaid
flowchart TD  
  A[Reasearch Software Good Practice] --> B{Processes};
  B -->|Beginner| C[Using version control];
  C --> D[Using virtual environments];
  D --> E[Writing clean, readable code];
  E --> F[Writing tests];
  B ---->|Intermediate| F;
  F --> G[Documenting the software];
  G --> H[Using continuous integration];
  H --> I[Using a package manager];
  I --> J[Using a code review process];
  J --> K[Is it FAIR?];
  B ---->|Advanced| K;
  A --> EB{Languages};
  EB --> |Python| PA[Python overview];
  PA --> PEP8[Python language standards];  
  PEP8 --> PINTRO1[Intro to python in person];
  PINTRO1 --- PINTRO2[Intro to python online];
  PINTRO1 --> PC[A python package];
  PC --> PD[A python webapp];
  EB --> |R| RA[R language standards];
  RA --> RB[Intro to R];
  RB --> RC[An R package];
  RC --> RD[An R-shiny webapp];
  A --> TA{Tools};
  style A fill:#ff3399,stroke:#333,stroke-width:1px,color:#99ff99
  click A "https://icr-rse-group.github.io/good-practice/about/" "RS Good Practice"
  style PA fill:#ffcce6,stroke:#ff6600,stroke-width:1px,color:#33334d
  click PA "https://icr-rse-group.github.io/good-practice/good/python/" "Python Overview"
  style PEP8 fill:#bbf,stroke:#f66,stroke-width:1px,color:#33334d
  click PEP8 "https://peps.python.org/pep-0008/" "PEP8"
  style PINTRO1 fill:#ffff99,stroke:#ff6600,stroke-width:1px,color:#33334d
  click PINTRO1 "https://training.icr.ac.uk/coursed.php?course=544" "Intro to Python"
  style PINTRO2 fill:#ffff99,stroke:#ff6600,stroke-width:1px,color:#33334d
  click PINTRO2 "https://training.icr.ac.uk/coursed.php?course=1189" "Intro to Python"
  style PC fill:#b3ffb3,stroke:#ff6600,stroke-width:1px,color:#33334d
  style PD fill:#b3ffb3,stroke:#ff6600,stroke-width:1px,color:#33334d
  style RA fill:#ffcce6,stroke:#ff6600,stroke-width:1px,color:#33334d
  style RB fill:#ffff99,stroke:#ff6600,stroke-width:1px,color:#33334d
  style RC fill:#b3ffb3,stroke:#ff6600,stroke-width:1px,color:#33334d
  style RD fill:#b3ffb3,stroke:#ff6600,stroke-width:1px,color:#33334d
  click EB "https://cran.r-project.org/web/packages/devtools/readme/README.html" "R packaging good practice"
```

https://squidfunk.github.io/mkdocs-material/reference/diagrams/
https://mermaid.js.org/syntax/gitgraph.html

### Project Processes

- Using version control
- Using virtual environments
- Writing clean, readable code
- Writing tests
- Documenting the software (https://realpython.com/python-project-documentation-with-mkdocs/)
- Is it FAIR https://www.researchsoft.org/blog/2024-03/
- Using continuous integration
- Using a package manager
- Using a code review process

---  

### Languages
- Python
- R
- Matlab
- C++
- C#

---  

### Demonstration projects
- A python package  
- A python streamlit (web) app  
- An R package  
- An R-shiny webapp  

---  

### Mini articles

- Defining the scope of the project through tests  
- Demonstrating proof of correctness through tests  
- The 3 tier user model  
- Developing with containers  
- Developing in reproducible environments  
- https://coderefinery.github.io/reproducible-research/  

---  

### In-house training  

- Using vscode modules  

---  

### Resources / References  

https://betterscientificsoftware.github.io/python-for-hpc/python-for-hpc/
https://coderefinery.org/
https://www.universe-hpc.ac.uk/resources/training-material/#course-website
https://github.com/UNIVERSE-HPC/course-material
https://code.visualstudio.com/docs/python/python-tutorial
https://learn.microsoft.com/en-us/
https://www.software.ac.uk/guide/how-make-your-script-ready-publication
http://www.archer.ac.uk/training/courses/
https://learn.microsoft.com/en-us/training/paths/beginner-python/
https://code.visualstudio.com/learn/educators/python

email from streamlit:
https://www.youtube.com/watch?v=FOULV9Xij_8

Clickable scatter: https://community.plotly.com/t/is-it-possible-to-add-a-hyperlink-to-data-points-in-a-scatter-plot/28343/5





