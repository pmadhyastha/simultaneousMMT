#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/rl/en-fr-cgru-simmmtrl-multimodal-agent-side-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt-ozan
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=1 nmtpy train -C ../simultaneousMMT/custom_configs/en-fr/en-fr-simrl-multimodal-agent-side.conf train.seed:2
/usr/bin/nvidia-smi
uptime
