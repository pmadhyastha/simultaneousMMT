#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/custom/en-fr-unimodal-waitk-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt
cd simmt
TERM=xterm
for k in 1 2 3 5 7
do
    CUDA_VISIBLE_DEVICES=0 nmtpy train -C ../simultaneousMMT/custom_configs/en-fr/wait$k-rnn-unimodal.conf
    /usr/bin/nvidia-smi
done
uptime
