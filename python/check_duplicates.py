import json

with open("../src/data/jobs/WhereToApply.json", "r") as file:
    content = json.load(file)
    companies = content["Companies"]

    names = []

    for company in companies:
        if company["Name"].strip() not in names:
            names.append(company["Name"].strip())
        else:
            print(company["Name"].strip())