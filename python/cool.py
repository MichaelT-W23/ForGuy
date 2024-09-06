import json
import re
import subprocess

#"/**\n   * This class implements an array-based list for a maximum of 20 boats\n   *   \n   * @author Michael Totaro\n   */\n  public class BoatList {\n\n{tab}/** Capacity of the list containing names of Boats */\n{tab}public static final int MAX_BOATS = 20;\n\n{tab}/**\n{tab} * Creates an array-based list of boats, adds some boats, removes a boat,\n{tab} * queries if a boat exists in the list, and prints the list.\n{tab} *\n{tab} * @param args command line arguments (not used)\n{tab} */\n{tab}public static void main(String[] args) {\n{tab}{tab}String[] boats = new String[MAX_BOATS];\n\n{tab}{tab}int numberOfBoats = 0;\n\n{tab}{tab}numberOfBoats = addBoat(boats, numberOfBoats, \"Natalie\");\n{tab}{tab}numberOfBoats = addBoat(boats, numberOfBoats, \"Wendell\");\n{tab}{tab}numberOfBoats = addBoat(boats, numberOfBoats, \"Lori\");\n{tab}{tab}numberOfBoats = addBoat(boats, numberOfBoats, \"Steve\");\n{tab}{tab}numberOfBoats = addBoat(boats, numberOfBoats, \"Kevin\");\n\n{tab}{tab}System.out.println(\"\\nBoat List:\");\n{tab}{tab}printList(boats, numberOfBoats);\n\n{tab}{tab}int index = findBoat(boats, numberOfBoats, \"Rosa\");\n\n{tab}{tab}if (index == -1) {\n{tab}{tab}{tab}numberOfBoats = addBoat(boats, numberOfBoats, \"Rosa\");\n{tab}{tab}} else {\n{tab}{tab}{tab}System.out.println(boats[index] + \" is located at index \" +\n{tab}{tab}{tab}{tab}{tab}{tab}{tab}{tab}index + \" in the boats list.\");\n{tab}{tab}}\n\n{tab}{tab}numberOfBoats = removeBoat(boats, numberOfBoats, \"Wendell\");\n\n{tab}{tab}System.out.println(\"\\nBoat List:\");\n{tab}{tab}printList(boats, numberOfBoats);\n{tab}}\n\n{tab}/**\n{tab} * Adds a boat to the list.\n{tab} *\n{tab} * @param list the array of boat names\n{tab} * @param numberOfBoats the current number of boats in the list\n{tab} * @param boat the boat to add to the list\n{tab} * @return the new number of boats on the list\n{tab} * @throws IllegalArgumentException (with message \"No room in list\") if list is full\n{tab} */\n{tab}public static int addBoat(String[] list, int numberOfBoats, String boat) {\n\n{tab}{tab}if (numberOfBoats >= list.length) {\n{tab}{tab}{tab}throw new IllegalArgumentException(\"No room in list\");\n{tab}{tab}}\n\n{tab}{tab}list[numberOfBoats++] = boat;\n\n{tab}{tab}return numberOfBoats;\n\n{tab}}\n\n{tab}/**\n{tab} * Prints the list with each element on a separate line.\n{tab} *\n{tab} * @param list the array of boat names\n{tab} * @param numberOfBoats the current number of boats in the list\n{tab} */\n{tab}public static void printList(String[] list, int numberOfBoats) {\n{tab}{tab}for (int i = 0; i < numberOfBoats; i++) {\n{tab}{tab}{tab}System.out.println(list[i]);\n{tab}{tab}}\n{tab}}\n\n{tab}/**\n{tab} * Removes a boat from the list.\n{tab} *\n{tab} * @param list the array of boat names\n{tab} * @param numberOfBoats the current number of boats in the list\n{tab} * @param boat the boat to remove from the list\n{tab} * @return the new number of boat on the list\n{tab} */\n{tab}public static int removeBoat(String[] list, int numberOfBoats, String boat) {\n{tab}{tab}boolean found = false;\n\n{tab}{tab}for (int i = 0; i < numberOfBoats; i++) {\n{tab}{tab}{tab}if (found) {\n{tab}{tab}{tab}{tab}list[i - 1] = list[i];\n{tab}{tab}{tab}}\n\n{tab}{tab}{tab}if (list[i].equals(boat)) {\n{tab}{tab}{tab}{tab}found = true;\n{tab}{tab}{tab}{tab}numberOfBoats--;\n{tab}{tab}{tab}}\n{tab}{tab}}\n\n{tab}{tab}return numberOfBoats;\n{tab}}\n\n{tab}/**\n{tab} * Determines if the given boat is in the list.\n{tab} *\n{tab} * @param list the array of boat names\n{tab} * @param numberOfBoats the current number of boats in the list\n{tab} * @param boat the boat to find in the list\n{tab} * @return the index of the list element containing boat\n{tab} *         or -1 if boat does not exist in the list\n{tab} */\n{tab}public static int findBoat(String[] list, int numberOfBoats, String boat) {\n{tab}{tab}for (int i = 0; i < list.length; i++) {\n{tab}{tab}{tab}if (list[i] == boat) {\n{tab}{tab}{tab}{tab}return i;\n{tab}{tab}{tab}}\n{tab}{tab}}\n\n{tab}{tab}return -1;\n{tab}}\n  }",

# if (list[i] == boat)

def write_to_clipboard(output: str):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))
    
# Function to update the "FormatCode" field in the component data
def update_format_code(data):
    # Definitions for the replacements
    tab = " " * 6
    two_tab = " " * 10  # or whatever your definition of two_tab is
    three_tab = " " * 14  # or your definition of three_tab
    four_tab = " " * 18 # or your definition of four_tab

    java = data['ComponentData'][1]
    formatCode = java['FormatCode']
    
    # Replacing four {tab} occurrences first to avoid conflicts with fewer {tab} patterns
    formatCode = re.sub(r'\{tab\}\{tab\}\{tab\}\{tab\}', four_tab, formatCode)
    # Then replace three {tab} occurrences
    formatCode = re.sub(r'\{tab\}\{tab\}\{tab\}', three_tab, formatCode)
    # Then two {tab} occurrences
    formatCode = re.sub(r'\{tab\}\{tab\}', two_tab, formatCode)
    # Finally, replace single {tab} occurrences
    formatCode = formatCode.replace('{tab}', tab)

    print(formatCode)
    return repr(formatCode).replace('\"', '\\"')


file_path = '../src/data/CompSci/CompSciTips.json'

with open(file_path, 'r') as file:
    data = json.load(file)




write_to_clipboard(update_format_code(data))
