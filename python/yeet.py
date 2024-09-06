import json

contacts_one = []
with open("../src/data/LinkedIn/Contacts.json", "r") as file:
    content = json.load(file)
    contacts = content["Contacts"]

    for contact in contacts:
        contacts_one.append(contact["Name"])


with open("../../contacts.json", "r") as file:

    content = json.load(file)
    contacts = content["Contacts"]

    for contact in contacts:
        if "Name" in contact:
            if contact["Name"] not in contacts_one:
                print(contact)




# import re

# pattern = r"(?:\s*\.)\b(lastname|firstname|value)\b"
# pattern = r'(?<=\.)(lastname|firstname|value)'
# string = " guy.value"

# match = re.search(pattern, string)

# if match:
#     print("YEET")
# else:
#     print("No match")
