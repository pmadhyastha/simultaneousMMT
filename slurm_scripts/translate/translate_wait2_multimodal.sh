#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./experiments/custom/dump-attention-wait2-multimodal-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy stranslate -m 100 -s test_2016_flickr -f vwk --n-init-tokens "1,2,3,5,7" -o wait2_multimodal_decoding_results ../experiments/simultaneouswaitknmt-r553c9-val036.best.bleu_29.370.ckpt 
