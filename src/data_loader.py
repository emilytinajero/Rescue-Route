import json 

def load_data(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)

    return data 