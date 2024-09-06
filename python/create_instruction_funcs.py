import json
import subprocess; 
import os


def get_all_instructions_files():
    directory_path = '../src/data/CompSci/Instructions/'

    files_and_directories = os.listdir(directory_path)

    file_names = [f for f in files_and_directories if os.path.isfile(os.path.join(directory_path, f))]
    file_names = [f for f in file_names if f.lower() not in ["displaylinks.json", "instructionsets.vue", "template.json"]]

    return file_names


def write_to_clipboard(output: str):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))


with open("../src/data/CompSci/Instructions/DisplayLinks.json", "r") as file:
    data = json.load(file)
    content = data["DisplayLinks"]

    ref_list = [link['ref'] for category in content.values() for link in category['links']]

    emojis_str = "emojis = {\n"

    for ref in ref_list:
        emojis_str += f'    "{ref}": "",\n'

    emojis_str = emojis_str[:-2]
    emojis_str += "\n}"

    #print(emojis_str)
    write_to_clipboard(emojis_str)


emojis = {
    "node": "🌐",
    "vue": "🌁",
    "react": "⚛️",
    "gh-pages": "📜",
    "vite-gh-pages": "⚡️",
    "aws": "☁️",
    "docker": "🐳",
    "flask-sqlite3": "🧪",
    "deploy-sqlite": "🚀",
    "flask-PostgreSQL": "🧰",
    "deploy-PostgreSQL": "🚀",
    "react-sqlite": "🍃",
    "deploy-spring": "🚀",

    "complex-mysql": "🗄️",
    "deploy-mysql": "🚀",


    "intellij": "✈️",
    "eclipse": "🌑",
    "cisco": "🌎",
    "php": "🐘",
    "tiktok": "🎥",
    "youtube": "📺",

    "google-api": "🔍",
    "reddit-api": "📖",
    "openai-api": "💬",
    "reddit-bot-aws": "🤖",



    "swift-firebase": "🐦",

    "swift-data": "🏎️",

    "developer-mode": "📱",

    "postman": "🧑🏻‍🚀",
    "python-server": "📡",

    "oauth": "🔐",


    "basic-sqlite": "📊",
    
    "excel": "📈",


    "prism": "🌈",

    "executable-python": "🐍"

}

files = get_all_instructions_files()

add_to_search_pages = ""

id_count = 34

for file in files:

    dir_path = '../src/data/CompSci/Instructions/'

    

    with open(f"{dir_path}{file}", 'r') as file:
        data = json.load(file)
        content = data["Info"][0]

        ref = content["ref"]
        emoji = emojis[ref]

        title = content["title"]
        

        add_to_search_pages += (
            "    {\n"
            f'        "id": {id_count},\n'
            f'        "Emoji": "{emoji}",\n'
            f'        "MenuName": "{title}",\n'
            f'        "Link": "/CompSci/SetupProjects/{ref}"\n'
            "    },\n"
        )

    id_count += 1

#print(add_to_search_pages[:-1])




add_to_search_data = ""


for file in files:

    dir_path = '../src/data/CompSci/Instructions/'

    file_path = f"{dir_path}{file}"

    with open(f"{file_path}", 'r') as file:
        data = json.load(file)

        content = data["Info"]
        instruction_list = data["Instructions"]

        ref_name = content[0]['ref'].replace("-", "_").lower()


        title = content[0]["title"]
        ref = content[0]["ref"]
        emoji = emojis[ref]

        add_to_search_data += (
            f"\ndef get_{ref_name}():\n"
            f"\twith open(\"{file_path}\", \"r\") as file:\n"
            "\t\tcontent = json.load(file)\n\n"
            f"\t\tinfo = content[\"Info\"]\n"
            f"\t\tinstructions = content[\"Instructions\"]\n"
            "\t\tinstructions = modify_list_with_code_separation(instructions, \"Code\")\n\n"
            f"\t\tTitle = \"{title} {emoji}\"\n"
            f"\t\tLink = \"/CompSci/SetupProjects/{ref}\"\n"
            f"\t\tResults = info + instructions\n\n"
            "\t\treturn { \"Title\": Title, \"Link\": Link, \"Results\": Results }\n"
        )

print(add_to_search_data)
# write_to_clipboard(add_to_search_data)