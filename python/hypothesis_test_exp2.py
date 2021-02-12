#
# This script performs the pre-registered analysis for "data/data.json". It saves graphs in "out/".
#
# The working directory must be the directory containing the python/data/out folders.
#
# Requires pandas, scipy, statsmodels, matplotlib. Get them using
#  `pip install pandas scipy statsmodels matplotlib`

import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
from scipy.stats import mannwhitneyu
from statsmodels.graphics.gofplots import qqplot
import matplotlib
import matplotlib.pyplot as plt
from statistics import mean, stdev
from math import sqrt

from load_process_exp2 import load_data, process_data

def hypothesis_test_1(game, tool):
    print("""Hypothesis 1: Enjoyment (DV1) will be greater in the game condition than the task condition.
    A one-tailed two-sample t-test will be used to test whether the mean scores of DV1 is greater
    in the game condition than the task condition. α = 0.05.""")
    alpha = 0.05
    c0 = game['imi_enjoyment']
    c1 = tool['imi_enjoyment']
    ttest = ttest_ind(c0,c1)
    n0 = len(c0)
    n1 = len(c1)
    cond0 = (n0 - 1) * (stdev(c0) ** 2)
    cond1 = (n1 - 1) * (stdev(c1) ** 2)
    pooledSD = sqrt((cond0 + cond1) / (n0 + n1 - 2))
    cohens_d = (mean(c0) - mean(c1)) / pooledSD
    p = ttest.pvalue/2 # because it's a one tailed test, we also check that ttest.statistic has the correct sign
    print("Game mean" ,mean(c0), "sd" ,stdev(c0))
    print("mean Tool" ,mean(c1), "sd", stdev(c1))
    print("one tailed t test: p =", p, "; t =",ttest.statistic, "; significant =",(p < alpha) and (ttest.statistic > 0), "; d =",cohens_d, "\n\n")

def hypothesis_test_2(game, tool):
    print("""Hypothesis 2: Proportion of valid data (DV2) will be lower in the game condition
    than the task condition. A two-tailed Mann-Whitney U test will be used to test
    whether the distribution of DV2 differs significantly between the game condition
    than the task condition. α = 0.05""")
    c0 = game['proportion_of_valid_data_last10']
    c1 = tool['proportion_of_valid_data_last10']
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

def hypothesis_test_3(game, tool):
    print("""Hypothesis 3: Time per input (DV3) will be higher in the game condition than
    the task condition. A two-tailed two-sample t-test will be used to test whether
    scores of DV3 are greater in the game condition than the task condition. α =
    0.05""")
    alpha = 0.05
    c0 = game['time_per_input_from_8min']
    c1 = tool['time_per_input_from_8min']
    ttest = ttest_ind(c0, c1)
    n0 = len(c0)
    n1 = len(c1)
    cond0 = (n0 - 1) * (stdev(c0) ** 2)
    cond1 = (n1 - 1) * (stdev(c1) ** 2)
    pooledSD = sqrt((cond0 + cond1) / (n0 + n1 - 2))
    cohens_d = (mean(c0) - mean(c1)) / pooledSD
    print("Game mean" ,mean(c0), "sd" ,stdev(c0))
    print("mean Tool" ,mean(c1), "sd", stdev(c1))
    print("two tailed t test: p =", ttest.pvalue, "; t =",ttest.statistic, "; significant =",(ttest.pvalue < alpha), "; d =",cohens_d, "\n\n")

def enjoyment_box_plot(df):
    plt.clf()
    boxplot = df.boxplot(column='imi_enjoyment', by='version', grid=False)
    plt.suptitle('')
    plt.title("")
    boxplot.set_xlabel("")
    boxplot.set_ylabel("IMI Enjoyment subscale")
    plt.savefig('out/imi_enjoyment_per_condition+'+dataset+'.pdf', bbox_inches='tight')

def valid_proportion_all_data_boxplot(df):
    plt.clf()
    boxplot = df.boxplot(column='proportion_of_valid_data_last10', by='version', grid=False)
    plt.suptitle('')
    plt.title("")
    boxplot.set_xlabel("")
    boxplot.set_ylabel("Proportion of Valid Data (last 10)")
    plt.savefig('out/prop_valid_data_last10_per_condition+'+dataset+'.pdf', bbox_inches='tight')

def time_per_input_boxplot(df):
    plt.clf()
    boxplot = df.boxplot(column='time_per_input_from_8min', by='version', grid=False)
    plt.suptitle('')
    plt.title("")
    boxplot.set_xlabel("")
    boxplot.set_ylabel("Time per input (from 8 min)")
    plt.savefig('out/time_per_input_per_condition+'+dataset+'.pdf', bbox_inches='tight')

def gaming_frequency_bar_plot(df):
    plt.clf()
    boxplot = df['gaming_frequency'].value_counts().plot.bar(grid=False)
    plt.suptitle('')
    plt.title("")
    #boxplot.set_xlabel("Gaming Frequency")
    boxplot.set_ylabel("Count")
    plt.savefig('out/gaming_frequency+'+dataset+'.pdf', bbox_inches='tight')

minimum_moves = 16
dataset = 'data'
print("Analysing dataset", dataset, "\n")
rawData = load_data("data/"+dataset)
df = process_data(rawData)
df = df[df['total_moves']>=minimum_moves]
df = df[df['bug'] == "nobug"]

gameCondition = df[df['version']=='Game']
toolCondition = df[df['version']=='Tool']

hypothesis_test_1(gameCondition, toolCondition)
hypothesis_test_2(gameCondition, toolCondition)
hypothesis_test_3(gameCondition, toolCondition)
enjoyment_box_plot(df)
valid_proportion_all_data_boxplot(df)
time_per_input_boxplot(df)
gaming_frequency_bar_plot(df)
print(df['gaming_frequency'].value_counts())
