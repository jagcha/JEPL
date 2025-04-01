#!/bin/bash
#SBATCH --job-name=010504 ## Checkme
#SBATCH --mail-user=jchasco@wisc.edu
#SBATCH --mail-type=FAIL
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=700gb ## Checkme
#SBATCH --time=90:00:00
#SBATCH --error=US24UW990JEPL.01.05.04.error ## Checkme

python3.9 US24UW990JEPL.01.05.04.py > US24UW990JEPL.01.05.04.out 2>&1 ## Checkme
