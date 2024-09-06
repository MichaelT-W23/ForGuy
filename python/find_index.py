import json
import os 
from termcolor import colored as c

path = os.getcwd()
last_folder = os.path.basename(path)

dots = '../' if last_folder == 'python' else ""

with open(f"{dots}src/data/CompSci/GitHub.json", "r") as file:
    content = json.load(file)

    last_item_idx = len(content["Text"]) - 1

    print(f'\nThe new item is at index {c(last_item_idx, 'blue')}')

    print(f'\nThis is the item at index {c(last_item_idx, 'blue')} in the list\n')
    item = content["Text"][last_item_idx]

    print(json.dumps(item, indent=4))
    print()