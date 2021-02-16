#
# This script generates the analysis for "data/duration.csv". It saves
# output data and graphs in "out/".
#

#
# Note: The duration in `/data/duration.csv` include time spent in the tutorial.
#

import numpy as np
import pandas as pd
import json
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
import matplotlib
import matplotlib.pyplot as plt
from statistics import mean, stdev
from math import sqrt

def duration_histogram(gameCondition, toolCondition):
    plt.clf()
    bins = np.linspace(0, 720, 24)
    plt.hist(gameCondition['duration'], bins, alpha=0.5, label="Game")
    plt.hist(toolCondition['duration'], bins, alpha=0.5, label="Tool")
    plt.suptitle('')
    plt.title("")
    plt.legend(loc='upper right')
    plt.savefig('out/duration_hist+'+dataset+'.pdf', bbox_inches='tight')

def duration_boxplot(df):
    plt.clf()
    boxplot = df.boxplot(column='duration', by='version', grid=False)
    plt.suptitle('')
    plt.title("")
    boxplot.set_xlabel("")
    boxplot.set_ylabel("Duration")
    plt.savefig('out/duration_per_condition+'+dataset+'.pdf', bbox_inches='tight')


dataset = 'duration'
print("Analysing dataset", dataset, "\n")
df=  pd.read_csv("data/"+dataset+".csv", names=["version","duration"])

gameCondition = df[df['version']=='normal']
toolCondition = df[df['version']=='tool']

duration_histogram(gameCondition,toolCondition)
duration_boxplot(df)


c0 = gameCondition['duration']
c1 = toolCondition['duration']
alpha = 0.05
ttest = ttest_ind(c0, c1)
n0 = len(c0)
n1 = len(c1)
cond0 = (n0 - 1) * (stdev(c0) ** 2)
cond1 = (n1 - 1) * (stdev(c1) ** 2)
pooledSD = sqrt((cond0 + cond1) / (n0 + n1 - 2))
cohens_d = (mean(c0) - mean(c1)) / pooledSD

print("game condition: mean", mean(c0), "sd", stdev(c0))
print("tool condition: mean", mean(c1), "sd", stdev(c1))
print(ttest, cohens_d)

