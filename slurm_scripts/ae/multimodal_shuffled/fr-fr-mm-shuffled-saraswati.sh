#!/bin/bash

export PATH=~/miniconda3/bin/:$PATH
source activate
conda activate simnmt
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy train -C ../simultaneousMMT/custom_configs/fr-fr-multimodal-shuffled-w2bpe.conf train.seed:0
/usr/bin/nvidia-smi
uptime
