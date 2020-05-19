#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/custom/en-en-unimodal-dump-attention-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy stranslate -m 100 -s test_2016_flickr -f wk --n-init-tokens "1,2,3,5,7" -o ../simultaneousMMT/decoding_results/en_en_unimodal ../simultaneousMMT/experiments/simultaneousnmt-r65ec1.best.bleu.ckpt
