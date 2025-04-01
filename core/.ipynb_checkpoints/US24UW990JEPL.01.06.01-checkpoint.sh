#!/bin/bash
#SBATCH --job-name=010601
#SBATCH --mail-user=jchasco@wisc.edu
#SBATCH --mail-type=FAIL
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=700gb
#SBATCH --time=90:00:00
#SBATCH --error=US24UW990JEPL.01.06.01.error

python3.9 US24UW990JEPL.01.06.01.py > US24UW990JEPL.01.06.01.out 2>&1
