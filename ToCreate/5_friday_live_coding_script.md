# Friday Session: Conda Environments for Sustainable Research Computing
## Live Coding Script for Instructors

*Duration: 60 minutes | Format: Participatory live coding*
*Homework: 2-3 hours comprehensive environment management practice*

---

## Pre-Session Setup (5 minutes before start)

**[ASIDE: Have terminal open, verify conda is installed and working. Have the project from Monday-Thursday available. Check that participants can run `conda --version`.]**

---

## Opening & Welcome (starts at 0 min, takes 10 min)

### What I Say:
"Welcome to Friday - our final session! This week we've built project structures, version control workflows, Python analysis pipelines, and R statistical analysis. Today we ensure all of this work is completely reproducible by anyone, anywhere, at any time.

Computational reproducibility is the capstone of The Turing Way approach. It's not enough to have good code if others can't run it because they have different package versions. Today we solve that challenge.

By the end of today, your research will be truly reproducible - others can recreate your exact computational environment and get identical results. Let's start by checking our conda installation."

#### What I Type (Live Coding):
```bash
# Check conda installation and version
conda --version

# Check current environment
conda info --envs

# See what's currently installed
conda list | head -10

# Check current working directory (should be our project)
pwd
ls -la
```

#### What I Say:
"Perfect! Conda is our package and environment manager that works across languages - Python, R, and even system tools. Notice how it shows our current environment and installed packages. This transparency is exactly what we need for reproducible research."

**[ASIDE: Help anyone with conda installation issues. Windows users might need to use conda prompt.]**

---

## Part 5.1 (starts at 10 min, takes 15 min): Conda Environment Creation

### Understanding Why Environments Matter

#### What I Say:
"Let me show you a common research reproducibility nightmare, then how environments solve it."

#### What I Type (Live Coding):
```bash
# Show current Python and package versions
python --version
python -c "import pandas; print('pandas:', pandas.__version__)"
python -c "import numpy; print('numpy:', numpy.__version__)"

# This is what your collaborator might have...
echo "Your collaborator might have different versions!"
echo "pandas: 1.4.0 (you have 1.5.3)"
echo "numpy: 1.20.0 (you have 1.24.3)"
echo "Results might be subtly different!"
```

#### What I Say:
"These version differences seem minor, but they can cause reproducibility failures. A statistical test might give slightly different p-values, or a visualization might look different. Environments solve this by creating isolated, reproducible computational spaces."

### Creating Our Research Environment

#### What I Say:
"Let's create a dedicated environment for our biomarker research project, capturing exactly what we need for our analysis pipeline."

#### What I Type (Live Coding):
```bash
# Create new environment for our biomarker project
conda create --name biomarker-analysis python=3.9

# Activate the environment
conda activate biomarker-analysis

# Check that we're in the new environment
conda info --envs
which python

# Install our core analysis packages with specific versions
conda install pandas=1.5.3 numpy=1.24.3 matplotlib=3.7.1

# Install scientific packages from conda-forge channel
conda install -c conda-forge scikit-learn=1.3.0

# Check what we've installed
conda list | head -10
```

#### What I Say:
"Notice how we specified exact versions? This ensures anyone who recreates this environment gets identical package versions. The conda-forge channel provides additional scientific packages."

### Adding R to Our Environment

#### What I Say:
"Research often requires multiple languages. Let's add R to our environment."

#### What I Type (Live Coding):
```bash
# Add R to our environment
conda install r-base=4.3.1

# Install key R packages via conda
conda install r-tidyverse r-ggplot2

# Check our mixed-language environment
conda list | grep -E "python|r-base|pandas"
```

#### What I Say:
"See how we can mix languages in one environment? This is powerful for research workflows that span Python and R. Everything is managed together with consistent versions."

### Environment Documentation (starts at 25 min, takes 10 min)

#### What I Say:
"The key to reproducibility is documenting exactly what's in our environment so others can recreate it."


#### What I Type (Live Coding):
```bash
# Step-by-step recipe to create the biomarker analysis environment

# 1. Create the environment with Python
conda create --name biomarker-analysis python=3.9

# 2. Activate the environment
conda activate biomarker-analysis

# 3. Install core Python packages
conda install pandas=1.5.3 numpy=1.24.3 matplotlib=3.7.1

# 4. Install machine learning and interactive tools
conda install scikit-learn=1.3.0 jupyter=1.0.0

# 5. Add R and key R packages
conda install r-base=4.3.1 r-tidyverse=2.0.0 r-ggplot2=3.4.2

# 6. Install development tools
conda install git=2.40.1

# 7. Install pip and pip-only packages
conda install pip=23.1.2
pip install umap-learn==0.5.3

# 8. Verify installation
conda list | head -20
python -c "import pandas, numpy, matplotlib, sklearn; print('Python packages OK')"
R --version | head -1

# 9. Export environment for sharing and reproduceability
conda env export --no-builds > environment/biomarker-env.yml

# 10. Export the full version of the yaml file
conda env export > environment/biomarker-env-full.yml

# 11. look inside both with head
head -20 environment/biomarker-env.yml
echo "---"
head -20 environment/biomarker-env-full.yml

```

#### What I Type (Live Coding):

"The no-builds YAML file gives us control over what we include. The fully exported version captures everything currently installed. For reproducibility, the no-builds approach is usually better."

### Testing Environment Recreation

#### What I Say:
"Let's test that our environment file actually works by recreating the environment."

#### What I Type (Live Coding):
```bash
# Deactivate current environment
conda deactivate

# Remove the test environment (if it exists)
conda env remove --name biomarker-test 2>/dev/null || true

# Create environment from our file
conda env create -f environment/biomarker-env.yml -n biomarker-test

# Activate and test the recreated environment
conda activate biomarker-test

# Verify it works
python -c "import pandas; print('pandas:', pandas.__version__)"
python -c "import numpy; print('numpy:', numpy.__version__)"
R --version | head -1

echo "✅ Environment recreation successful!"

# Switch back to our main environment
conda activate biomarker-analysis
```

#### What I Say:
"Perfect! This proves our environment file works. Anyone can now recreate our exact computational environment using just this one file."

---

## Part 5.2 (starts at 35 min, takes 10 min): Docker for Reproducibility (optional)

### Multiple Environments for Different Purposes

#### What I Say:
"Research projects often need different environments for different phases. Let's create a workflow that supports this."

#### What I Type (Live Coding):
```bash
# Create a Python-focused environment for data preprocessing
conda create --name biomarker-preprocessing python=3.9 pandas numpy scikit-learn

# Create an R-focused environment for statistical analysis
conda create --name biomarker-stats r-base r-tidyverse r-ggplot2

# Show all our environments
conda info --envs

# Quick test of the preprocessing environment
conda activate biomarker-preprocessing
python -c "import pandas; print('Preprocessing env ready')"

# Switch to stats environment
conda activate biomarker-stats
R -e "library(ggplot2); cat('Stats env ready\n')"

# Back to main environment
conda activate biomarker-analysis
```

#### What I Say:
"This strategy lets us have specialized environments: one for data preprocessing, one for statistical analysis, and our main one for general work. Each can have different stability requirements."

### Cross-Platform Environment Files

#### What I Say:
"Research teams often use different operating systems. Let's create an environment that works across platforms."

#### What I Type (create environment/cross-platform-env.yml):
```yaml
# Cross-Platform Environment
# Works on Windows, macOS, and Linux

name: biomarker-cross-platform

channels:
  - conda-forge
  - defaults

dependencies:
  # Use version ranges for flexibility
  - python >=3.9,<3.11
  - pandas >=1.5,<2.0
  - numpy >=1.20,<2.0
  - matplotlib >=3.5,<4.0
  - scikit-learn >=1.2,<2.0
  
  # R with broad compatibility
  - r-base >=4.2,<4.4
  - r-essentials
  
  # Cross-platform tools
  - git
  - pip
  
  - pip:
    - umap-learn >=0.5,<1.0
```

#### What I Say:
"Notice how we use version ranges instead of exact versions? This gives flexibility across platforms while maintaining compatibility. The key is testing on all target platforms."

### Environment Verification and Testing

#### What I Say:
"Let's create a simple test to verify our environment works correctly."

#### What I Type (create src/python/verify_environment.py):
```python
#!/usr/bin/env python3
"""
Environment Verification Script
Tests that required packages are installed and working.
"""

def test_python_packages():
    """Test Python package imports."""
    print("Testing Python packages...")
    
    try:
        import pandas
        import numpy
        import matplotlib
        import sklearn
        print("✅ Python packages: All imports successful")
        
        # Test basic functionality
        import pandas as pd
        df = pd.DataFrame({'test': [1, 2, 3]})
        assert len(df) == 3
        print("✅ Pandas: Basic functionality works")
        
        import numpy as np
        arr = np.array([1, 2, 3])
        assert np.sum(arr) == 6
        print("✅ NumPy: Basic functionality works")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Functionality error: {e}")
        return False

def test_r_availability():
    """Test R installation."""
    print("\nTesting R installation...")
    
    try:
        import subprocess
        result = subprocess.run(['R', '--version'], 
                               capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"✅ R: {version_line}")
            return True
        else:
            print("❌ R: Not available")
            return False
            
    except Exception as e:
        print(f"❌ R test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🔬 ENVIRONMENT VERIFICATION")
    print("=" * 40)
    
    python_ok = test_python_packages()
    r_ok = test_r_availability()
    
    print("\n" + "=" * 40)
    if python_ok and r_ok:
        print("🎉 Environment verification PASSED!")
        print("Your environment is ready for analysis.")
    else:
        print("⚠️  Environment verification FAILED!")
        print("Please check package installations.")

if __name__ == "__main__":
    main()
```

#### What I Type (Live Coding):
```bash
# Test our environment verification
python src/python/verify_environment.py

# Make it executable for easy use
chmod +x src/python/verify_environment.py
```

#### What I Say:
"This verification script ensures our environment is working correctly. Teams can run this to quickly check if their environment setup is correct."

---

## Part 5.3 (starts at 45 min, takes 10 min): Practical Demo & Verification

### Introduction to Containers

#### What I Say:
"Conda environments are excellent, but Docker containers provide ultimate reproducibility by capturing the entire system. This is crucial for long-term archival or complex dependencies."

#### What I Type (create docker/Dockerfile):
```dockerfile
# Simple Docker container for biomarker analysis
FROM continuumio/miniconda3:latest

# Set working directory
WORKDIR /analysis

# Copy environment file
COPY environment/biomarker-env.yml /tmp/biomarker-env.yml

# Create conda environment
RUN conda env create -f /tmp/biomarker-env.yml

# Make conda environment available
SHELL ["conda", "run", "-n", "biomarker-analysis", "/bin/bash", "-c"]

# Copy project files
COPY src/ /analysis/src/
COPY config/ /analysis/config/

# Create data directories
RUN mkdir -p data results

# Set default command
CMD ["conda", "run", "-n", "biomarker-analysis", "python", "src/python/verify_environment.py"]
```

#### What I Say:
"This Dockerfile creates a complete, self-contained environment including the operating system. Anyone can run this container and get identical results, regardless of their local setup."

### Container Usage Instructions

#### What I Type (create docker/README.md):
```markdown
# Docker Container for Biomarker Analysis

## Quick Start

```bash
# Build the container
docker build -t biomarker-analysis .

# Run the verification
docker run biomarker-analysis

# Run with your data
docker run -v $(pwd)/data:/analysis/data biomarker-analysis \
    conda run -n biomarker-analysis python src/python/analysis_pipeline.py

# Interactive session
docker run -it biomarker-analysis \
    conda run -n biomarker-analysis bash
```

## When to Use Docker

- **Long-term archival**: Freeze complete environment for papers
- **Complex dependencies**: When conda can't handle system requirements  
- **Team collaboration**: Ensure identical environments across different systems
- **Cloud deployment**: Easy deployment to any cloud platform

## When to Use Conda

- **Active development**: Faster iteration and package updates
- **Interactive work**: Better integration with IDEs and notebooks
- **Package exploration**: Easy to add/remove packages for testing
```

#### What I Say:
"Docker is perfect for final reproducibility and archival, while conda is better for active development. Use both strategically - conda for daily work, Docker for sharing and long-term preservation."

---

## Part 5.4 (starts at 55 min, takes 5 min): Wrap-up & Questions

### Versioning and Documentation Strategy

#### What I Say:
"Research projects span years. Let's create a strategy for managing environments over time."

#### What I Type (create environment/README.md):
```markdown
# Environment Management Guide

## Environment Files

- `biomarker-env.yml` - Main analysis environment (recommended)
- `cross-platform-env.yml` - Compatible across operating systems
- `biomarker-preprocessing.yml` - Specialized for data preprocessing
- `biomarker-stats.yml` - R-focused statistical analysis

## Usage Instructions

### First-time Setup
```bash
# Create the environment
conda env create -f environment/biomarker-env.yml

# Activate the environment
conda activate biomarker-analysis

# Verify installation
python src/python/verify_environment.py
```

### Daily Usage
```bash
# Always activate environment before work
conda activate biomarker-analysis

# Run analysis
python src/python/analysis_pipeline.py

# When done, deactivate (optional)
conda deactivate
```

### Updating the Environment
```bash
# Add new package
conda install new-package

# Update environment file
conda env export --no-builds > environment/biomarker-env.yml

# Commit to version control
git add environment/biomarker-env.yml
git commit -m "Add new-package to environment"
```

## Troubleshooting

**Environment conflicts:**
```bash
conda clean --all
conda env remove -n biomarker-analysis
conda env create -f environment/biomarker-env.yml
```

**Missing packages:**
Check that you're in the correct environment:
```bash
conda info --envs
conda activate biomarker-analysis
```

## Environment Lifecycle

1. **Development**: Use conda for active package management
2. **Collaboration**: Share YAML files for team reproducibility  
3. **Publication**: Create Docker container for archival
4. **Long-term**: Archive both conda YAML and Docker image
```

#### What I Say:
"This documentation ensures your team knows how to use and maintain the environments properly. Clear instructions prevent environment-related problems."

---

## Session Wrap-up & Course Summary (5 minutes)

### What I Say:
"Congratulations! You've completed our comprehensive journey through reproducible research practices. Let me summarize what you've accomplished this week and how it all fits together.

✅ **This Week's Journey:**
- **Monday**: Project structure and command line fundamentals
- **Tuesday**: Version control and collaboration with Git
- **Wednesday**: Ethical Python analysis with bias detection and testing
- **Thursday**: Statistical rigor with R and reproducible reporting
- **Friday**: Complete computational reproducibility with environments

✅ **You Can Now:**
- Create standardized, reproducible project structures
- Track and collaborate on code changes with Git
- Write ethical, tested Python analysis code
- Perform rigorous statistical analysis with R
- Ensure computational reproducibility with conda environments
- Package everything for long-term preservation

✅ **The Turing Way Principles You've Applied:**
- **Reproducible**: Others can recreate your exact analysis
- **Collaborative**: Teams can work together effectively
- **Ethical**: Bias detection and fairness built into analysis
- **Transparent**: All decisions documented and version controlled
- **Sustainable**: Environments ensure long-term usability

**Your Final Homework** will integrate everything - you'll create a complete, reproducible research pipeline that demonstrates all these skills together.

**Key Message**: You now have the tools to conduct research that meets the highest standards of reproducibility and scientific rigor. This isn't just about good practices - it's about advancing science through trustworthy, reproducible research.

**The real test**: Can a colleague take your repository and environment files and recreate your results exactly? If yes, you've achieved true computational reproducibility.

Thank you for an amazing week of learning! Your research will make a real difference because it's built on this solid foundation of reproducible practices."

---

**END OF LIVE SESSION**