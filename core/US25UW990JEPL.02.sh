#!/bin/bash
#SBATCH --job-name=AC01
#SBATCH --mail-user=jchasco@wisc.edu
#SBATCH --mail-type=FAIL
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=350gb
#SBATCH --time=12:00:00
#SBATCH --error=US25UW990JEPL.02.error

python3.9 US25UW990JEPL.02.py > US25UW990JEPL.02.out
