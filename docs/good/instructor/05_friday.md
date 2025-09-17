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
conda env export --no-build > environment-no.yml
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

## Part 2: Building a Singularity Image from a Dockerfile

>Let’s convert our Docker image to a Singularity image (`.sif` file).

### 1. Install Singularity (if needed, on your local machine)

```bash
# On Ubuntu (if you have sudo)
sudo apt-get update
sudo apt-get install singularity-container
# Or use Apptainer (new name)
sudo apt-get install apptainer
```

### 2. Build the SIF file from your Dockerfile

```bash
# Build the Docker image first (if not already done)
docker build -f Dockerfile.conda -t good-conda .

# Convert the Docker image to a Singularity SIF file
singularity build good-conda.sif docker-daemon://good-conda:latest
```
>**Note:** You may need root/admin privileges to build the SIF file.

---

## Part 3: Transferring the SIF File to the HPC

>Now, let’s transfer the `.sif` file to Alma using `scp` or `rsync`.

```bash
# From your local machine
scp good-conda.sif <username>@alma.icr.ac.uk:/data/your_folder/
# Or using rsync
rsync -av good-conda.sif <username>@alma.icr.ac.uk:/data/your_folder/
```

>Log in to Alma and check the file is there:

```bash
ssh <username>@alma.icr.ac.uk
ls /data/your_folder/good-conda.sif
```

---

## Part 4: Running Python & R Scripts in Singularity on Alma

>Let’s run our code inside the container on the HPC.

```bash
# Load Singularity module if needed
module load singularity

# Run the Python script
singularity exec --bind /data/your_folder/data:/app/data,/data/your_folder/results:/app/results good-conda.sif python analysis.py

# Run the R script
singularity exec --bind /data/your_folder/data:/app/data,/data/your_folder/results:/app/results good-conda.sif Rscript analysis.R
```

>**Tip:** The `--bind` option mounts your data and results folders inside the container.

>**For batch jobs:**  
Create a simple SLURM script (e.g., `run_container.slurm`):

```bash
#!/bin/bash
#SBATCH --job-name=run_container
#SBATCH --output=container_output.txt
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G

module load singularity
singularity exec --bind /data/your_folder/data:/app/data,/data/your_folder/results:/app/results good-conda.sif python analysis.py
```

Submit with:
```bash
sbatch run_container.slurm
```

---

## Part 5: Wrap-up, Best Practices & Homework

- **Best Practices:**
    - Use Singularity for reproducible, portable research on HPC.
    - Always test your container locally before transferring to HPC.
    - Document your workflow for others to follow.

- **Homework:**
    - Try building and running a Singularity container for a different project.
    - Share your `.sif` file and workflow with a collaborator.

---

## Session Cheat Sheet: Singularity on HPC

```bash
# Build Docker image
docker build -f Dockerfile.conda -t good-conda .
singularity build good-conda.sif docker-daemon://good-conda:latest
#or 
docker save good-conda:latest -o good-conda.tar
singularity build good-conda.sif docker-archive://good-conda.tar

# Use files to transfer to scratch and copy data
## Run the Python script
singularity exec --bind data:/app/data,results:/app/results good-conda.sif bash -c "source /opt/conda/etc/profile.d/conda.sh && conda run -n good-env python /app/analysis.py"

## Run the R script
singularity exec --bind data:/app/data,results:/app/results good-conda.sif bash -c "source /opt/conda/etc/profile.d/conda.sh && conda run -n good-env Rscript /app/analysis.R"



```

---

**Congratulations on completing the course!**