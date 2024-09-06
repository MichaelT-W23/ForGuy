import re

def replace_strings(text):
    # Replace \n\t NOT followed by another \t with "\n      "
    text = re.sub(r'\n\t(?![\t])', '\n      ', text)
    
    # Replace \n\t\t with "\n\t  "
    text = re.sub(r'\n\t\t', '\n\t  ', text)
    
    # Replace one instance of \n with "\n  "
    text = re.sub(r'(?<!\n)\n(?!\n)', '\n  ', text)
    
    # Replace exactly two instances of \n\n with "\n\n  ", ensuring not to match three
    text = re.sub(r'(?<!\n)\n\n(?!\n)', '\n\n  ', text)

    # Replace exactly three instances of \n with '\n\n\n  '
    text = re.sub(r'(?<!\n)\n\n\n(?!\n)', '\n\n\n  ', text)

    return text


code = "<template>\n\t<p class=\"title\">Second Page</p>\n\t<LinkBtn\n\t\t:path="'/'"\n\t\t:buttonText="'Go to Home page'">\n\t</LinkBtn>\n</template>\n\n\n<script setup>\nimport LinkBtn from '../components/RouterBtn.vue';\n</script>\n\n\n<style scoped>\n\n.title {\n\tcolor: purple;\n\tfont-family: Arial, sans-serif;\n}\n\n</style>"
output_text = replace_strings(code)

print(repr(output_text))

