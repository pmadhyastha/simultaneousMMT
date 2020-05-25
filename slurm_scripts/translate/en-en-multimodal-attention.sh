#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/custom/en-en-multimodal-wait1-dump-attention-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy stranslate -m 100 -s test_2016_flickr -f wk --n-init-tokens "1,2,3,5,7" -o ../simultaneousMMT/decoding_results/en_en_multimodal_wait1 ../simultaneousMMT/experiments/bpe_models/en-en/en-en-multimodal-w2bpe-wait1/simultaneouswaitknmt-r2b64a-val040.best.bleu_93.820.ckpt
