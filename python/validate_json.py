import json

file_path = '../src/data/CompSci/instructions/Youtube.json'

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("JSON is valid.")
except json.JSONDecodeError as e:
    print(f"JSON is invalid: {e}")
