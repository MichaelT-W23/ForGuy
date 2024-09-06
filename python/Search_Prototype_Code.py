
# WHAT TO DO WITH .vue files

json_data = {
    "All views": [
        {
            "Name": "Where to Apply",
            "Objects": [
                {
                    "Section": 1,
                    "Fire": "water",
                    "State": "Illinois"
                },
                {
                    "Location": "Wilmington"
                }
            ]
        },
        {
            "Name": "Contacts",
            "Objects": [
                {
                    "Name": "Michael",
                    "Link": "twenty28",
                    "Friend": "Will"
                }
            ]
        }
    ]
}

def search_json(data, search_str, results=None, parent_name=None):
    if results is None:
        results = []

    if isinstance(data, dict):
        current_name = data.get("Name", parent_name)  # Get current name if it exists, else use parent
        for key, value in data.items():
            search_json(value, search_str, results, current_name)
    elif isinstance(data, list):
        for item in data:
            search_json(item, search_str, results, parent_name)
    else:
        if search_str.lower() in str(data).lower() and parent_name is not None:
            # Check if the parent_name is already added
            if not any(d['Name'] == parent_name for d in results):
                results.append({"Name": parent_name, "Matches": [data]})
            else:
                # Find the dictionary and add the match to the 'Matches' list
                for d in results:
                    if d['Name'] == parent_name:
                        d['Matches'].append(data)
                        break

    return results

# Input from user
search_str = "il"  # For demonstration purposes, replace with input("Enter search string: ") for interactive use

# Trigger the search
matches = search_json(json_data, search_str)

for match in matches:
    print(match)
