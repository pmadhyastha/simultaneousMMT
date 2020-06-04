#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=al4616
#SBATCH -o ./simultaneousMMT/experiments/custom/en-fr-decode-rl-slurm-%j.out

export PATH=/vol/bitbucket/al4616/miniconda3/bin/:$PATH
source activate
conda activate simnmt-ozan
cd ~/experiments/simnmt/nmtpy/w2w_models/en-fr
ls
/vol/bitbucket/al4616/simmt/scripts/decode_snmt_rl.sh
/vol/bitbucket/al4616/simmt/scripts/delay_analysis.py -r /vol/bitbucket/al4616/simmt/data/multi30k/en-fr/test_2016_flickr.lc.norm.tok.fr
