# Friday Live Coding Script: Good-Practices with Conda and Docker
[instructor home](overview.md)

## Friday Session Timings (Instructor Guide) — Revised

| Part | Section(s) Covered                                                                 | Suggested Time | Running Time |
|------|------------------------------------------------------------------------------------|:--------------:|:------------:|
| 1    | Opening, Welcome & Why Use Conda and Docker                                        |    10 min      |     10       |
| 2    | Creating and Using Conda Environments (Python & R)                                 |    15 min      |     25       |
| 3    | Introduction to Docker & Writing a Dockerfile                                      |    10 min      |     35       |
| 4    | Building and Running Python & R Scripts in Docker                                  |    20 min      |     55       |
| 5    | Wrap-up, Best Practices & Homework                                                 |     5 min      |     60       |

---

## Part 1: Opening, Welcome & Why Use Conda and Docker

>Welcome to our final session! Today, we’ll learn how to use Conda and Docker to make our research environments reproducible and portable. This is essential for sharing your work and ensuring others (and future you!) can run your code.

- **Conda** helps you manage packages and environments for Python, R, and more.
- **Docker** lets you package your code and environment into a container that runs anywhere.

---

## Part 2: Creating and Using Conda Environments (Python & R)

>Let’s start by creating Conda environments for both Python and R, matching the packages we’ve used this week.

### Python Environment

```bash
# Create a new conda environment for Python
conda create -n good-python python=3.11 pandas matplotlib pytest -y
conda activate good-python

# Check installed packages
conda list

# Run your Python script
python src/python/analysis.py
```

### R Environment

```bash
# Create a new conda environment for R
conda create -n good-r r-base=4.3 r-tidyverse r-ggplot2 r-testthat -y
conda activate good-r

# Start R and run your script
Rscript src/R/analysis.R
```

>**Tip:** You can export your environment for sharing:
```bash
conda env export > environment.yml
```

---

## Part 3: Introduction to Docker & Writing a Dockerfile

>Docker lets you create a container with everything your code needs. Let’s write a simple Dockerfile for both Python and R.

### Python Dockerfile (`docker/Dockerfile.python`)

```dockerfile
# ---------- Python dockerfile --------------------------------
# BUILD IT:     docker build -f docker/Dockerfile.python -t good-python .
# CHECK IT:     docker run -it good-python /bin/bash
# RUN IT:       docker run -v ./data:/app/data -v ./results:/app/results good-python
# -------------------------------------------------------------
FROM python:3.13-slim
WORKDIR /app
RUN pip install pandas matplotlib pytest
COPY src/python/analysis.py ./analysis.py
COPY data/raw/aml_tcga_gdc ./data/raw/aml_tcga_gdc
CMD ["python", "analysis.py"]
```

### R Dockerfile (`docker/Dockerfile.rscript`)

```dockerfile
# filepath: Dockerfile.rscript
FROM rocker/r-base:4.3.1

WORKDIR /app

COPY src/R/analysis.R ./analysis.R
COPY data/raw ./data/raw

RUN R -e "install.packages(c('tidyverse', 'ggplot2', 'testthat'), repos='https://cloud.r-project.org')"

CMD ["Rscript", "analysis.R"]
```

---

## Part 4: Building and Running Python & R Scripts in Docker

>Let’s build and run our containers!

### Python

```bash
# Build the Python Docker image
docker build -f docker/Dockerfile.python -t good-python .
# Look inside the docker image and navigate with bash
docker run -it good-python /bin/bash
# Run the Python container
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-python
```

### R

```bash
# Build the R Docker image
docker build -f docker/Dockerfile.r -t good-r .

# Run the R container
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-r
```

>**Tip:** The `-v` flag mounts your local data and results folders into the container, so outputs are saved outside the container.

---


### Conda Dockerfile (`docker/Dockerfile.conda`)
```dockerfile
# filepath: Dockerfile.conda
FROM continuumio/miniconda3:latest

WORKDIR /app

# Copy your environment file and scripts
COPY environment.yml .
COPY src/python/analysis.py ./analysis.py
COPY src/R/analysis.R ./analysis.R
COPY data/raw ./data/raw

# Create the conda environment
RUN conda env create -f environment.yml

# Ensure conda environment is activated by default
SHELL ["conda", "run", "-n", "good-env", "/bin/bash", "-c"]

# Set entrypoint to run either script (pass as argument)
ENTRYPOINT ["conda", "run", "-n", "good-env"]

# Default command (can be overridden)
CMD ["python", "analysis.py"]
```

```bash
# Build the Conda Docker image
docker build -f docker/Dockerfile.conda -t good-conda .
# Look inside the docker image and navigate with bash
docker run -it good-python /bin/bash
# Run the python script
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-conda python analysis.py
# Run the R script
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results good-conda Rscript analysis.R
```
## Part 5: Wrap-up, Best Practices & Homework

- **Best Practices:**
    - Always use environment files (`environment.yml`, `Dockerfile`) for reproducibility.
    - Document your dependencies and how to run your code.
    - Use containers for sharing and deploying your research.

- **Homework:**
    - Try building and running your own Docker container for a different script or project.
    - Share your `environment.yml` or `Dockerfile` with a collaborator and see if they can reproduce your results.

