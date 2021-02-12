## Output the number of users in each condition that are not excluded from analysis

import numpy as np
from load_process_exp2 import load_data, process_data

minimum_moves = 16

dataset = 'data'
print("Analysing dataset", dataset, "\n")
rawData = load_data("data/"+dataset)
df = process_data(rawData)

before_move_min = len(df.index)
df = df[df['total_moves'] >= minimum_moves]
print("Excluded due to moves <", minimum_moves, "=", (before_move_min - len(df.index)))

before_nobug = len(df.index)
df = df[df['bug'] == "nobug"]
print("Excluded due reporting bugs", before_nobug - len(df.index))

before_language = len(df.index)
df = df[df['language'] == "english"]
print("Excluded due to language", before_language - len(df.index), "(should be 0 as already excluded)")

gameCondition = df[df['version']=='Game']
toolCondition = df[df['version']=='Tool']

print("Total count", len(df.index))
print("Count in game condition", len(gameCondition.index))
print("Count in tool condition", len(toolCondition.index))