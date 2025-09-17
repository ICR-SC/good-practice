# Friday Session: Containerization & Environment Management
*Duration: 60 minutes | Format: Interactive demonstration and hands-on practice*

## Summary
Friday's session focuses on containerization and advanced environment management for reproducible research. You'll learn to use Docker for creating portable, reproducible environments and explore conda for Python package management. We'll demonstrate how containers solve the "it works on my machine" problem and provide a foundation for scalable, reproducible research workflows.

---

## What We Cover

### Docker Fundamentals
- Understanding containers vs virtual machines
- Installing and configuring Docker
- Basic Docker commands and workflow
- Creating simple Dockerfiles for research projects

### Conda Environment Management
- Installing Anaconda/Miniconda
- Creating and managing conda environments
- Using environment.yml files for reproducibility
- Comparing conda vs pip for package management

### Practical Applications
- Containerizing a simple analysis pipeline
- Sharing reproducible environments with colleagues
- Best practices for container security and efficiency
- Integration with version control systems

---

## Key Takeaways

By the end of this session, you'll be able to:

- **Create Docker containers** for your research projects to ensure reproducibility across different systems
- **Manage Python environments** using conda to avoid dependency conflicts
- **Share reproducible environments** with collaborators using container images and environment files
- **Understand when to use** containers vs virtual environments for different research scenarios
- **Apply containerization** to make your research more portable and reproducible

---

## Homework & Resources

### Practice Exercise (~30 minutes)
- Create a simple Dockerfile for one of your analysis scripts from earlier sessions
- Set up a conda environment with specific package versions for a research project
- Practice sharing an environment file with a colleague or on GitLab

### Additional Resources
- [Docker for Data Science Tutorial](https://docker-curriculum.com/)
- [Conda User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)
- [The Turing Way: Reproducible Environments](https://book.the-turing-way.org/reproducible-research/renv.html)
- [Docker Best Practices for Research](https://docs.docker.com/develop/dev-best-practices/)

### Cheat Sheet

**Conda Commands Used:**
```bash
# Create Python environment
conda create -n good-python python=3.13 pandas matplotlib pytest -y
conda activate good-python
conda list

# Create R environment  
conda create -n good-r r-base=4.3 r-tidyverse r-ggplot2 r-testthat -y
conda activate good-r

# Export environment
conda env export > environment.yml

# Export platform indeppendedn
conda env export --no-builds > environment.yml

# Run scripts
python src/python/analysis.py
Rscript src/R/analysis.R
```

**Docker Commands Used:**
```bash
# Build Docker images
docker build -f Dockerfile.python -t good-python .
docker build -f Dockerfile.r -t good-r .
docker build -f Dockerfile.conda -t good-conda .

# Run Docker containers
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-python
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-r
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-conda python analysis.py
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-conda Rscript analysis.R
```

**Dockerfile Examples Created:**
```dockerfile
# Python Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY src/python/analysis.py ./analysis.py
COPY data/raw ./data/raw
RUN pip install pandas matplotlib
CMD ["python", "analysis.py"]

# R Dockerfile  
FROM rocker/r-base:4.3.1
WORKDIR /app
COPY src/R/analysis.R ./analysis.R
COPY data/raw ./data/raw
RUN R -e "install.packages(c('tidyverse', 'ggplot2', 'testthat'), repos='https://cloud.r-project.org')"
CMD ["Rscript", "analysis.R"]

# Conda Dockerfile
FROM continuumio/miniconda3:latest
WORKDIR /app
COPY environment.yml .
COPY src/python/analysis.py ./analysis.py
COPY src/R/analysis.R ./analysis.R
COPY data/raw ./data/raw
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "good-env", "/bin/bash", "-c"]
ENTRYPOINT ["conda", "run", "-n", "good-env"]
CMD ["python", "analysis.py"]
```