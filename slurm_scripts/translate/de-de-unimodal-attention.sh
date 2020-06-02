#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/custom/de-de-unimodal-wait1-dump-attention-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy stranslate -m 100 -s test_2016_flickr -f wk --n-init-tokens "1,2,3,5,7" -o ../simultaneousMMT/decoding_results/de_de_unimodal_wait1/de_de_unimodal_wait1 ../simultaneousMMT/experiments/simultaneouswaitknmt-rb65f6.best.bleu.ckpt

