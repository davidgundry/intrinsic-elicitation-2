#
# A script to analyse the difference between number of inputs in the two conditions 
#

import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
from scipy.stats import mannwhitneyu
from statsmodels.graphics.gofplots import qqplot
import matplotlib
import matplotlib.pyplot as plt
from statistics import mean, stdev
from math import sqrt

import seaborn as sns
sns.set(style="ticks", font_scale=1.5)
import ptitprince as pt

from load_process_exp2 import load_data, process_data

def hypothesis_inputs(game, tool):
    print("""Hypothesis: Number of moves will be lower in the game condition
    than the task condition. A two-tailed Mann-Whitney U test will be used to test
    whether the distribution of number of moves differs significantly between the game condition
    than the task condition. α = 0.05""")
    c0 = game['total_moves']
    c1 = tool['total_moves']
    alpha = 0.05
    mwu = mannwhitneyu(c0, c1)
    n0 = len(c0)
    n1 = len(c1)
    cond0 = (n0 - 1) * (stdev(c0) ** 2)
    cond1 = (n1 - 1) * (stdev(c1) ** 2)
    pooledSD = sqrt((cond0 + cond1) / (n0 + n1 - 2))
    cohens_d = (mean(c0) - mean(c1)) / pooledSD
    print("Game mean" ,mean(c0), "sd" ,stdev(c0))
    print("mean Tool" ,mean(c1), "sd", stdev(c1))
    print("Mann-Whitney U test: p =", mwu.pvalue, "; U =",mwu.statistic, "; significant =",(mwu.pvalue < alpha), "; d =",cohens_d, "\n\n")

def inputs_raincloud(df):
    dy="total_moves"; dx="version"; ort="v"; pal = sns.color_palette(n_colors=2)
    f, ax = plt.subplots(figsize=(7, 5))
    ax=pt.half_violinplot( x = dx, y = dy, data = df, palette = pal, bw = .2, cut = 0.,
                        scale = "area", width = .6, inner = None, orient = ort)
    ax=sns.stripplot( x = dx, y = dy, data = df, palette = pal, edgecolor = "white",
                    size = 3, jitter = 1, zorder = 0, orient = ort)
    ax=sns.boxplot( x = dx, y = dy, data = df, color = "black", width = .15, zorder = 10,\
                showcaps = True, boxprops = {'facecolor':'none', "zorder":10},\
                showfliers=True, whiskerprops = {'linewidth':2, "zorder":10},\
                saturation = 1, orient = ort)
    plt.xticks(plt.xticks()[0], ["Game","Control"])

    ax.set_xlabel("")
    ax.set_ylabel("Total Moves")
    plt.savefig('out/total_moves_per_condition_raincloud+'+dataset+'.pdf', bbox_inches='tight')

#not using a minimum
#minimum_moves = 16
dataset = 'data'
print("Analysing dataset", dataset, "\n")
rawData = load_data("data/"+dataset)
df = process_data(rawData)
#df = df[df['total_moves']>=minimum_moves]
df = df[df['bug'] == "nobug"]

gameCondition = df[df['version']=='normal']
toolCondition = df[df['version']=='tool']

hypothesis_inputs(gameCondition, toolCondition)
inputs_raincloud(df)
