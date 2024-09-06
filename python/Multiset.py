import json

def modify_list_with_code_separation(obj, _):
    return obj


def get_multi_set_example():
    with open("../src/data/CompSci/Instructions/MultiSetTemplate.json", "r") as file:
        content = json.load(file)
		
        multi_set = content["MultiSet"]

        Results = []

        for obj in multi_set:
            info = obj["Info"]
            instructions = obj["Instructions"]
            instructions = modify_list_with_code_separation(instructions, "Code")

            Results += info + instructions

        Title = "Deploy the Vue, Flask and SQLite3 app to PythonAnywhere 🐍"
        Link = "/CompSci/SetupProjects/deploy-sqlite"
        
        return { "Title": Title, "Link": Link, "Results": Results }
		

print(json.dumps(get_multi_set_example(), indent=4))