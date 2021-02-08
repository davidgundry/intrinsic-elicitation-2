#
# This script generates the analysis for "data/age-gender.csv". It saves
# output data and graphs in "out/".
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

def gender_bar_plot(df):
    plt.clf()
    boxplot = df['gender'].value_counts().plot.bar(grid=False)
    plt.suptitle('')
    plt.title("")
    boxplot.set_xlabel("Gender")
    boxplot.set_ylabel("Count")
    plt.savefig('out/gender+'+dataset+'.pdf', bbox_inches='tight')

def age_histogram(df):
    plt.clf()
    bins = np.linspace(18, 70, 24)
    plt.hist(df['age'], bins)
    plt.suptitle('')
    plt.title("")
    #plt.set_xlabel("Age")
    #plt.set_ylabel("Count")
    plt.legend(loc='upper right')
    plt.savefig('out/age_hist+'+dataset+'.pdf', bbox_inches='tight')


dataset = 'age-gender'
print("Analysing dataset", dataset, "\n")
df = pd.read_csv("data/"+dataset+".csv", names=["age","gender"])

print(df['gender'].value_counts())

gender_bar_plot(df)
age_histogram(df)