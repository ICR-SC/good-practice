# Daily Reference Guide
## 5-Session Coding Good Practices Course

*Quick reference for key concepts, commands, and workflows from each session*

---

## 📚 **Course Overview**

Based on **The Turing Way** framework for reproducible, ethical, and collaborative research. Each day builds essential skills for modern computational research.

**Course Goal:** Transform your research workflows to be trustworthy, shareable, and impactful.

---

## 📅 **Monday: Command Line & VSCode**
*Foundation - Professional Development Environment*

### **Key Concepts:**
- **Reproducible project structure** following Turing Way guidelines
- **Command line efficiency** for research workflows
- **Professional development environment** setup
- **Cross-platform compatibility** (local + HPC)

### **Essential Commands:**
```bash
# Navigation and file management
pwd                           # Show current directory
ls -la                        # List files with details
mkdir -p project/{data,src}   # Create nested directories
cd project                    # Change directory
tree                          # Show directory structure

# Project setup
touch README.md               # Create files
echo "content" > file.txt     # Write to file
cp source dest                # Copy files
mv old new                    # Move/rename files

# HPC access
ssh username@alma.icr.ac.uk   # Connect to ICR cluster
scp file user@host:path       # Transfer files
```

### **VSCode Essential Extensions:**
- **Python** (Microsoft) - Python development
- **R** (REditorSupport) - R programming  
- **Jupyter** (Microsoft) - Notebook integration
- **GitLens** (GitKraken) - Enhanced Git
- **Markdown All in One** - Documentation
- **YAML** (Red Hat) - Configuration files
- **Rainbow CSV** - Data file viewing
- **Docker** (Microsoft) - Container support

### **Standard Project Structure:**
```
research-project/
├── data/
│   ├── raw/           # Original, immutable data
│   ├── processed/     # Cleaned data
│   └── external/      # Reference data
├── src/
│   ├── python/        # Python analysis scripts
│   ├── r/             # R statistical scripts
│   └── utils/         # Utility functions
├── results/
│   ├── figures/       # Generated plots
│   ├── tables/        # Analysis outputs
│   └── models/        # Trained models
├── docs/
│   ├── reports/       # Analysis reports
│   └── protocols/     # Methods documentation
├── environment/       # Computational environments
├── config/           # Configuration files
├── README.md         # Project overview
└── .gitignore       # Git exclusions
```

### **Key Takeaways:**
- Consistent project structure enables collaboration
- Command line skills transfer across all computing environments
- Professional setup saves time and prevents errors
- Documentation from day one prevents future confusion

---

## 📅 **Tuesday: Git & Collaboration**
*Version Control & Team Science*

### **Key Concepts:**
- **Version control** for tracking research decisions
- **Collaborative workflows** for team science
- **GitLab vs GitHub** - institutional vs external platforms
- **Visual Git tools** for non-technical team members

### **Essential Git Commands:**
```bash
# Setup and configuration
git config --global user.name "Your Name"
git config --global user.email "email@icr.ac.uk"
git config --global init.defaultBranch main

# Basic workflow
git init                      # Initialize repository
git status                    # Check current state
git add filename             # Stage files
git add .                    # Stage all changes
git commit -m "message"      # Commit with message
git log --oneline            # View commit history

# Branching and collaboration
git branch                   # List branches
git checkout -b feature      # Create and switch branch
git checkout main            # Switch to main branch
git merge feature            # Merge branch
git branch -d feature        # Delete branch

# Remote repositories
git remote add origin URL    # Add remote repository
git push -u origin main      # Push to remote
git pull                     # Get latest changes
git clone URL               # Copy repository
```

### **Collaborative Workflow:**
1. **Create feature branch** for new analysis
2. **Make changes** and commit with clear messages
3. **Push branch** to GitLab/GitHub
4. **Create merge request** for peer review
5. **Review and discuss** changes
6. **Merge** after approval
7. **Delete feature branch** and sync

### **GitHub Desktop Alternative:**
- Visual interface for Git operations
- Multi-project overview dashboard
- Ideal for wet lab scientists and clinical researchers
- Integrates with command line workflows

### **SSH Key Setup:**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "email@icr.ac.uk"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key (add to GitLab/GitHub)
cat ~/.ssh/id_ed25519.pub
```

### **Key Takeaways:**
- Version control creates complete audit trail of research decisions
- Branching enables safe experimentation with different approaches
- Peer review through merge requests improves research quality
- Both command line and visual tools support different team preferences

---

## 📅 **Wednesday: Python & Ethics**
*Ethical & Reproducible Data Science*

### **Key Concepts:**
- **Clean, testable code** for scientific validity
- **Ethical AI practices** including bias detection
- **Comprehensive testing** for research reliability
- **Reproducible analysis pipelines** with configuration management

### **Python Best Practices:**
```python
# Professional function structure
def analyze_biomarkers(data: pd.DataFrame, 
                      biomarkers: List[str],
                      method: str = "pearson") -> Dict[str, float]:
    """
    Analyze biomarker correlations with bias detection.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Patient data with biomarker measurements
    biomarkers : List[str]
        Column names of biomarkers to analyze
    method : str, default="pearson"
        Correlation method to use
        
    Returns:
    --------
    Dict[str, float]
        Correlation results with bias scores
    """
    logger.info(f"Analyzing {len(biomarkers)} biomarkers")
    
    # Implementation with error handling
    # Bias detection included
    # Statistical validation
    
    return results
```

### **Testing Framework:**
```python
import unittest

class TestBiomarkerAnalysis(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.test_data = create_synthetic_data()
    
    def test_reproducibility(self):
        # Test same inputs give same outputs
        result1 = analyze_biomarkers(self.test_data, ["marker1"])
        result2 = analyze_biomarkers(self.test_data, ["marker1"])
        self.assertEqual(result1, result2)
    
    def test_bias_detection(self):
        # Test bias detection works
        biased_data = introduce_bias(self.test_data)
        results = detect_bias(biased_data)
        self.assertGreater(results['bias_score'], 0.1)
```

### **Ethical AI Checklist:**
- **Bias Detection**: Test for demographic disparities
- **Fairness Metrics**: Assess performance across groups
- **Privacy Protection**: Implement data anonymization
- **Transparency**: Document all analytical decisions
- **Validation**: Test assumptions and edge cases
- **Interpretability**: Ensure results can be explained

### **Configuration Management:**
```yaml
# analysis_config.yaml
data_file: "patient_data.csv"
biomarkers: ["marker1", "marker2", "marker3"]
analysis_method: "pearson"
random_seed: 42
bias_threshold: 0.1
privacy_protection: true
```

### **Key Takeaways:**
- Testing ensures scientific validity, not just code correctness
- Ethical considerations must be built into analysis from the start
- Configuration files enable reproducible parameter management
- Clear documentation supports peer review and collaboration

---

## 📅 **Thursday: R & Statistics**
*Statistical Rigor & Reproducible Reporting*

### **Key Concepts:**
- **Rigorous statistical analysis** with proper corrections
- **R Markdown** for reproducible reporting
- **Publication-ready visualizations** following best practices
- **Integration** with Python workflows

### **Statistical Analysis Framework:**
```r
# Professional R function structure
perform_correlation_analysis <- function(data,
                                       biomarker_columns,
                                       method = "pearson",
                                       correction = "BH",
                                       alpha = 0.05) {
  
  # Log analysis parameters
  logger::log_info("Performing {method} correlation with {correction} correction")
  
  # Compute correlations
  cor_matrix <- cor(data[biomarker_columns], method = method, use = "complete.obs")
  
  # Apply multiple testing correction
  p_adjusted <- p.adjust(p_values, method = correction)
  
  # Return comprehensive results
  return(list(
    correlation_matrix = cor_matrix,
    p_values_adjusted = p_adjusted,
    significant_pairs = significant_correlations,
    summary_stats = summary_statistics
  ))
}
```

### **R Markdown Template:**
```markdown
---
title: "Research Analysis Report"
author: "Your Name"
date: "`r Sys.Date()`"
output:
  html_document:
    toc: true
    code_folding: show
params:
  data_file: "data.csv"
  alpha_level: 0.05
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE, warning = FALSE, message = FALSE)
set.seed(42)  # Reproducibility
```

## Analysis Results

```{r analysis}
# Analysis code here - updates automatically
results <- perform_analysis(params$data_file)
```

The analysis found `r sum(results$significant)` significant associations.
```

### **Statistical Best Practices:**
- **Multiple testing correction** (Benjamini-Hochberg recommended)
- **Effect size calculation** (Cohen's d, etc.)
- **Power analysis** for study design
- **Assumption validation** (normality, homoscedasticity)
- **Confidence intervals** alongside p-values

### **Visualization Principles:**
```r
# Publication-ready plot
create_correlation_heatmap <- function(cor_matrix, p_matrix) {
  ggplot(correlation_data, aes(x = var1, y = var2, fill = correlation)) +
    geom_tile() +
    scale_fill_gradient2(low = "blue", high = "red", mid = "white") +
    theme_minimal() +
    labs(title = "Biomarker Correlations",
         subtitle = "Significant correlations marked with *") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}
```

### **Key Takeaways:**
- Multiple testing correction is essential for genomics/biomarker studies
- R Markdown enables automatic report generation
- Statistical assumptions must be validated before analysis
- Publication-ready outputs save time and ensure consistency

---

## 📅 **Friday: Computational Reproducibility**
*Environments & Sustainability*

### **Key Concepts:**
- **Computational environments** for exact reproducibility
- **Multi-language integration** (Python + R + tools)
- **Containerization** for ultimate portability
- **Long-term sustainability** planning

### **Conda Environment Management:**
```bash
# Create project environment
conda create --name biomarker-analysis python=3.9
conda activate biomarker-analysis

# Install packages with specific versions
conda install pandas=1.5.3 numpy=1.24.3 matplotlib=3.7.1
conda install r-base=4.3.1 r-tidyverse r-ggplot2

# Export environment
conda env export > environment/biomarker-env.yml
conda env export --no-builds > environment/biomarker-env-portable.yml

# Recreate environment elsewhere
conda env create -f environment/biomarker-env.yml
```

### **Environment Configuration File:**
```yaml
# biomarker-env.yml
name: biomarker-analysis
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - python=3.9.16
  - pandas=1.5.3
  - numpy=1.24.3
  - r-base=4.3.1
  - r-tidyverse=2.0.0
  - jupyter=1.0.0
  - git=2.40.1
  - pip:
    - umap-learn==0.5.3
```

### **Jupyter Integration:**
```bash
# Jupyter environment with multi-kernel support
conda create --name biomarker-jupyter python=3.9
conda activate biomarker-jupyter
conda install jupyterlab jupyter nb_conda_kernels
conda install r-base r-irkernel  # R kernel for Jupyter

# Start JupyterLab
jupyter lab --port=8888 --no-browser
```

### **Docker for Ultimate Reproducibility:**
```dockerfile
FROM continuumio/miniconda3:latest
WORKDIR /research
COPY environment/biomarker-env.yml .
RUN conda env create -f biomarker-env.yml
SHELL ["conda", "run", "-n", "biomarker-analysis", "/bin/bash", "-c"]
COPY src/ ./src/
COPY config/ ./config/
```

### **Environment Lifecycle Strategy:**
- **Development**: Flexible environment for experimentation
- **Production**: Locked versions for analysis reproducibility
- **Archival**: Complete Docker images for long-term preservation
- **Collaboration**: Portable environments for team sharing

### **Key Takeaways:**
- Exact package versions ensure identical results across systems
- Multi-language environments support complex research workflows
- Containers provide ultimate reproducibility insurance
- Environment documentation is as important as code documentation

---

## 🎯 **Integration: Putting It All Together**

### **Complete Workflow:**
1. **Monday**: Create standardized project structure
2. **Tuesday**: Initialize Git repository and collaboration workflow
3. **Wednesday**: Develop tested Python analysis pipeline
4. **Thursday**: Add statistical analysis and reporting with R
5. **Friday**: Package everything in reproducible environment

### **Final Project Structure:**
```
biomarker-discovery-study/
├── data/                    # Monday: Organized data storage
├── src/
│   ├── python/             # Wednesday: Tested Python analysis
│   └── r/                  # Thursday: Statistical R scripts
├── docs/
│   └── reports/           # Thursday: R Markdown reports
├── results/               # All sessions: Generated outputs
├── environment/           # Friday: Reproducible environments
├── config/               # Wednesday: Configuration management
├── docker/               # Friday: Containerization
├── .git/                 # Tuesday: Version control
├── README.md            # Monday: Project documentation
└── .gitignore          # Tuesday: Git file management
```

### **Professional Research Checklist:**
- [ ] **Organized project structure** (Monday)
- [ ] **Version controlled** with clear history (Tuesday)
- [ ] **Tested, ethical analysis code** (Wednesday)
- [ ] **Rigorous statistics with reporting** (Thursday)
- [ ] **Reproducible computational environment** (Friday)
- [ ] **Comprehensive documentation** throughout
- [ ] **Collaboration-ready** for team science

---

## 📖 **Quick Reference Commands**

### **Daily Essentials:**
```bash
# Monday: Project setup
mkdir -p project/{data,src,results,docs,environment}
code .

# Tuesday: Git workflow
git status && git add . && git commit -m "Clear message"
git push origin feature-branch

# Wednesday: Python testing
python -m pytest tests/ -v
python src/python/analysis_pipeline.py --config config/setup.yaml

# Thursday: R analysis
Rscript src/r/statistical_analysis.R
R -e "rmarkdown::render('docs/reports/analysis.Rmd')"

# Friday: Environment management
conda activate biomarker-analysis
conda env export > environment/current-env.yml
```

### **Emergency Troubleshooting:**
```bash
# Git issues
git status  # Check current state
git log --oneline  # See recent commits
git checkout main  # Return to main branch

# Environment issues  
conda info --envs  # List environments
conda activate base  # Return to base environment
conda clean --all  # Clean package cache

# Python issues
python --version  # Check Python version
pip list  # See installed packages
python -c "import pandas; print('OK')"  # Test imports
```

---

## 🌟 **Next Steps After the Course**

### **Immediate Actions:**
1. **Apply to current project**: Choose one active project and implement these practices
2. **Share with team**: Introduce colleagues to reproducible workflows
3. **Join community**: Connect with The Turing Way community online
4. **Practice regularly**: Use these tools daily to build proficiency

### **Advanced Learning:**
- **Workflow orchestration**: Snakemake, Nextflow for complex pipelines
- **Advanced containerization**: Multi-stage Docker builds, Singularity for HPC
- **Cloud computing**: Scaling reproducible research to cloud platforms
- **Data management**: Advanced strategies for large-scale research data

### **Community Resources:**
- **The Turing Way**: https://book.the-turing-way.org/
- **ICR GitLab**: Your institutional collaboration platform
- **GitHub/GitLab**: Public repositories for open science
- **Research Software Engineering**: Professional development community

---

*This reference guide provides quick access to essential concepts and commands from each session. Keep it handy as you implement reproducible research practices in your daily work!*