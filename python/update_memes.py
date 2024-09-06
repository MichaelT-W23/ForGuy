import json
import re


with open("../src/components/Memes.vue", "r") as file:
    lines = file.readlines()

    for line in lines:
        if 'import Vid' in line:
            print(line)

    file.seek(0)

    content = file.read()

    # Regular expression pattern to match meme objects
    pattern = re.compile(
        r'\{\s*text:\s*"(.*?)",\s*transcription:\s*"(.*?)",\s*(image|video):\s*(Meme\d+|Video\d+)\s*\}', re.DOTALL
    )

    # Find all matches
    matches = pattern.findall(content)

    # Convert matches into a list of dictionaries
    meme_objects = [
        {"text": match[0], "transcription": match[1], match[2]: match[3]} for match in matches
    ]

    for meme_obj in meme_objects:

        if 'video' in meme_obj:
            print(json.dumps(meme_obj, indent=4))


with open("../src/components/Memes.vue", "r") as file:

    pattern = r'.*Meme\d{1,2}.*'

    count = 1
    import_statements = True

    all_lines = []
    
    for line in file:

        if "image: " in line and import_statements:
            count = 1
            import_statements = False

        if re.search(pattern, line):
            new_line = re.sub(r'Meme\d{1,2}', f'Meme{count}', line)[:-1]
            count += 1
            all_lines.append(new_line)
        else:
            all_lines.append(line[:-1])

with open("../src/components/Memes.vue", "w", encoding='utf-8') as f:
    for line in all_lines:
        print(line)
        f.write(line + '\n') 
