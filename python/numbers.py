with open("../src/components/Memes.vue", "r") as file:
    count = 1 
    count_two = 1

    for line in file:
        line = line.rstrip()

        if "import" not in line and "image:" not in line:
            print(line)

        if "import" in line:
            line_lst = line.split(" ")
            line_lst[1] = f"Meme{count}"
            count += 1
            print(' '.join(line_lst))
            
        if "image:" in line:
            line_lst = line.split(" ")
            line_lst[-1] = f"Meme{count_two}"

            print(' '.join(line_lst))
            count_two += 1

        




