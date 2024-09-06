#/Users/michaeltotaro/top-bar/src/assets/memes

import os

def list_files(directory):

    all_memes = []

    for entry in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, entry)):
            all_memes.append(entry)

    return all_memes


#directory_path = '../../top-bar/src/assets/memes'
directory_path = '../../top-bar/src/assets/UncwPics'
all_memes = list_files(directory_path)


for idx, pic in enumerate(all_memes):
    # print(f'import Meme{idx + 1} from "../assets/memes/{meme}";')
    print(f'import Pic{idx + 1} from "../assets/UncwPics/{pic}";')

    # print('    { text: "t", image: Pic',end="")
    # print(idx + 1, end="")
    # print(' },', end="")
    # print(f' //{pic}')