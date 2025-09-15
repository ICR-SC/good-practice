# Final Session: Running Reproducible Research with Singularity on HPC
[instructor home](overview.md)

## Final Session Timings (Instructor Guide) — Revised

| Part | Section(s) Covered                                                      | Suggested Time | Running Time |
|------|-------------------------------------------------------------------------|:--------------:|:------------:|
| 1    | Opening, Welcome & Why Use Singularity on HPC                           |    10 min      |     10       |
| 2    | Building a Singularity Image from a Dockerfile                          |    15 min      |     25       |
| 3    | Transferring the SIF File to the HPC                                    |    10 min      |     35       |
| 4    | Running Python & R Scripts in Singularity on Alma                       |    20 min      |     55       |
| 5    | Wrap-up, Best Practices & Homework                                      |     5 min      |     60       |

---

## Part 1: Opening, Welcome & Why Use Singularity on HPC

>Welcome to our final session! Today, we’ll see how to use Singularity (now called Apptainer) to run your containerized research code on the Alma HPC. Singularity is designed for HPC environments and works well with Docker images.

- **Singularity** runs containers securely on shared systems like HPC clusters.
- You can convert your Docker images to Singularity images and run them on Alma.

---

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

# Convert Docker image to Singularity SIF
singularity build good-conda.sif docker-daemon://good-conda:latest

# Transfer SIF to HPC
scp good-conda.sif <username>@alma.icr.ac.uk:/data/your_folder/

# On Alma: Run Python
singularity exec --bind /data/your_folder/data:/app/data,/data/your_folder/results:/app/results good-conda.sif python analysis.py

# On Alma: Run R
singularity exec --bind /data/your_folder/data:/app/data,/data/your_folder/results:/app/results good-conda.sif Rscript analysis.R

# Submit as a batch job
sbatch run_container.slurm
```

---

**Congratulations on completing the course!**