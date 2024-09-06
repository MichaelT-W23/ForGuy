import re


cool = [
     "How to Create a GitHub Account(createGHAccount)",
     "How to Create a GitHub Repository(createGHRepo)",
     "How to Create Multiple GitHub Accounts(multipleGHAccounts)",
     "How to Create a GitHub Repository Using a Different Account(multipleDifferentAccount)",
     "Git Commands(GitCommands)",
     "General Tips(GeneralTips)",
     "Three Main Git Commands(ThreeCommands)",
     "How to Fork a Repository(ForkRepo)",
     "Existing Folder Commands(ExistingCmds)",
     "Amotions Workflow(AmotionsWorkflow)"
]

for idx, cool in enumerate(cool):
    print('        {')
    print(f'            "id": {idx + 1},')
    print(f'            "name": "{cool}"')
    print('        },')

# # Pattern to find strings within parentheses
# pattern = r"\((.*?)\)"

# # List to store the extracted strings
# extracted_strings = []

# # Iterate over each item in the list
# for item in cool:
#     # Find all substrings that match the pattern
#     matches = re.findall(pattern, item)
    
#     # matches will be a list of all substrings found. We expect only one per item here.
#     for match in matches:
#         extracted_strings.append(match)

# for string in extracted_strings:
#     print(f"const {string} = ref(null);")


# print()


# for string in extracted_strings:
#     print(f"        {string},")