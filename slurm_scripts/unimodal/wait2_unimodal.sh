#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./experiments/unimodal/wait2-unimodal-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy train -C configs/en-de/word2word-min2/wait2-rnn-unimodal.conf
/usr/bin/nvidia-smi
uptime
