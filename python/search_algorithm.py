import json

def load_data():
    with open("delete.json", "r") as file:
        content = json.load(file)
        return content

def highlight_string(text, search_string):
    idx = 0
    highlighted_text = ''
    search_length = len(search_string)
    lower_text = text.lower()
    lower_search_string = search_string.lower()
    count = 0 
    
    while idx < len(text):
        next_find = lower_text.find(lower_search_string, idx)
        if next_find == -1:
            highlighted_text += text[idx:]
            break
        highlighted_text += text[idx:next_find] + '<span style="background-color: yellow">' + text[next_find:next_find + search_length] + '</span>'
        idx = next_find + search_length
        count += 1 
    
    return highlighted_text, count

def search_in_results(results, search_string):
    matched_results = []
    total_highlight_count = 0 
    if results is None:
        return matched_results, total_highlight_count 
    for result in results:
        for key, value in result.items():
            if isinstance(value, str) and search_string.lower() in value.lower():
                highlighted_text, count = highlight_string(value, search_string)
                matched_results.append(f'<p>{highlighted_text}</p>')
                total_highlight_count += count
            elif isinstance(value, (int, float)) and search_string.isdigit():
                if search_string == str(value):
                    matched_results.append(f'<p><span style="background-color: yellow">{str(value)}</span></p>')
                    total_highlight_count += 1
    return matched_results, total_highlight_count

def search_json(data, search_string):
    all_matches = []
    total_count = 0
    for item in data:
        results = item.get('Results', []) 
        matched_results, highlight_count = search_in_results(results, search_string)
        if matched_results:
            match_info = {
                "Title": item['Title'],
                "Link": item['Link'],
                "MatchedResults": matched_results
            }
            all_matches.append(match_info)
            total_count += highlight_count

    return all_matches, total_count

data = load_data()

search_string = input("Enter search term: ")
all_matches, total_count = search_json(data, search_string)

for item in all_matches:
    print(item["Title"])
    print(item["Link"])
    for result in item["MatchedResults"]:
        print(result)
    print()
    print()
    print()

print(f"Total count {total_count}")
