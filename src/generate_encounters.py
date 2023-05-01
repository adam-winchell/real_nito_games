import csv
from pathlib import Path
import os
import random
import pickle
import re

# def preprocess_latex_tables(filename):
#     with open(filename+".csv", newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter='&')

#         mapper = {}
#         for row in reader:
#             text = row[1].replace('\\\\', '').rstrip().lstrip()
#             try:
#                 x = int(row[0])
#                 mapper[x] = text
#             except:
#                 # row[0] looks like x-y, e.g. 1-5
#                 x, y = map(int, row[0].split('-'))
#                 for i in range(x,y+1):
#                     mapper[i] = text
                
#         with open(filename, "wb") as f: 
#             pickle.dump(mapper, f)

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def find_encounter_tables():
    path = Path(__file__).parent.absolute().parent
    path = Path(find("plot_relatedness", path)).parent
    return path

def multiple_number_monsters(text, multiplier):
    split_text = re.split(r"(\d+)", text)

    result = ''
    for i in range(len(split_text)):
        token = split_text[i]

        if token.isdigit() and split_text[i-1] != 'd':
            num = int(token)
            num = str(multiplier*num)
            new_token = re.sub("\d+", num, token)
            result += new_token
        else:
            result += token
    return result

def get_entry(filename, max_roll=-1, multiplier=1):
    with open(filename, "rb") as f:
        mapper = pickle.load(f)

        if max_roll == -1:
            max_roll = len(mapper)

        result = mapper[random.randint(1, max_roll)]

        if multiplier > 1:
            result = multiple_number_monsters(result, multiplier)

        return result

def extract_zone_information(text):
    matches = re.findall(r'Roll on (\w+) Encounter Table and (\w+) the number of creatures. Re-roll if you get (\d+)-100.', text)[0]
    
    if matches[1] == 'double':
        multiplier = 2
    else:
        multiplier = 3

    return matches[0].lower(), multiplier, int(matches[2])

def generate_encounter(zone='twilight'):
    root_path = find_encounter_tables()

    print("\nAttitude to Party:")
    text = get_entry(os.path.join(root_path, 'attitude'))
    print(text)

    print("\nPlot Relatedness:")
    text = get_entry(os.path.join(root_path, 'plot_relatedness'))
    print(text)

    print("\nActivity:")
    text = get_entry(os.path.join(root_path, 'activity'))
    print(text)

    print("\nLocation:")
    text = get_entry(os.path.join(root_path, 'location'))
    print(text)

    print("\nBreach:")
    text = get_entry(os.path.join(root_path, 'breach'))
    print(text)

    
    num_rolls = get_entry(os.path.join(root_path, 'num_encounters'))
    num_converter = {"Once":1, "Twice":2, "Three times":3, "Four times":4}

    print("\nZone Encounter:")
    for _ in range(num_converter[num_rolls]):
        text = get_entry(os.path.join(root_path, zone))

        if 'Madness' in text:
            text= text.replace("rolls on the Madness table where the effect", "gain the following madness that")
            print(text)
            madness_text = get_entry(os.path.join(root_path, 'madness'))
            print(madness_text)
        elif 'Re-roll if you get' in text:
            zone, multiplier, max_roll = extract_zone_information(text)
            text = get_entry(os.path.join(root_path, zone), max_roll=max_roll, multiplier=multiplier)
            print(text)
        else:
            print(text)

def get_zone():
    zone = input("Enter Zone to generate random encounter for: ")

    if zone.lower() == 'twilight':
        return 'twilight'
    elif zone.lower() == 'dusk':
        return 'dusk'
    elif zone.lower() == 'gloom':
        return 'gloom'
    elif zone.lower() == 'shadow':
        return 'shadow'
    elif zone.lower() == 'void':
        return 'void'
    else:
        print('You entered an invalid zone, defaulting to Twilight')
        return 'twilight'

if __name__ == "__main__":
    zone = get_zone()
    generate_encounter(zone)
            

    # all_tables = ['attitude', 'plot_relatedness', 'activity', 'location', 'breach', 'num_encounters', 'madness', 'twilight', 'dusk', 'gloom', 'shadow', 'void']
    # for table in tables:
        # preprocess_latex_tables(os.path.join(root_path, table))