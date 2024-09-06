import json 
from termcolor import colored as c

# file_path = "../src/data/SearchPages.json"
# file_path = "../src/data/CompSci/Instructions/SwiftData.json"
# file_path = "../src/data/CompSci/Instructions/RedditBotAWS.json"
file_path = "../src/data/CompSci/Instructions/SpringApp.json"
# file_path = "../src/data/CompSci/Instructions/NodeServer.json"

# file_path = "../src/data/CompSci/Instructions/EmailJS.json"
# file_path = "../src/data/CompSci/Instructions/PyiCloud.json"


with open(file_path, 'r') as file:
    data = json.load(file)
    
    # For normal files
    # for i, item in enumerate(data):
    #     item["id"] = i + 1


    # # For One set Instructions 
    # data_set = data["Instructions"]
    
    # for i, item in enumerate(data_set):
    #     item["id"] = i + 1
    
    
    # For MultiSet Instructions
    for data_sets in data["MultiSet"]:
        current_set = data_sets["Instructions"]

        for i, item in enumerate(current_set):
            item["id"] = i + 1


with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    print(c("Updated Successfully!", "green"))
