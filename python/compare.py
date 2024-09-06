from termcolor import colored as c

"""
Checks if the create_settings_file and the contents 
of the file in "Comp Sci" -> "VSCode settings" are the same.

Paste the VSCode Settings in results.txt
"""

def files_are_identical(file1, file2):

    identical = True

    with open(file1, 'r') as file:
        linesFile1 = file.readlines()

    with open(file2, 'r') as file:
        linesFile2 = file.readlines()

    if len(linesFile1) != len(linesFile2):
        print(c(f"Real settings has: {len(linesFile1)} lines", 'red'))
        print(c(f"Results has: {len(linesFile2)} lines\n", 'red'))
        return False 
    
    for i in range(len(linesFile1)):
        if linesFile1[i].rstrip() != linesFile2[i].rstrip():
            print(f"File 1: {linesFile1[i]}")
            print(f"File 2: {linesFile2[i]}")
            print()
            identical = False

    return identical

    
# # Example usage
file1 = 'real_settings.txt'
file2 = 'results.txt'

if files_are_identical(file1, file2):
    print(c("The files are identical.", 'green'))
else:
    print(c("The files are different.", 'red'))



