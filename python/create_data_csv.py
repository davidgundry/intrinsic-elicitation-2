#
# This script reads "data/data.json" and saves processed data as "out/data.csv"
# 
# The working directory must be the directory containing the python/data/out folders.
#

from load_process_exp2 import load_data, process_data

def save_dataset(dataset, df):
    filename = r'out/'+dataset.replace("/","-")+".csv";
    print("Saving data to", filename)
    df.to_csv(filename, index = False)

dataset = 'data'
print("Loading dataset", dataset)
rawData = load_data("data/"+dataset)
df = process_data(rawData)
save_dataset(dataset, df)


