#!/bin/bash

source activate
conda activate simnmt-ozan
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=1 nmtpy train -C ../simultaneousMMT/custom_configs/en-de/en-de-simrl-multimodal-full-large.conf train.seed:0
/usr/bin/nvidia-smi
uptime
