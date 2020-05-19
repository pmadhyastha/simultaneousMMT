#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousNMT/experiments/custom/en-en-unimodal-dump-attention-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt
cd simmt
TERM=xterm
ls ~
CUDA_VISIBLE_DEVICES=0 nmtpy stranslate -m 100 -s test_2016_flickr -f vwk --n-init-tokens "1,2,3,5,7" -o ../simultaneousNMT/en_en_unimodal_decoding_results ~/experiments/experiments/simnmt/nmtpy/bpe_models/en-en/en-en-unimodal-w2bpe/simultaneousnmt-r65ec1-val026.best.bleu_93.400.ckpt
