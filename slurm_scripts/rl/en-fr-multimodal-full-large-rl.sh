#!/bin/bash


source activate
conda activate simnmt-ozan
cd simmt
TERM=xterm
CUDA_VISIBLE_DEVICES=0 nmtpy train -C ../simultaneousMMT/custom_configs/en-fr/en-fr-simrl-multimodal-full-large.conf train.seed:0
/usr/bin/nvidia-smi
uptime
