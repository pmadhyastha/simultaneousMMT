#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/rl/en-fr-unimodal-rlenv-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt-ozan
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy train -C configs/en-fr/word2word/snmt-rnn-unimodal.conf train.seed:0
/usr/bin/nvidia-smi
uptime
