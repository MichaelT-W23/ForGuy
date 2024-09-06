import re
from termcolor import colored as c


with open('../src/components/UncwPics.vue', 'r') as file:
    all_lines = file.readlines()

    import_stmts = []
    main_lines = []

    main_part = False

    for line in all_lines:
        if not main_part:
            import_stmts.append(line)
        else:
            main_lines.append(line)

        if "export" in line:
            main_part = True

    correct_numbering = []

    count = 1
    
    for stmt in import_stmts:

        output_string = stmt

        if re.search(r'import Pic\d+', stmt):
            output_string = re.sub(r'import Pic\d+', f'import Pic{count}', stmt)
            count += 1
        
        correct_numbering.append(output_string)

    count = 1

    for line in main_lines:

        output_str = line

        if re.search(r'image: Pic\d+', line):
            output_str = re.sub(r'image: Pic\d+', f'image: Pic{count}', line)
            count += 1
        
        correct_numbering.append(output_str)

    with open('../src/components/UncwPics.vue', 'w') as file:
        for string in correct_numbering:
            file.write(string)

print(c("Files numbers corrected successfully.", 'green'))
