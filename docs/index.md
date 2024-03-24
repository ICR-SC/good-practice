# Research Software Good Practice

## Index

``` mermaid
graph LR
  K1[Key: External resource]  --> K2[Key: Internal article];
  K2 --> K3[Internal how-to guides];
  K3 --> K4[Internal Training];
  style K1 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff
  style K2 fill:#ffcce6,stroke:#ff6600,stroke-width:2px,color:#4d4dff
  style K3 fill:#b3ffb3,stroke:#ff6600,stroke-width:2px,color:#4d4dff
  style K4 fill:#ffff99,stroke:#ff6600,stroke-width:2px,color:#4d4dff
```

Click on the resources below or go to the [full index](index.md) for more information.

``` mermaid
graph TD  
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
  EB --> |Python| PA[A python package];
  PA --> PB[A python webapp];
  EB --> |R| RA[An R package];
  RA --> RB[An R-shiny webapp];
  A --> TA{Tools};
  click K1 "https://www.github.com" "This is a tooltip for a link"
  style A fill:#ff3399,stroke:#333,stroke-width:1px,color:#99ff99
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





