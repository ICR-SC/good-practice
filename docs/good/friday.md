# Friday Session: Containerization & Environment Management
*Duration: 60 minutes | Format: Interactive demonstration and hands-on practice*

## Summary
Friday's session focuses on containerization and advanced environment management for reproducible research. You'll learn to use Docker for creating portable, reproducible environments and explore conda for package management. We'll demonstrate a foundation for scalable, reproducible research workflows.

---

## What We Cover

### Docker Fundamentals
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
- Converting docker to singularity for HPC

---

## Key Takeaways

By the end of this session, you'll be able to:

- **Create Docker containers** for your research projects to ensure reproducibility across different systems
- **Manage Python environments** using conda to avoid dependency conflicts
- **Share reproducible environments** with collaborators using container images and environment files
- **Understand when to use** containers vs virtual environments for different research scenarios
- **Apply containerization** to make your research more portable and reproducible

---

### Additional Resources
- [Docker for Data Science Tutorial](https://docker-curriculum.com/)
- [Conda User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)
- [The Turing Way: Reproducible Environments](https://book.the-turing-way.org/reproducible-research/renv.html)
- [Docker Best Practices for Research](https://docs.docker.com/develop/dev-best-practices/)
- Link to repo: [github.com/ICR-SC/gp-01-biomarkers](https://github.com/ICR-SC/gp-01-biomarkers)  

### Cheat Sheet
#### **Conda Commands Used:**
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
conda env export --no-build > environment.yml

# Run scripts
python src/python/analysis.py
Rscript src/R/analysis.R
```

#### **Docker Commands Used:**
```bash
# Build Docker images
docker build -f docker/Dockerfile.python -t good-python .
docker build -f docker/Dockerfile.r -t good-r .
docker build -f docker/Dockerfile.conda -t good-conda .
# Look inside the docker image and navigate with bash
docker run -it good-python /bin/bash
# Run Docker containers
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-python
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-r
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-conda python analysis.py
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-conda Rscript analysis.R
```

#### **Dockerfile Examples Created:**
```dockerfile
# Python Dockerfile
FROM python:3.13-slim
WORKDIR /app
RUN pip install pandas matplotlib pytest
COPY src/python/analysis.py ./analysis.py
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

#### **Singularity Commands used**
```bash
# Build Docker image
docker build -f Dockerfile.conda -t good-conda .
singularity build good-conda.sif docker-daemon://good-conda:latest
#or 
docker save good-conda:latest -o good-conda.tar
singularity build good-conda.sif docker-archive://good-conda.tar

# (Copy files and data to alma, eg /data/scratch/etc...)
## Run the Python script
singularity exec --bind data:/app/data,results:/app/results good-conda.sif bash -c "source /opt/conda/etc/profile.d/conda.sh && conda run -n good-env python /app/analysis.py"

## Run the R script
singularity exec --bind data:/app/data,results:/app/results good-conda.sif bash -c "source /opt/conda/etc/profile.d/conda.sh && conda run -n good-env Rscript /app/analysis.R"
```