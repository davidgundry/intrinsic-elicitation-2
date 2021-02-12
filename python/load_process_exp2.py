import pandas as pd
import json

def load_data(filename):
    rawData = []
    with open(filename+".json") as f:
        content = f.read()
        rawData = json.loads(content)
    return rawData

def process_data(rawData):
    data, language, version = [], [], [],
    excludedPIDs = []
    for d in rawData:
        data.append(d["data"])
        language.append(d["data"]["answers"][0])
        dVersion = d["data"]["gameVersion"]
        if (dVersion == "Normal"):
            dVersion = "Game"
        version.append(dVersion)
            
    duration, gaming_frequency = [], []
    imi1, imi2, imi3, imi4, imi5, imi6, imi7, imi_enjoyment = [], [], [], [], [], [], [], []
    g1, g2, g3, g4, g5, g6 = [], [], [], [], [], []
    bug, bugdesc = [], []
    grammatical_moves, moves_with_noun, total_moves = [], [] ,[]
    proportion_of_valid_data, proportion_of_valid_data_providing_mechanic_actuations = [], []
    grammatical_moves_last10, moves_with_noun_last10 = [], []
    proportion_of_valid_data_last10 = []
    proportion_of_valid_data_providing_mechanic_actuations_last10 = []
    time_per_input_from_moveDurations = []
    time_per_input_from_8min = []
    for i, d in enumerate(data):
        gaming_frequency.append(d["answers"][1])

        # Calculate IMI Enjoyment subscale mean
        # Scores for questions 3 and 4 are reversed
        a = [int(numeric_string) for numeric_string in d["answers"][2:9]]
        imi1.append(a[0])
        imi2.append(a[1])
        imi3.append(a[2])
        imi4.append(a[3])
        imi5.append(a[4])
        imi6.append(a[5])
        imi7.append(a[6])
        imi_value = (a[0] + a[1] + (6-a[2]) + (6-a[3]) + a[4] + a[5] + a[6])/7
        imi_enjoyment.append(imi_value)

        b = d["answers"][9:15]
        g1.append(b[0])
        g2.append(b[1])
        g3.append(b[2])
        g4.append(b[3])
        g5.append(b[4])
        g6.append(b[5])

        bug.append(d["answers"][15])
        bugdesc.append(d["answers"][16])

        # Calculate proportions of valid moves (from total):
        count_gram = sum([is_grammatical(a,b) and has_noun(a) for a in d["moves"]])
        count_w_noun = sum([has_noun(a) for a in d["moves"]])
        count_all = len(d["moves"])
        total_moves.append(count_all)
        grammatical_moves.append(count_gram)
        moves_with_noun.append(count_w_noun)
        proportion_of_valid_data.append(count_gram/count_all)
        proportion_of_valid_data_providing_mechanic_actuations.append(count_gram/count_w_noun)

        # Calculate proportions of valid moves (from last 10):
        count_gram_last_10 = sum([is_grammatical(a,b) and has_noun(a) for a in d["moves"][-10:]])
        count_w_noun_last_10 = sum([has_noun(a) for a in d["moves"][-10:]])
        grammatical_moves_last10.append(count_gram_last_10)
        moves_with_noun_last10.append(count_w_noun_last_10)
        proportion_of_valid_data_last10.append(count_gram_last_10/10)
        proportion_of_valid_data_providing_mechanic_actuations_last10.append(count_gram_last_10/count_w_noun_last_10)

        #Calculate Time per input
        time_per_input_from_moveDurations.append(sum(d["moveDurations"])/len(d["moveDurations"]))
        time_per_input_from_8min.append(8/count_all)

    d = { 
            "version": version,
            "language": language,
            "gaming_frequency": gaming_frequency,
            "imi1": imi1, "imi2": imi2, "imi3": imi3, "imi4": imi4, "imi5": imi5, "imi6": imi6, "imi7": imi7,
            "g-rbs": g1, "g-brs": g2, "g-bfs": g3, "g-frs": g4, "g-rfs": g5, "g-fbs": g6,
            "bug": bug,
            "bugdesc": bugdesc,
            "imi_enjoyment": imi_enjoyment,
            "total_moves" : total_moves,
            "moves_with_noun": moves_with_noun,
            "grammatical_moves": grammatical_moves,
            "proportion_of_valid_data_total" : proportion_of_valid_data,
            "proportion_of_valid_data_providing_mechanic_actuations_total": proportion_of_valid_data_providing_mechanic_actuations,
            "moves_with_noun_last10": moves_with_noun_last10,
            "grammatical_moves_last10": grammatical_moves_last10,
            "proportion_of_valid_data_last10" : proportion_of_valid_data_last10,
            "proportion_of_valid_data_providing_mechanic_actuations_last10": proportion_of_valid_data_providing_mechanic_actuations_last10,
            "time_per_input_from_moveDurations": time_per_input_from_moveDurations,
            "time_per_input_from_8min": time_per_input_from_8min
        }
    df = pd.DataFrame(data=d)
    return df

def is_grammatical(array, b):
    a = []
    adj1 = ["big", "small"]
    adj2 = ["empty", "filled"]
    adj3 = ["red", "blue", "green"]
    nouns = ["square","circle","triangle"]

    ## red big square
    if (b[0] == "g") and (array[0] in adj3) and (array[1] in adj1) and (array[2] in nouns):
        return True
    # big red square
    if (b[1] == "g") and (array[0] in adj1) and (array[1] in adj3) and (array[2] in nouns):
        return True
    # big filled square
    if (b[2] == "g") and (array[0] in adj1) and (array[1] in adj2) and (array[2] in nouns):
        return True
    # filled red square
    if (b[3] == "g") and (array[0] in adj2) and (array[1] in adj3) and (array[2] in nouns):
        return True
    # red filled square
    if (b[4] == "g") and (array[0] in adj3) and (array[1] in adj2) and (array[2] in nouns):
        return True
    # filled big square
    if (b[5] == "g") and (array[0] in adj2) and (array[1] in adj1) and (array[2] in nouns):
        return True
    return False

def has_noun(array):
    nouns = ["square","circle","triangle"]
    for word in array:
        if word in nouns:
            return True
    return False