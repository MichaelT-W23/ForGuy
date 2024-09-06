import json

with open("../src/data/LinkedIn/Contacts.json", 'r') as file:
    content = json.load(file)
    contacts = content["Contacts"]


def obj_to_write(attribute):
    return f"| {attribute if attribute else 'null'} "


with open("../public/download/contacts.md", 'w') as wfile:
    # wfile.write("Cool")

    count = 1

    wfile.write("# Contacts\n")
    wfile.write("| Name | Company | Role | Location | Email | LinkedIn | Details |\n")
    wfile.write("| ---- | ------- | ---- | -------- | ----- | -------- | ------- |\n")

    for contact in contacts:

        if "Contact" in contact and contact["Contact"]:
            contact["Email"] = contact["Contact"]
            contact["Contact"] = ""
        
        row = ""
        row += obj_to_write(contact["Name"])
        row += obj_to_write(contact["Company"])
        row += obj_to_write(contact["Role"])
        row += obj_to_write(contact["Location"])
        row += obj_to_write(contact["Email"])
        row += obj_to_write(contact["LinkedIn"])
        row += obj_to_write(contact["Details"])
        row += "|\n"
        
        wfile.write(row)
        row = ""


with open("../public/download/contacts.txt", 'w') as wfile_two:
    for index, contact in enumerate(contacts):
        wfile_two.write(f"Contact #{index + 1} - {contact['Company']}\n")

        if contact["Name"]:
            wfile_two.write(contact["Name"] + "\n")

        if contact["Company"]:
            wfile_two.write(contact["Company"] + "\n")

        if contact["Role"]:
            wfile_two.write(contact["Role"] + "\n")

        if contact["Location"]:
            wfile_two.write(contact["Location"] + "\n")

        if contact["Email"]:
            wfile_two.write(contact["Email"] + "\n")

        if contact["LinkedIn"]:
            wfile_two.write(contact["LinkedIn"] + "\n")

        if contact["Details"]:
            wfile_two.write(contact["Details"] + "\n")

        wfile_two.write("\n\n")
        