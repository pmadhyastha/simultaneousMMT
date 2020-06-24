#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/rl/en-fr-cgru-simmmtrl-multimodal-agent-side-slurm-%j.out

#export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt-ozan
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=1 nmtpy train -C ../simultaneousMMT/custom_configs/en-de/en-de-simrl-multimodal-agent-side-large.conf train.seed:0
/usr/bin/nvidia-smi
uptime
