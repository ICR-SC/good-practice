# Research Software Good Practice

## Index


``` mermaid
graph TD
  A[Reasearch Software Good Practice] --> B{Beginner?};
  B -->|Yes| C[Using version control];
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
  PA[Python] --> PB{Beginner?};
  click B "https://www.github.com" "This is a tooltip for a link"
  style A fill:#f9f,stroke:#333,stroke-width:4px
  style B fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
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





