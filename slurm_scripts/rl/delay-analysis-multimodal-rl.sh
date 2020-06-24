#!/bin/bash


export PATH=~/miniconda3/bin/:$PATH
source activate
conda activate simnmt-ozan
cd ~/experiments/simnmt/nmtpy/w2w_models/en-fr
ls
~/simmt/scripts/decode_snmt_rl.sh
~/simmt/scripts/delay_analysis.py -r ~/simmt/data/multi30k/en-fr/test_2016_flickr.lc.norm.tok.fr
