#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/rl/en-fr-cgru-simmmtrl-multimodal-full-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt-ozan
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy train -C ../simultaneousMMT/custom_configs/en-fr/en-fr-simrl-multimodal-full.conf train.seed:2
/usr/bin/nvidia-smi
uptime
