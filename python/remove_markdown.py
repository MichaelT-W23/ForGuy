import re

class RemoveMarkdown:
    """
    Removes markdown syntax in SearchData.json
    """

    def __init__(self, content):
        self.content = content

        # [Cool Website](https://www.target.com/)
        self.hyperlink = r'\[([^\]]+)\]\((https?:\/\/[^\s]+)\)'

        # (Contact me)[/ContactMe]
        self.routerlink = r'\(([^)]+)\)\[([^\s]+)\]'

        # @NSA and DoD@[{ 'name': 'ImageView', 'params': { 'Name': 'NSA Pic', 'Description': 'UNCW is designated as a National Center of Academic Excellence in Cyber Defense Education (CAE-CDE) by the National Security Agency and Department of Homeland Security. Link -> www.uncw.edu/ccde. (I took this picture in Congdon Hall)', 'Pic': 'NSA.png'} }]
        self.routerlink_props = r'@([^@]+)@\[\s*({.*?})\s*\]'

        # # &here&(https://michaelt-w23.github.io/TestWebsite/Practice.docx)
        # self.download_link = r'\&([^\]]+)\&\((https?:\/\/[^\s]+)\)'

        # &here&() /\&([^\]]+)\&\((\/download[^\s]+)\)/g;
        self.download_link = r'/\&([^\]]+)\&\((\/download[^\s]+)\)/g;'

        # Scroll down(codeBlockRef), Different for multiple accounts(secondGitHubEight), etc.
        self.scroll_link = r'(Different for multiple accounts|Scroll back up to original step|Scroll back to links|Scroll down)\((.*?)\)'

        # Keys to remove from the search objects
        self.exclude_keys = ["FormatCode", "id"]

    def undo_all_links(self):
        for item in self.content:
            for idx, result in enumerate(item["Results"]):

                keys_to_remove = []

                for key, value in result.items():
                    if key in self.exclude_keys:
                        keys_to_remove.append(key)
                    else:
                        new_text = self.undo_link(value, self.hyperlink)
                        new_text = self.undo_link(new_text, self.routerlink)
                        new_text = self.undo_link(new_text, self.routerlink_props)
                        new_text = self.undo_link(new_text, self.download_link)
                        new_text = self.undo_link(new_text, self.scroll_link)

                        # Make's it obvious whats's happening. Could be result[key]
                        item["Results"][idx][key] = new_text

                for key in keys_to_remove:
                    del item["Results"][idx][key]

        return self.content


    def undo_link(self, text, markdown_pattern):
        if isinstance(text, int):
            return text

        cleaned_text = re.sub(markdown_pattern, r'\1', text)

        return cleaned_text
    





