import re
from collections import defaultdict
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pprint as pp

unimodal_out = """
AVL score: AVL = 10.39
AVP score: AVP = 0.95
Validation 1 -> LOSS = -0.41
Validation 1 -> BLEU = 51.34, 74.7/58.5/47.4/38.6 (BP=0.966, ratio=0.966, hyp_len=13895, ref_len=14382)
--
AVL score: AVL = 3.84
AVP score: AVP = 0.83
Validation 2 -> LOSS = -0.43
Validation 2 -> BLEU = 30.23, 53.1/33.6/25.0/18.7 (BP=1.000, ratio=1.029, hyp_len=14796, ref_len=14382)
--
AVL score: AVL = 4.24
AVP score: AVP = 0.76
Validation 3 -> LOSS = -0.42
Validation 3 -> BLEU = 42.47, 66.5/48.0/36.6/27.8 (BP=1.000, ratio=1.010, hyp_len=14520, ref_len=14382)
--
AVL score: AVL = 4.42
AVP score: AVP = 0.78
Validation 4 -> LOSS = -0.42
Validation 4 -> BLEU = 44.63, 69.7/51.2/39.3/30.4 (BP=0.983, ratio=0.983, hyp_len=14133, ref_len=14382)
--
AVL score: AVL = 3.75
AVP score: AVP = 0.74
Validation 5 -> LOSS = -0.43
Validation 5 -> BLEU = 39.69, 64.7/45.4/33.7/25.1 (BP=1.000, ratio=1.001, hyp_len=14398, ref_len=14382)
--
AVL score: AVL = 3.08
AVP score: AVP = 0.70
Validation 6 -> LOSS = -0.43
Validation 6 -> BLEU = 34.87, 58.9/40.0/29.1/21.6 (BP=1.000, ratio=1.060, hyp_len=15241, ref_len=14382)
--
AVL score: AVL = 3.52
AVP score: AVP = 0.73
Validation 7 -> LOSS = -0.42
Validation 7 -> BLEU = 42.48, 67.1/48.7/36.4/27.4 (BP=1.000, ratio=1.010, hyp_len=14527, ref_len=14382)
--
AVL score: AVL = 3.66
AVP score: AVP = 0.73
Validation 8 -> LOSS = -0.42
Validation 8 -> BLEU = 41.14, 65.6/46.7/35.0/26.7 (BP=1.000, ratio=1.006, hyp_len=14468, ref_len=14382)
--
AVL score: AVL = 2.84
AVP score: AVP = 0.68
Validation 9 -> LOSS = -0.43
Validation 9 -> BLEU = 35.96, 61.3/41.9/30.1/21.6 (BP=1.000, ratio=1.041, hyp_len=14977, ref_len=14382)
--
AVL score: AVL = 3.76
AVP score: AVP = 0.73
Validation 10 -> LOSS = -0.42
Validation 10 -> BLEU = 43.07, 66.5/48.6/37.3/28.5 (BP=1.000, ratio=1.020, hyp_len=14666, ref_len=14382)
--
AVL score: AVL = 5.45
AVP score: AVP = 0.83
Validation 11 -> LOSS = -0.41
Validation 11 -> BLEU = 50.77, 74.6/58.3/46.7/37.5 (BP=0.966, ratio=0.967, hyp_len=13905, ref_len=14382)
--
AVL score: AVL = 6.04
AVP score: AVP = 0.85
Validation 12 -> LOSS = -0.41
Validation 12 -> BLEU = 51.32, 75.1/58.7/47.2/38.1 (BP=0.966, ratio=0.967, hyp_len=13907, ref_len=14382)
--
AVL score: AVL = 4.47
AVP score: AVP = 0.77
Validation 13 -> LOSS = -0.42
Validation 13 -> BLEU = 47.09, 70.6/53.2/41.8/33.2 (BP=0.986, ratio=0.986, hyp_len=14180, ref_len=14382)
--
AVL score: AVL = 4.91
AVP score: AVP = 0.80
Validation 14 -> LOSS = -0.42
Validation 14 -> BLEU = 48.61, 72.6/55.3/43.9/34.9 (BP=0.976, ratio=0.977, hyp_len=14046, ref_len=14382)
--
AVL score: AVL = 5.47
AVP score: AVP = 0.83
Validation 15 -> LOSS = -0.41
Validation 15 -> BLEU = 49.83, 74.1/57.3/45.7/36.5 (BP=0.966, ratio=0.966, hyp_len=13899, ref_len=14382)
--
AVL score: AVL = 4.48
AVP score: AVP = 0.78
Validation 16 -> LOSS = -0.42
Validation 16 -> BLEU = 47.15, 71.8/54.2/42.3/33.5 (BP=0.973, ratio=0.973, hyp_len=13997, ref_len=14382)
--
AVL score: AVL = 5.37
AVP score: AVP = 0.82
Validation 17 -> LOSS = -0.41
Validation 17 -> BLEU = 50.02, 74.9/58.0/46.5/37.0 (BP=0.957, ratio=0.958, hyp_len=13775, ref_len=14382)
--
AVL score: AVL = 4.93
AVP score: AVP = 0.80
Validation 18 -> LOSS = -0.42
Validation 18 -> BLEU = 48.84, 72.7/55.4/44.0/35.2 (BP=0.977, ratio=0.977, hyp_len=14053, ref_len=14382)
--
AVL score: AVL = 4.36
AVP score: AVP = 0.76
Validation 19 -> LOSS = -0.42
Validation 19 -> BLEU = 47.19, 71.7/54.3/42.6/33.2 (BP=0.975, ratio=0.975, hyp_len=14021, ref_len=14382)
--
AVL score: AVL = 3.99
AVP score: AVP = 0.74
Validation 20 -> LOSS = -0.42
Validation 20 -> BLEU = 46.25, 70.1/52.1/40.6/31.8 (BP=0.993, ratio=0.993, hyp_len=14275, ref_len=14382)
--
AVL score: AVL = 5.49
AVP score: AVP = 0.82
Validation 21 -> LOSS = -0.41
Validation 21 -> BLEU = 49.18, 73.2/56.1/44.8/36.0 (BP=0.970, ratio=0.970, hyp_len=13953, ref_len=14382)
--
AVL score: AVL = 3.87
AVP score: AVP = 0.73
Validation 22 -> LOSS = -0.43
Validation 22 -> BLEU = 45.88, 69.3/51.4/39.9/31.2 (BP=1.000, ratio=1.011, hyp_len=14545, ref_len=14382)
--
AVL score: AVL = 4.05
AVP score: AVP = 0.74
Validation 23 -> LOSS = -0.42
Validation 23 -> BLEU = 46.23, 70.7/52.5/40.7/31.8 (BP=0.987, ratio=0.987, hyp_len=14199, ref_len=14382)
--
AVL score: AVL = 4.79
AVP score: AVP = 0.79
Validation 24 -> LOSS = -0.42
Validation 24 -> BLEU = 49.20, 72.7/55.5/44.4/35.9 (BP=0.977, ratio=0.977, hyp_len=14057, ref_len=14382)
--
AVL score: AVL = 4.26
AVP score: AVP = 0.77
Validation 25 -> LOSS = -0.42
Validation 25 -> BLEU = 47.11, 72.0/54.3/42.3/33.1 (BP=0.974, ratio=0.974, hyp_len=14009, ref_len=14382)
--
AVL score: AVL = 4.95
AVP score: AVP = 0.80
Validation 26 -> LOSS = -0.41
Validation 26 -> BLEU = 48.47, 72.7/55.5/43.9/34.6 (BP=0.974, ratio=0.974, hyp_len=14013, ref_len=14382)
--
AVL score: AVL = 4.22
AVP score: AVP = 0.75
Validation 27 -> LOSS = -0.42
Validation 27 -> BLEU = 48.47, 72.2/54.8/43.4/34.6 (BP=0.982, ratio=0.982, hyp_len=14122, ref_len=14382)
--
AVL score: AVL = 3.87
AVP score: AVP = 0.73
Validation 28 -> LOSS = -0.42
Validation 28 -> BLEU = 47.23, 71.3/53.4/41.5/32.6 (BP=0.991, ratio=0.991, hyp_len=14257, ref_len=14382)
--
AVL score: AVL = 5.13
AVP score: AVP = 0.79
Validation 29 -> LOSS = -0.42
Validation 29 -> BLEU = 50.26, 74.3/57.4/45.7/36.5 (BP=0.973, ratio=0.974, hyp_len=14002, ref_len=14382)
--
AVL score: AVL = 4.85
AVP score: AVP = 0.79
Validation 30 -> LOSS = -0.41
Validation 30 -> BLEU = 50.21, 74.4/57.5/46.1/37.1 (BP=0.966, ratio=0.967, hyp_len=13901, ref_len=14382)
--
AVL score: AVL = 3.69
AVP score: AVP = 0.72
Validation 31 -> LOSS = -0.43
Validation 31 -> BLEU = 46.51, 70.3/52.2/40.5/31.7 (BP=0.998, ratio=0.998, hyp_len=14349, ref_len=14382)
"""
multimodal_out = """AVL score: AVL = 5.23
AVP score: AVP = 0.83
Validation 1 -> LOSS = -0.41
Validation 1 -> BLEU = 43.80, 69.2/51.1/38.7/30.0 (BP=0.973, ratio=0.973, hyp_len=13996, ref_len=14382)
--
AVL score: AVL = 5.99
AVP score: AVP = 0.87
Validation 2 -> LOSS = -0.40
Validation 2 -> BLEU = 49.35, 72.8/56.0/44.9/36.2 (BP=0.973, ratio=0.973, hyp_len=13993, ref_len=14382)
--
AVL score: AVL = 2.85
AVP score: AVP = 0.69
Validation 3 -> LOSS = -0.42
Validation 3 -> BLEU = 31.96, 57.2/38.0/26.2/18.3 (BP=1.000, ratio=1.089, hyp_len=15656, ref_len=14382)
--
AVL score: AVL = 4.73
AVP score: AVP = 0.81
Validation 4 -> LOSS = -0.41
Validation 4 -> BLEU = 47.79, 71.8/54.5/42.9/33.9 (BP=0.978, ratio=0.979, hyp_len=14075, ref_len=14382)
--
AVL score: AVL = 4.65
AVP score: AVP = 0.79
Validation 5 -> LOSS = -0.41
Validation 5 -> BLEU = 46.15, 69.5/51.9/40.3/31.5 (BP=0.998, ratio=0.998, hyp_len=14352, ref_len=14382)
--
AVL score: AVL = 3.87
AVP score: AVP = 0.74
Validation 6 -> LOSS = -0.42
Validation 6 -> BLEU = 42.40, 65.9/47.7/36.4/28.2 (BP=1.000, ratio=1.016, hyp_len=14607, ref_len=14382)
--
AVL score: AVL = 4.80
AVP score: AVP = 0.81
Validation 7 -> LOSS = -0.41
Validation 7 -> BLEU = 47.72, 71.9/54.5/42.6/33.6 (BP=0.981, ratio=0.981, hyp_len=14107, ref_len=14382)
--
AVL score: AVL = 4.31
AVP score: AVP = 0.77
Validation 8 -> LOSS = -0.42
Validation 8 -> BLEU = 46.83, 70.5/53.3/41.5/32.6 (BP=0.986, ratio=0.986, hyp_len=14185, ref_len=14382)
--
AVL score: AVL = 3.85
AVP score: AVP = 0.75
Validation 9 -> LOSS = -0.42
Validation 9 -> BLEU = 45.29, 69.2/51.3/39.5/30.6 (BP=0.995, ratio=0.995, hyp_len=14315, ref_len=14382)
--
AVL score: AVL = 4.98
AVP score: AVP = 0.80
Validation 10 -> LOSS = -0.41
Validation 10 -> BLEU = 48.26, 72.3/55.1/43.6/34.7 (BP=0.974, ratio=0.975, hyp_len=14017, ref_len=14382)
--
AVL score: AVL = 3.97
AVP score: AVP = 0.74
Validation 11 -> LOSS = -0.42
Validation 11 -> BLEU = 45.07, 68.9/50.9/39.1/30.1 (BP=1.000, ratio=1.000, hyp_len=14377, ref_len=14382)
--
AVL score: AVL = 4.56
AVP score: AVP = 0.78
Validation 12 -> LOSS = -0.41
Validation 12 -> BLEU = 47.07, 71.0/53.4/41.7/33.0 (BP=0.984, ratio=0.984, hyp_len=14157, ref_len=14382)
--
AVL score: AVL = 3.53
AVP score: AVP = 0.72
Validation 13 -> LOSS = -0.43
Validation 13 -> BLEU = 39.82, 63.5/45.2/34.0/25.8 (BP=1.000, ratio=1.039, hyp_len=14941, ref_len=14382)
--
AVL score: AVL = 5.15
AVP score: AVP = 0.80
Validation 14 -> LOSS = -0.41
Validation 14 -> BLEU = 49.64, 72.9/56.0/44.6/35.7 (BP=0.983, ratio=0.983, hyp_len=14136, ref_len=14382)
--
AVL score: AVL = 4.56
AVP score: AVP = 0.78
Validation 15 -> LOSS = -0.41
Validation 15 -> BLEU = 48.01, 72.1/54.8/43.0/34.0 (BP=0.980, ratio=0.980, hyp_len=14095, ref_len=14382)
--
AVL score: AVL = 5.87
AVP score: AVP = 0.84
Validation 16 -> LOSS = -0.40
Validation 16 -> BLEU = 50.08, 73.7/57.2/45.8/37.0 (BP=0.969, ratio=0.969, hyp_len=13943, ref_len=14382)
--
AVL score: AVL = 4.42
AVP score: AVP = 0.77
Validation 17 -> LOSS = -0.42
Validation 17 -> BLEU = 46.68, 70.9/53.2/41.5/32.4 (BP=0.984, ratio=0.984, hyp_len=14151, ref_len=14382)
--
AVL score: AVL = 4.78
AVP score: AVP = 0.78
Validation 18 -> LOSS = -0.42
Validation 18 -> BLEU = 48.14, 72.0/54.5/43.0/34.2 (BP=0.983, ratio=0.983, hyp_len=14136, ref_len=14382)
--
AVL score: AVL = 5.50
AVP score: AVP = 0.82
Validation 19 -> LOSS = -0.41
Validation 19 -> BLEU = 49.18, 72.9/55.9/44.6/35.8 (BP=0.974, ratio=0.974, hyp_len=14010, ref_len=14382)
--
AVL score: AVL = 4.37
AVP score: AVP = 0.76
Validation 20 -> LOSS = -0.42
Validation 20 -> BLEU = 48.19, 71.0/53.9/42.7/33.8 (BP=0.994, ratio=0.994, hyp_len=14299, ref_len=14382)
--
AVL score: AVL = 4.41
AVP score: AVP = 0.76
Validation 21 -> LOSS = -0.42
Validation 21 -> BLEU = 47.33, 70.9/53.4/41.8/32.9 (BP=0.991, ratio=0.991, hyp_len=14251, ref_len=14382)
--
AVL score: AVL = 4.57
AVP score: AVP = 0.77
Validation 22 -> LOSS = -0.42
Validation 22 -> BLEU = 48.43, 72.3/54.9/43.2/34.3 (BP=0.983, ratio=0.983, hyp_len=14144, ref_len=14382)
--
AVL score: AVL = 4.49
AVP score: AVP = 0.78
Validation 23 -> LOSS = -0.42
Validation 23 -> BLEU = 46.66, 71.1/53.5/41.6/32.4 (BP=0.980, ratio=0.981, hyp_len=14104, ref_len=14382)
--
AVL score: AVL = 4.80
AVP score: AVP = 0.78
Validation 24 -> LOSS = -0.42
Validation 24 -> BLEU = 49.12, 72.9/55.9/44.3/35.2 (BP=0.979, ratio=0.979, hyp_len=14077, ref_len=14382)
--
AVL score: AVL = 3.93
AVP score: AVP = 0.74
Validation 25 -> LOSS = -0.42
Validation 25 -> BLEU = 44.70, 68.6/50.5/38.7/29.8 (BP=1.000, ratio=1.003, hyp_len=14432, ref_len=14382)
--
AVL score: AVL = 4.74
AVP score: AVP = 0.77
Validation 26 -> LOSS = -0.41
Validation 26 -> BLEU = 48.97, 72.6/55.5/44.0/35.1 (BP=0.981, ratio=0.981, hyp_len=14109, ref_len=14382)
--
AVL score: AVL = 4.05
AVP score: AVP = 0.74
Validation 27 -> LOSS = -0.42
Validation 27 -> BLEU = 46.65, 69.4/52.0/40.8/32.1 (BP=1.000, ratio=1.000, hyp_len=14382, ref_len=14382)
--
AVL score: AVL = 5.01
AVP score: AVP = 0.80
Validation 28 -> LOSS = -0.41
Validation 28 -> BLEU = 48.12, 71.9/54.8/43.2/34.2 (BP=0.980, ratio=0.980, hyp_len=14093, ref_len=14382)
--
AVL score: AVL = 5.11
AVP score: AVP = 0.81
Validation 29 -> LOSS = -0.41
Validation 29 -> BLEU = 48.73, 72.8/55.8/44.2/35.1 (BP=0.973, ratio=0.973, hyp_len=13998, ref_len=14382)
--
AVL score: AVL = 3.99
AVP score: AVP = 0.75
Validation 30 -> LOSS = -0.42
Validation 30 -> BLEU = 45.59, 69.5/51.4/39.7/30.9 (BP=0.996, ratio=0.996, hyp_len=14327, ref_len=14382)
--
AVL score: AVL = 3.99
AVP score: AVP = 0.75
Validation 31 -> LOSS = -0.42
Validation 31 -> BLEU = 44.50, 68.3/50.0/38.5/29.8 (BP=1.000, ratio=1.001, hyp_len=14396, ref_len=14382)
--
AVL score: AVL = 4.69
AVP score: AVP = 0.78
Validation 32 -> LOSS = -0.41
Validation 32 -> BLEU = 49.33, 73.6/56.7/45.0/36.0 (BP=0.967, ratio=0.968, hyp_len=13915, ref_len=14382)
--
AVL score: AVL = 4.94
AVP score: AVP = 0.79
Validation 33 -> LOSS = -0.41
Validation 33 -> BLEU = 49.26, 73.3/56.3/44.7/35.6 (BP=0.973, ratio=0.973, hyp_len=13996, ref_len=14382)
--
AVL score: AVL = 4.82
AVP score: AVP = 0.79
Validation 34 -> LOSS = -0.41
Validation 34 -> BLEU = 47.66, 72.1/54.6/42.9/33.8 (BP=0.975, ratio=0.976, hyp_len=14031, ref_len=14382)
--
AVL score: AVL = 4.38
AVP score: AVP = 0.76
Validation 35 -> LOSS = -0.42
Validation 35 -> BLEU = 48.27, 72.2/54.9/43.1/34.2 (BP=0.982, ratio=0.982, hyp_len=14123, ref_len=14382)
--
AVL score: AVL = 4.34
AVP score: AVP = 0.76
Validation 36 -> LOSS = -0.42
Validation 36 -> BLEU = 46.91, 70.4/52.7/41.2/32.7 (BP=0.992, ratio=0.992, hyp_len=14264, ref_len=14382)
--
AVL score: AVL = 4.74
AVP score: AVP = 0.78
Validation 37 -> LOSS = -0.42
Validation 37 -> BLEU = 49.36, 73.1/56.2/44.7/35.9 (BP=0.974, ratio=0.974, hyp_len=14015, ref_len=14382)
--
AVL score: AVL = 4.93
AVP score: AVP = 0.79
Validation 38 -> LOSS = -0.41
Validation 38 -> BLEU = 47.58, 71.1/53.9/42.4/33.5 (BP=0.985, ratio=0.985, hyp_len=14169, ref_len=14382)
--
AVL score: AVL = 5.15
AVP score: AVP = 0.80
Validation 39 -> LOSS = -0.41
Validation 39 -> BLEU = 49.86, 74.1/57.3/45.8/36.8 (BP=0.964, ratio=0.965, hyp_len=13874, ref_len=14382)
--
AVL score: AVL = 4.68
AVP score: AVP = 0.78
Validation 40 -> LOSS = -0.42
Validation 40 -> BLEU = 46.96, 69.9/52.3/41.2/32.7 (BP=0.997, ratio=0.997, hyp_len=14339, ref_len=14382)
--
AVL score: AVL = 5.17
AVP score: AVP = 0.80
Validation 41 -> LOSS = -0.41
Validation 41 -> BLEU = 50.49, 73.4/56.8/45.3/36.6 (BP=0.984, ratio=0.984, hyp_len=14157, ref_len=14382)
--
AVL score: AVL = 4.36
AVP score: AVP = 0.76
Validation 42 -> LOSS = -0.42
Validation 42 -> BLEU = 48.02, 71.8/54.5/42.9/34.0 (BP=0.983, ratio=0.983, hyp_len=14135, ref_len=14382)
--
AVL score: AVL = 4.26
AVP score: AVP = 0.75
Validation 43 -> LOSS = -0.42
Validation 43 -> BLEU = 48.56, 71.6/54.6/43.2/34.4 (BP=0.989, ratio=0.989, hyp_len=14227, ref_len=14382)
--
AVL score: AVL = 3.94
AVP score: AVP = 0.73
Validation 44 -> LOSS = -0.42
Validation 44 -> BLEU = 45.96, 69.3/51.6/40.1/31.4 (BP=0.998, ratio=0.998, hyp_len=14359, ref_len=14382)
--
AVL score: AVL = 5.12
AVP score: AVP = 0.80
Validation 45 -> LOSS = -0.41
Validation 45 -> BLEU = 49.39, 73.1/56.5/44.8/35.7 (BP=0.974, ratio=0.975, hyp_len=14017, ref_len=14382)
--
AVL score: AVL = 4.95
AVP score: AVP = 0.79
Validation 46 -> LOSS = -0.41
Validation 46 -> BLEU = 49.81, 73.7/56.8/45.1/36.0 (BP=0.975, ratio=0.976, hyp_len=14033, ref_len=14382)
--
AVL score: AVL = 5.18
AVP score: AVP = 0.80
Validation 47 -> LOSS = -0.41
Validation 47 -> BLEU = 49.49, 72.9/56.0/44.4/35.4 (BP=0.983, ratio=0.983, hyp_len=14141, ref_len=14382)
--
AVL score: AVL = 5.26
AVP score: AVP = 0.81
Validation 48 -> LOSS = -0.41
Validation 48 -> BLEU = 49.30, 73.2/56.2/44.6/35.6 (BP=0.975, ratio=0.976, hyp_len=14033, ref_len=14382)
--
AVL score: AVL = 5.23
AVP score: AVP = 0.81
Validation 49 -> LOSS = -0.41
Validation 49 -> BLEU = 48.03, 72.2/54.9/43.4/34.4 (BP=0.974, ratio=0.974, hyp_len=14006, ref_len=14382)
--
AVL score: AVL = 4.36
AVP score: AVP = 0.76
Validation 50 -> LOSS = -0.42
Validation 50 -> BLEU = 48.30, 71.6/54.8/43.1/34.1 (BP=0.986, ratio=0.986, hyp_len=14181, ref_len=14382)
--
AVL score: AVL = 4.61
AVP score: AVP = 0.77
Validation 51 -> LOSS = -0.42
Validation 51 -> BLEU = 48.77, 72.1/55.3/43.7/34.8 (BP=0.982, ratio=0.982, hyp_len=14130, ref_len=14382)
--
AVL score: AVL = 4.29
AVP score: AVP = 0.75
Validation 52 -> LOSS = -0.42
Validation 52 -> BLEU = 49.39, 73.0/56.3/45.1/36.1 (BP=0.971, ratio=0.971, hyp_len=13969, ref_len=14382)
--
AVL score: AVL = 4.65
AVP score: AVP = 0.77
Validation 53 -> LOSS = -0.42
Validation 53 -> BLEU = 48.54, 71.8/54.8/43.5/34.5 (BP=0.985, ratio=0.985, hyp_len=14161, ref_len=14382)
--
AVL score: AVL = 4.38
AVP score: AVP = 0.77
Validation 54 -> LOSS = -0.42
Validation 54 -> BLEU = 47.36, 70.7/53.1/41.7/32.9 (BP=0.994, ratio=0.994, hyp_len=14298, ref_len=14382)
--
AVL score: AVL = 5.32
AVP score: AVP = 0.81
Validation 55 -> LOSS = -0.41
Validation 55 -> BLEU = 49.39, 73.3/56.5/44.9/35.7 (BP=0.973, ratio=0.973, hyp_len=13997, ref_len=14382)
--
AVL score: AVL = 4.57
AVP score: AVP = 0.77
Validation 56 -> LOSS = -0.42
Validation 56 -> BLEU = 48.74, 71.8/54.9/43.6/34.7 (BP=0.986, ratio=0.986, hyp_len=14183, ref_len=14382)
--
AVL score: AVL = 4.89
AVP score: AVP = 0.79
Validation 57 -> LOSS = -0.42
Validation 57 -> BLEU = 49.46, 73.0/56.2/45.0/36.1 (BP=0.974, ratio=0.974, hyp_len=14008, ref_len=14382)
--
AVL score: AVL = 4.57
AVP score: AVP = 0.78
Validation 58 -> LOSS = -0.42
Validation 58 -> BLEU = 49.03, 72.9/55.9/44.2/35.2 (BP=0.977, ratio=0.977, hyp_len=14056, ref_len=14382)
--
AVL score: AVL = 4.32
AVP score: AVP = 0.75
Validation 59 -> LOSS = -0.42
Validation 59 -> BLEU = 47.46, 69.9/52.9/41.6/33.0 (BP=1.000, ratio=1.000, hyp_len=14389, ref_len=14382)
--
AVL score: AVL = 4.93
AVP score: AVP = 0.79
Validation 60 -> LOSS = -0.41
Validation 60 -> BLEU = 49.54, 73.7/56.8/45.1/36.1 (BP=0.969, ratio=0.970, hyp_len=13948, ref_len=14382)
--
AVL score: AVL = 4.39
AVP score: AVP = 0.76
Validation 61 -> LOSS = -0.42
Validation 61 -> BLEU = 49.33, 72.8/55.7/44.2/35.3 (BP=0.984, ratio=0.984, hyp_len=14151, ref_len=14382)
--
AVL score: AVL = 4.85
AVP score: AVP = 0.78
Validation 62 -> LOSS = -0.42
Validation 62 -> BLEU = 48.85, 72.7/55.6/43.9/34.8 (BP=0.980, ratio=0.980, hyp_len=14096, ref_len=14382)
--
AVL score: AVL = 4.98
AVP score: AVP = 0.79
Validation 63 -> LOSS = -0.41
Validation 63 -> BLEU = 49.00, 73.6/56.5/44.7/35.6 (BP=0.965, ratio=0.966, hyp_len=13894, ref_len=14382)
--
AVL score: AVL = 4.83
AVP score: AVP = 0.78
Validation 64 -> LOSS = -0.42
Validation 64 -> BLEU = 49.87, 73.2/56.5/45.1/36.1 (BP=0.979, ratio=0.979, hyp_len=14079, ref_len=14382)
--
AVL score: AVL = 4.38
AVP score: AVP = 0.76
Validation 65 -> LOSS = -0.42
Validation 65 -> BLEU = 47.28, 70.1/52.8/41.5/32.9 (BP=0.997, ratio=0.997, hyp_len=14338, ref_len=14382)
--
AVL score: AVL = 4.30
AVP score: AVP = 0.76
Validation 66 -> LOSS = -0.42
Validation 66 -> BLEU = 47.20, 69.6/52.5/41.4/32.9 (BP=1.000, ratio=1.003, hyp_len=14424, ref_len=14382)
--
AVL score: AVL = 4.51
AVP score: AVP = 0.76
Validation 67 -> LOSS = -0.42
Validation 67 -> BLEU = 48.53, 72.4/55.2/43.3/34.3 (BP=0.984, ratio=0.984, hyp_len=14149, ref_len=14382)
--
AVL score: AVL = 5.11
AVP score: AVP = 0.80
Validation 68 -> LOSS = -0.42
Validation 68 -> BLEU = 48.58, 72.5/55.6/43.9/34.8 (BP=0.975, ratio=0.976, hyp_len=14031, ref_len=14382)
--
AVL score: AVL = 4.54
AVP score: AVP = 0.77
Validation 69 -> LOSS = -0.42
Validation 69 -> BLEU = 48.94, 72.2/55.2/43.8/34.9 (BP=0.986, ratio=0.986, hyp_len=14175, ref_len=14382)
--
AVL score: AVL = 4.60
AVP score: AVP = 0.77
Validation 70 -> LOSS = -0.42
Validation 70 -> BLEU = 48.97, 72.7/55.5/43.9/35.0 (BP=0.981, ratio=0.982, hyp_len=14117, ref_len=14382)
--
AVL score: AVL = 5.06
AVP score: AVP = 0.79
Validation 71 -> LOSS = -0.42
Validation 71 -> BLEU = 50.07, 74.1/57.3/45.7/36.6 (BP=0.970, ratio=0.971, hyp_len=13958, ref_len=14382)"""
length_rew_uni = '../experiments/rl/en-fr-unimodal-rl-length-coeff-0.0005.out'
with open(length_rew_uni) as input:
    build_metrics = re.compile(r'AVL.*AVL.*\n.*\n.*\n.*\n.*\n')
    metric_lines = re.findall(build_metrics, ''.join(input.readlines()))

extracted_length_rew_out = ''.join(metric_lines)

scores = defaultdict(list)
metrics = ['AVP', 'AVL', 'SDIFF', 'BLEU']
for line in extracted_length_rew_out.split('\n'):
    for metric in metrics:
        if metric in line:
            i = line.index('=')
            scores[metric].append(float(line[i + 1:i + 6]))

scores['BLEU AVL ratio'] = [q / d for q, d in zip(scores['BLEU'], scores['AVL'])]
scores['BLEU AVP ratio'] = [q / d for q, d in zip(scores['BLEU'], scores['AVP'])]
xs = range(len(scores['BLEU']))
h, w = (2, 3)
f, axes = plt.subplots(h, w)
plt.suptitle('Unimodal simnmt RL, length_coeff = 0.0005', size=16)


def metric_subplot(ax, data, name, color):
    sns.lineplot(x=xs, y=data, ax=ax, color=color)
    ax.set_xlabel('Epoch')
    ax.set_ylabel(name)


score_it = iter(scores.items())
colors_it = iter(sns.color_palette('muted', n_colors=h * w))
# generate subplot for each name, data pair in scores
for y in range(h):
    for x in range(w):
        name, data = next(score_it)
        metric_subplot(axes[y, x], data, name, next(colors_it))

f.tight_layout()
plt.subplots_adjust(top=0.2, hspace=0.5)
plt.show()
