import json
import re
import html
from collections import Counter
from termcolor import colored as c

class HtmlCharCollector:
    @staticmethod
    def lists_have_same_elements(list1, list2):
        return Counter(list1) == Counter(list2)

    @staticmethod
    def collect_escaped_html_chars(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        escaped_chars_set = set()

        def find_and_collect_escaped_html(obj):
            if isinstance(obj, dict):
                for value in obj.values():
                    find_and_collect_escaped_html(value)
            elif isinstance(obj, list):
                for element in obj:
                    find_and_collect_escaped_html(element)
            elif isinstance(obj, str):
                escaped_chars = re.findall(r'&[a-zA-Z]+;|&#\d+;|&#x[0-9A-Fa-f]+;', obj)
                for char in escaped_chars:
                    escaped_chars_set.add(char)

        find_and_collect_escaped_html(data)

        escaped_chars_list = sorted(list(escaped_chars_set))

        return escaped_chars_list

    @classmethod
    def show_results(cls, file_path):
        escaped_chars_list = cls.collect_escaped_html_chars(file_path)

        if not cls.lists_have_same_elements(escaped_chars_list, ['&lt;', '&gt;']):
            print(c("THERE'S A NEW HTML CHARACTER ADD IT TO ", 'red'))
            print("It used to be ['&lt;', '&gt;']")
            print(f"Now it's {escaped_chars_list}\n")

            print("This is the unescaped NEW list: ", end="")
            unescaped_chars_list = [html.unescape(char) for char in escaped_chars_list]
            print(unescaped_chars_list)
            print("\nGo to \"SearchResults.vue\" and add the new character in the \"escapedSearchQuery\" function.\n")
            print("Or go to replace_strs in create_search_data and add it to the list\n")
            
