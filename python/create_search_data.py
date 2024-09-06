import html
import json
from remove_markdown import RemoveMarkdown 
from escape_chars import HtmlCharCollector
from termcolor import colored as c

"""
This file creates the src/data/SearchData.json page.
"""


def format_json(data):
	return json.dumps(data, indent=4)

def escape_html_in_json(file_path):
	"""
	Escapes all html is a json file 
	"""

	with open(file_path, 'r', encoding='utf-8') as file:
		data = json.load(file)

	def escape_html_in_strings(obj):
		if isinstance(obj, dict):
			return {key: escape_html_in_strings(value) for key, value in obj.items()}
		elif isinstance(obj, list):
			return [escape_html_in_strings(element) for element in obj]
		elif isinstance(obj, str):
			return html.escape(obj)
		else:
			return obj

	escaped_data = escape_html_in_strings(data)

	with open(file_path, 'w', encoding='utf-8') as file:
		json.dump(escaped_data, file, ensure_ascii=False, indent=4)

def transform_json(json_obj):
	"""
	Converts any attributes in a json object that are lists into a comma-separated string.
	Keeps the original key for each attribute. If none of the attributes are lists, returns 
	the unmodified json object.

	Example:
	Input:
		"Classes": [
			"CSC 360",
			"CSC 380"
		],
	
	Output:
		"Classes": "CSC 360, CSC 380"
	"""

	result = {}
	
	for key, value in json_obj.items():
		if isinstance(value, list):
			result[key] = ', '.join(value)
		else:
			result[key] = value
	
	return result

def make_json_object(key, value):
	"""
	Converts JSON attribute to it's own object 

	Example:
	Input:
		"Title": "Visual Studio Code Shortcuts"

	Output:
		{
			"Title": "Visual Studio Code Shortcuts",
		}
	
	"""
	return {key: value}

def modify_list_with_code_separation(og_list, key_to_separate):
	"""
	Takes a list with JSON objects that have an attribute which is 
	an object. The JSON objects that have an attribute will be split 
	into the two different list elements. The original list element 
	without the attribute thats and object, and an object. Can handle 
	regular objects and a list of JSON objects.

	Example:
	Input
		{
			"id": 2,
			"instruction": "To get started, download git. I'd recommend installing git using Homebrew. Install the Homebrew package manager using the following two commands.",
			"Code": {
				"Name": "",
				"Description": "",
				"Language": "Command",
				"FormatCode": "xcode-select --install\n\n  /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/\n  install/HEAD/install.sh)\"",
				"CopyCode": "xcode-select --install\n\n/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
			}
		},

	Output:
	   {
		  "id": 2,
		  "instruction": "To get started, download git. I'd recommend installing git using Homebrew. Install the Homebrew package manager using the following two commands."
	   },
	   {
		  "Name": "",
		  "Description": "",
		  "Language": "Command",
		  "CopyCode": "xcode-select --install\n\n/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
	   }

	Example: 
	Input
		{
			"id": 35,
			"instruction": "These are commonly used PostgreSQL commands.",
			"Table": [
				{
					"Command": "\\dt",
					"Description": "List all tables",
					"Example": "\\dt"
				},
				{
					"Command": "\\q",
					"Description": "Quit/exit your database",
					"Example": "\\q"
				}
			]
		}

	Output
		{
			"id": 35,
			"instruction": "These are commonly used PostgreSQL commands."
		},
		{
			"Command": "\\dt",
			"Description": "List all tables",
			"Example": "\\dt"
		},
		{
			"Command": "\\q",
			"Description": "Quit/exit your database",
			"Example": "\\q"
		}

	"""

	was_found = False 

	for item in og_list:
		if key_to_separate in item:
			was_found = True
	
	if not was_found:
		return og_list
	
	modified_list = []

	for item in og_list:
		item_copy = {key: value for key, value in item.items() if key != key_to_separate}
		modified_list.append(item_copy)
		
		if key_to_separate in item:
			separated_value = item[key_to_separate]

			if isinstance(separated_value, list):
				modified_list.extend(separated_value)
			else:
				modified_list.append(separated_value)

	return modified_list

def replace_strs(file_path):
	"""
	Replaces substrings in a JSON file with the new strings.
	:param file_path: File path of file to be modified.
	"""
	# <br> -> " "
	#
	old_strings = ["<br>", "&#x27;", "&amp;", '&quot;']
	new_strings = [" ", "'", "&", '\\"']

	with open(file_path, 'r') as file:
		data = file.read()

	for old, new in zip(old_strings, new_strings):
		data = data.replace(old, new)

	with open(file_path, 'w') as file:
		file.write(data)


def ensure_string(value):
	if not isinstance(value, str):
		print(c("THIS SHOULD BE A STRING ", "red"), end="")
		print(value)
	
	if isinstance(value, tuple):
		print(c("Make sure there's no comma after the quotes", "red"))
		print('Ex: Title = \"Comp Sci Minor 💻\", There shouldn\'t be a comma after the quote.\n')

def ensure_list(value, title):
	if not isinstance(value, list):
		print()

		print(c("THIS SHOULD BE A LIST", "red"), end="")
		print(" - ", end="")
		print(c(title, "blue"))
		print(value)	

# Classes
def get_classestoavoid():
	with open("../src/data/Classes/ClassesToAvoid.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		classes = content["Classes"]
		professors = content["Professors"]


		Title = "Classes To Avoid ❌"
		Link = "/Classes/ClassesToAvoid"
		Results = text + classes + professors

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


def get_classrecommendations():
	with open("../src/data/Classes/ClassRecommendations.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		classes = content["Classes"]
		professors = content["Professors"]

		professors = [transform_json(obj) for obj in professors]

		Title = "Class Recommendations 👍"
		Link = "/Classes/ClassRecommendations"
		Results = text + classes + professors

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }



def get_usefulcertifications():
	with open("../src/data/Classes/UsefulCertifications.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		cloud_certs = content["Cloud Certifications"]
		essential_skills = content["Certifications for Essential Skills"]
		machine_learning = content["Machine Learning Certifications"]
		degrees = content["Academic Certifications and Degrees"]
		tips = content["GeneralTips"]


		Title = "Useful Certifications 🏆"
		Link = "/Classes/Certifications"
		Results = text + cloud_certs + essential_skills + machine_learning + degrees + tips

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_cscdescriptions():
	with open("../src/data/Classes/CSCDescriptions.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		courses = content["Courses"]

		courses = [transform_json(course) for course in courses]

		Title = "CSC Descriptions 📝"
		Link = "/Classes/CSCDescriptions"
		Results = text + courses

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_classesivetaken():
	with open("../src/data/Classes/ClassesIveTaken.json", "r") as file:
		content = json.load(file)

		text = content["Text"]

		freshman_first = content["Freshman"]["First"]
		freshman_second = content["Freshman"]["Second"]

		sophomore_first = content["Sophomore"]["First"]
		sophomore_second = content["Sophomore"]["Second"]

		junior_first = content["Junior"]["First"]
		junior_second = content["Junior"]["Second"]

		senior = content["Senior"]["First"]

		ap_classes = content["Ap Classes"]

		sophomore_first = [transform_json(course) for course in sophomore_first]
		sophomore_second = [transform_json(course) for course in sophomore_second]
		junior_first = [transform_json(course) for course in junior_first]
		junior_second = [transform_json(course) for course in junior_second]
		senior = [transform_json(course) for course in senior]


		Title = "Classes I've Taken 👨🏻‍🏫"
		Link = "/Classes/ClassesIveTaken"
		Results = (text + freshman_first + freshman_second + sophomore_first + 
				   sophomore_second + junior_first + junior_second + senior + ap_classes)

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_compsciminor():
	with open("../src/data/Classes/CompSciMinor.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		classes = content["Classes"]
		semester_classes = content["SemesterClasses"]
		
		classes = [transform_json(course) for course in classes]
		semester_classes = [transform_json(course) for course in semester_classes]
		

		Title = "Comp Sci Minor 💻"    
		Link = "/Classes/CompSciMinor"
		Results = text + classes + semester_classes

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }



# CompSci
def get_vscodeshortcuts():
	with open("../src/data/CompSci/VSCodeShortcuts.json", "r") as file:
		content = json.load(file)

		# VSCode Shortcuts 
		title = content["VSCodeShortcuts"]["Title"]
		desc = content["VSCodeShortcuts"]["Description"]
		shortcuts = content["VSCodeShortcuts"]["Shortcuts"]

		shortcuts.append(make_json_object("Title", title))
		shortcuts.append(make_json_object("Description", desc))


		# Pycharm
		titlePy = content["PyCharm"]["Title"]
		descPy = content["PyCharm"]["Description"]
		shortcutsPy = content["PyCharm"]["Shortcuts"]

		shortcutsPy.append(make_json_object("Title", titlePy))
		shortcutsPy.append(make_json_object("Description", descPy))

		
		#Eclipse 
		titleEc = content["Eclipse"]["Title"]
		descEc = content["Eclipse"]["Description"]
		shortcutsEc = content["Eclipse"]["Shortcuts"]

		shortcutsEc.append(make_json_object("Title", titleEc))
		shortcutsEc.append(make_json_object("Description", descEc))

		#Xcode
		titleX = content["XCode"]["Title"]
		descX = content["XCode"]["Description"]
		shortcutsX = content["XCode"]["Shortcuts"]

		shortcutsX.append(make_json_object("Title", titleX))
		shortcutsX.append(make_json_object("Description", descX))

		#Slack
		titleSl = content["Slack"]["Title"]
		descSl = content["Slack"]["Description"]
		shortcutsSl = content["Slack"]["Shortcuts"]

		shortcutsSl.append(make_json_object("Title", titleSl))
		shortcutsSl.append(make_json_object("Description", descSl))


		Title = "VSCode Shortcuts 🚀"
		Link = "/compsci/VSCodeShortcuts"
		Results = shortcuts + shortcutsPy + shortcutsEc + shortcutsX + shortcutsSl

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	
def get_visualstudiocode():
	with open("../src/data/CompSci/VisualStudioCode.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		links = content["Links"]

		Title = "Visual Studio Code 🎨"
		Link = "/compsci/VisualStudioCode"
		Results = text + links

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_settings():
	with open("../src/data/CompSci/settings.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		settings = content["settings"]

		Title = "VSCode Settings ⚙️"
		Link = "/compsci/VSCodeSettings"
		Results = text + settings

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_uiux_tips():
	with open("../src/data/CompSci/UIUX_Tips.json", "r") as file:
		content = json.load(file)
		
		text = content["Text"]
		tips = content["UIDesignTips"]
		ibmTips = content["IBMDesignTips"]

		ibmTips = [transform_json(tip) for tip in ibmTips]

		other = [transform_json({"Other": content["Other"]})]

		Title = "UI/UX Design Tips 🖼️"
		Link = "/compsci/UIDesignTips"
		Results = text + tips + ibmTips + other

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_display_links():
	with open("../src/data/CompSci/Instructions/DisplayLinks.json", "r") as file:
		content = json.load(file)

		text = content["Text"]

		display_links = content["DisplayLinks"]

		display_link_list = []

		for _, details in display_links.items():
			
			title_obj = make_json_object("title", details['title'])
			desc_obj = make_json_object("desc", details['desc'])
			links_obj = details['links']

			links_obj.insert(0, title_obj)
			links_obj.insert(0, desc_obj)

			display_link_list.append(links_obj)

		flattened_list = [item for sublist in display_link_list for item in sublist]
		
		Title = "Setup Project 🛠️"
		Link = "/CompSci/SetupProjects"
		Results = text + flattened_list
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


# 365 - 687
def get_node():
	with open("../src/data/CompSci/Instructions/SetupNode.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Install Node.js 🌐"
		Link = "/CompSci/SetupProjects/node"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_vue():
	with open("../src/data/CompSci/Instructions/SetupVue.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a Vue.js Project 🌁"
		Link = "/CompSci/SetupProjects/vue"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_react():
	with open("../src/data/CompSci/Instructions/SetupReact.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a React.js Project ⚛️"
		Link = "/CompSci/SetupProjects/react"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_angular():
	with open("../src/data/CompSci/Instructions/SetupAngular.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup an Angular Project 🔺"
		Link = "/CompSci/SetupProjects/angular"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	
def get_templates():
	with open("../src/data/CompSci/Instructions/TemplatesFolder.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "Create a Project Templates Folder 📁"
		Link = "/CompSci/SetupProjects/templates"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_gh_pages():
	with open("../src/data/CompSci/Instructions/GithubPages.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "Deploy a Vanilla JS Project to GitHub Pages 📜"
		Link = "/CompSci/SetupProjects/gh-pages"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_vite_gh_pages():
	with open("../src/data/CompSci/Instructions/ViteGHPages.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "Deploy a Vite Project to GitHub Pages ⚡️"
		Link = "/CompSci/SetupProjects/vite-gh-pages"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_aws():
	with open("../src/data/CompSci/Instructions/SetupAWS.json", "r") as file:
		content = json.load(file)
		
		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup an Amazon Web Services Account ☁️"
		Link = "/CompSci/SetupProjects/aws"
		Results = info + instructions
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_docker():
	with open("../src/data/CompSci/Instructions/docker.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Install and Setup Docker 🐳"
		Link = "/CompSci/SetupProjects/docker"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_flask_sqlite3():
	with open("../src/data/CompSci/Instructions/FlaskSQLite.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Make a Simple REST Api using Vue, Flask and SQLite3 🧪"
		Link = "/CompSci/SetupProjects/flask-sqlite3"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	  

def get_deploy_sqlite():
	with open("../src/data/CompSci/Instructions/DeploySqlite.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "Deploy the Vue, Flask and SQLite3 app to PythonAnywhere 🐍"
		Link = "/CompSci/SetupProjects/deploy-sqlite"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


def get_flask_postgresql():
	with open("../src/data/CompSci/Instructions/FlaskPost.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")
			instructions = modify_list_with_code_separation(instructions, "Table")
			Results += info + instructions

		Title = "How to Make a Complex Rest API using Vue, Flask and PostgreSQL 🧰"
		Link = "/CompSci/SetupProjects/flask-PostgreSQL"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


def get_deploy_postgresql():
	with open("../src/data/CompSci/Instructions/DeployPost.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions
		
		Title = "Deploy the Vue, Flask and PostgreSQL app to Amazon Web Services 🚀"
		Link = "/CompSci/SetupProjects/deploy-PostgreSQL"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_react_spring():
	with open("../src/data/CompSci/Instructions/SpringApp.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "How to Make a Simple REST Api using React, Spring Boot and H2 🍃"
		Link = "/CompSci/SetupProjects/react-spring"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }      




def get_deploy_spring():
	with open("../src/data/CompSci/Instructions/DeploySpring.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions
		
		Title = "Deploy the React, Spring Boot and H2 app to Heroku 🦸🏻‍♂️"
		Link = "/CompSci/SetupProjects/deploy-spring"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	 
def get_complex_mysql():
	with open("../src/data/CompSci/Instructions/ComplexMySQL.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Make a Complex REST Api using React, Spring Boot and MySQL 🗄️"
		Link = "/CompSci/SetupProjects/complex-mysql"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	 
	 
def get_deploy_mysql():
	with open("../src/data/CompSci/Instructions/DeployMySQL.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "Deploy the React, Spring Boot and MySQL app to Amazon Web Services 🚀"
		Link = "/CompSci/SetupProjects/deploy-mysql"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


def get_intellij():
	with open("../src/data/CompSci/Instructions/IntellijJavaFX.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a JavaFX Project (Intellij IDEA) ✈️"
		Link = "/CompSci/SetupProjects/intellij"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_eclipse():
	with open("../src/data/CompSci/Instructions/EclipseJavaFX.json", "r") as file:
		content = json.load(file)
		
		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")
		
		Title = "How to Setup a JavaFX Project (Eclipse) 🌑"
		Link = "/CompSci/SetupProjects/eclipse"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_cisco():
	with open("../src/data/CompSci/Instructions/CiscoSecure.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup Cisco Secure Client and a VPN 🌎"
		Link = "/CompSci/SetupProjects/cisco"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_php():
	with open("../src/data/CompSci/Instructions/PhpAndMySQL.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a PHP and MySQL Project for UNCW 🐘"
		Link = "/CompSci/SetupProjects/php"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_tiktok():
	with open("../src/data/CompSci/Instructions/TikTok.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup TikTok Downloader 🎥"
		Link = "/CompSci/SetupProjects/tiktok"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_youtube():
	with open("../src/data/CompSci/Instructions/Youtube.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup YouTube Downloader 📺"
		Link = "/CompSci/SetupProjects/youtube"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	 
def get_google_api():
	with open("../src/data/CompSci/Instructions/GoogleApi.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "How to Setup a Google API Project 🔍"
		Link = "/CompSci/SetupProjects/google-api"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	 

def get_reddit_api():
	with open("../src/data/CompSci/Instructions/RedditApi.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a Reddit API Project 📖"
		Link = "/CompSci/SetupProjects/reddit-api"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	
def get_spotify_api():
	with open("../src/data/CompSci/Instructions/SpotifyApi.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a Spotify API Project 🎧"
		Link = "/CompSci/SetupProjects/spotify-api"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	  

def get_openai_api():
	with open("../src/data/CompSci/Instructions/OpenAI.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup an OpenAI API Project 💬"
		Link = "/CompSci/SetupProjects/openai-api"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_linkedin_api():
	with open("../src/data/CompSci/Instructions/Linkedin.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a LinkedIn API Project 📊"
		Link = "/CompSci/SetupProjects/linkedin-api"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_reddit_bot():
	with open("../src/data/CompSci/Instructions/RedditBot.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "How to Create a Reddit Bot 🤖"
		Link = "/CompSci/SetupProjects/reddit-bot"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_reddit_bot_aws():
	with open("../src/data/CompSci/Instructions/RedditBotAWS.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "How to Deploy a Reddit Bot on AWS 🚀"
		Link = "/CompSci/SetupProjects/reddit-bot-aws"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }  


def get_swift_firebase():
	with open("../src/data/CompSci/Instructions/SwiftFirebase.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "How to Setup an iOS app with SwiftUI and Firebase 🐦"
		Link = "/CompSci/SetupProjects/swift-firebase"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


def get_swift_data():
	with open("../src/data/CompSci/Instructions/SwiftData.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup SwiftData in a SwiftUI project 🏎️"
		Link = "/CompSci/SetupProjects/swift-data"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_developermode():
	with open("../src/data/CompSci/Instructions/DeveloperMode.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Run an iOS app in Developer Mode 📱"
		Link = "/CompSci/SetupProjects/developer-mode"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	 
def get_postman():
	with open("../src/data/CompSci/Instructions/Postman.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "How to Setup and Use Postman 🧑🏻‍🚀"
		Link = "/CompSci/SetupProjects/postman"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_flash_drive():
	with open("../src/data/CompSci/Instructions/FlashDrive.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "Interact with a Flash Drive Using Python 💾"
		Link = "/CompSci/SetupProjects/flash-drive"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


def get_python_server():
	with open("../src/data/CompSci/Instructions/PythonServer.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a Python Server 📡"
		Link = "/CompSci/SetupProjects/python-server"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


def get_node_server():
	with open("../src/data/CompSci/Instructions/NodeServer.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup a Node Server ⚙️"
		Link = "/CompSci/SetupProjects/node-server"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_emailjs():
	with open("../src/data/CompSci/Instructions/EmailJS.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "How to Setup Email.js in a Project 📬"
		Link = "/CompSci/SetupProjects/emailjs"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_pyicloud():
	with open("../src/data/CompSci/Instructions/PyiCloud.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Interact with iCloud using Python 🍎"
		Link = "/CompSci/SetupProjects/pyicloud"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_oauth():
	with open("../src/data/CompSci/Instructions/OAuth.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup OAuth Authentication 🔐"
		Link = "/CompSci/SetupProjects/oauth"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_basic_sqlite():
	with open("../src/data/CompSci/Instructions/SQLite3.json", "r") as file:
		content = json.load(file)
		
		multi_set = content["MultiSet"]

		Results = []

		for obj in multi_set:
			info = obj["Info"]
			instructions = obj["Instructions"]
			instructions = modify_list_with_code_separation(instructions, "Code")

			Results += info + instructions

		Title = "How to Populate a SQLite3 Database 📊"
		Link = "/CompSci/SetupProjects/basic-sqlite"
		
		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	
def get_excel():
	with open("../src/data/CompSci/Instructions/ReadExcel.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Use Excel with Python 📈"
		Link = "/CompSci/SetupProjects/excel"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_prism():
	with open("../src/data/CompSci/Instructions/PrismLang.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Add a Language to the Prism Library 🌈"
		Link = "/CompSci/SetupProjects/prism"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	  
def get_executable_python():
	with open("../src/data/CompSci/Instructions/ExecutablePython.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "How to Setup an Executable Python Script 🐍"
		Link = "/CompSci/SetupProjects/executable-python"
		Results = info + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	  
def get_compscitips():
	with open("../src/data/CompSci/CompSciTips.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		tips = content["Tips"]
		componentData = content["ComponentData"]
		codeLinks = content["CodeLinks"]

		Title = "Comp Sci Tips 🖥️"
		Link = "/compsci/CompSciTips"
		Results = text + tips + componentData + codeLinks

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_vscodeextensions():
	with open("../src/data/CompSci/VSCodeExtensions.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		extensions = content["Extensions"]

		Title = "VSCode Extensions 🧩"
		Link = "/compsci/VSCodeExtensions"
		Results = text + extensions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_github():
	with open("../src/data/CompSci/GitHub.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		scrollLinks = content["ScrollLinks"]

		setupGithub = content["SetupGitHub"]
		setupGithub = modify_list_with_code_separation(setupGithub, "Code")

		createGitHubRepo = content["CreateGitHubRepo"]
		createGitHubRepo = modify_list_with_code_separation(createGitHubRepo, "Code")

		setupSecondGitHub = content["SetupSecondGitHub"]
		setupSecondGitHub = modify_list_with_code_separation(setupSecondGitHub, "Code")

		createSecondGitHubRepo = content["CreateSecondGitHubRepo"]
		createSecondGitHubRepo = modify_list_with_code_separation(createSecondGitHubRepo, "Code")

		csc450WorkflowPtsOne = content["CSC450WorkflowPtsOne"]
		csc450WorkflowOne = content["CSC450WorkflowOne"]
		csc450WorkflowPtsTwo = content["CSC450WorkflowPtsTwo"]
		csc450WorkflowTwo = content["CSC450WorkflowTwo"]
		csc450WorkflowPtsThree = content["CSC450WorkflowPtsThree"]
		csc450WorkflowThree = content["CSC450WorkflowThree"]
		csc450WorkflowPtsFour = content["CSC450WorkflowPtsFour"]
		csc450WorkflowFour = content["CSC450WorkflowFour"]
		csc450WorkflowPtsFive = content["CSC450WorkflowPtsFive"]

		amotionsWorkflowOne = content["AmotionsWorkflowOne"]
		amotionsWorkflowTwo = content["AmotionsWorkflowTwo"]

		amotionsPts = content["AmotionsPts"]
		amotionsPtsTwo = content["AmotionsPtsTwo"]
		amotionsWorkflowThree = content["AmotionsWorkflowThree"]

		threeCommands = content["ThreeCommands"]

		generalTips = content["GeneralTips"]
		generalTips = modify_list_with_code_separation(generalTips, "Code")

		gitCommands = content["GitCommands"]
		
		createFork = content["CreateFork"]
		createFork = modify_list_with_code_separation(createFork, "Code")

		resetBranch = content["ResetBranch"]
		resetBranch = modify_list_with_code_separation(resetBranch, "Code")

		existingFolderPts = content["ExistingFolderPts"]
		existingFolder = content["ExistingFolder"]

		Title = "GitHub 🐙"
		Link = "/compsci/GitHub"
		Results = (text + scrollLinks + setupGithub
				  + createGitHubRepo + setupSecondGitHub
				  + createSecondGitHubRepo + csc450WorkflowPtsOne 
				  + csc450WorkflowOne + csc450WorkflowPtsTwo 
				  + csc450WorkflowTwo + csc450WorkflowPtsThree 
				  + csc450WorkflowThree + csc450WorkflowPtsFour 
				  + csc450WorkflowFour + csc450WorkflowPtsFive
				  + amotionsWorkflowOne + amotionsWorkflowTwo 
				  + amotionsPts + amotionsPtsTwo + amotionsWorkflowThree 
				  + threeCommands + generalTips + gitCommands 
				  + createFork + resetBranch
				  + existingFolderPts + existingFolder)

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

# Jobs
def get_offersreceived():
	with open("../src/data/Jobs/OffersReceived.json", "r") as file:
		content = json.load(file)


		text = content["text"]
		internships = content["internships"]
		fullTime = content["fullTime"]
		interviews = content["interviews"]

		Title = "Offers I've Received 🤝🏻"
		Link = "/Jobs/OffersReceived"
		Results = text + internships + fullTime + interviews

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_howtogetajob():
	with open("../src/data/Jobs/HowToGetAJob.json", "r") as file:
		content = json.load(file)

		text = content["Text"]

		tips = content["Tips"]
		tips = [transform_json(tip) for tip in tips]

		Title = "How To Get a Job 💡"
		Link = "/Jobs/HowToGetAJob"
		Results = text + tips

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_interviews():
	with open("../src/data/Jobs/InterviewTips.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		tips = content["Tips"]

		Title = "Interview Tips 💬"
		Link = "/jobs/InterviewTips"
		Results = text + tips

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_wheretoapply():
	with open("../src/data/Jobs/WhereToApply.json", "r") as file:
		content = json.load(file)

		text = content["text"]
		companies = content["Companies"]

		Title = "Where To Apply 🧳"
		Link = "/Jobs/WhereToApply"
		Results = text + companies

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_careerpathadvice():
	with open("../src/data/Jobs/CareerPathAdvice.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		advice = content["CareerPathAdvice"]

		Title = "Career Path Advice 🧭"
		Link = "/Jobs/CareerPathAdvice"
		Results = text + advice

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_resumetemplatetext():
	with open("../src/data/Jobs/ResumeTemplateText.json", "r") as file:
		content = json.load(file)

		information = content["information"]

		Title = "Resume Template 📄"
		Link = "/Jobs/ResumeTemplate"
		Results = information

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

# LinkedIn
def get_whatislinkedin():
	with open("../src/data/LinkedIn/WhatIsLinkedIn.json", "r") as file:
		content = json.load(file)
		
		info = content["Info"]

		Title = "What Is LinkedIn? 🌐"
		Link = "/LinkedIn/WhatIsLinkedIn"
		Results = info

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_linkedintips():
	with open("../src/data/LinkedIn/LinkedInTips.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		tips = content["LinkedInTips"]

		tips = [transform_json(tip) for tip in tips]

		Title = "LinkedIn Tips 🧐"
		Link = "/LinkedIn/LinkedinTips"
		Results = text + tips

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_setupprofile():
	with open("../src/data/LinkedIn/SetupProfile.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		instructions = content["Instructions"]

		Title = "Setup a Profile 🤳🏻"
		Link = "/LinkedIn/SetupProfile"
		Results = text + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	
def get_setupjobalerts():
	with open("../src/data/LinkedIn/SetupJobAlerts.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		instructions = content["Instructions"]

		Title = "Setup Job Alerts 🔔"
		Link = "/LinkedIn/SetupJobAlerts"
		Results = text + instructions

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_contacts():
	with open("../src/data/LinkedIn/Contacts.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		contacts = content["Contacts"]

		Title = "Contacts 👤"
		Link = "/LinkedIn/Contacts"
		Results = text + contacts

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }


# Other
def get_keyboardshortcuts():
	with open("../src/data/Other/KeyboardShortcuts.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		shortcuts = content["Shortcuts"]

		Title = "Keyboard Shortcuts ⚡️"
		Link = "/Other/KeyboardShortcuts"
		Results = text + shortcuts

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_appstodownload():
	with open("../src/data/Other/AppsToDownload.json", "r") as file:
		content = json.load(file)
		
		text = content["Text"]
		apps = content["AppsToDownload"]
		kinda = content["Kinda Obviously"]


		Title = "Apps To Download 📲"
		Link = "/Other/AppsToDownload"
		Results = text + apps + kinda

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_uncwpics():
	with open("../src/data/Other/UncwPics.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		pics = content["Pics"]

		Title = "UNCW Pictures 📸"
		Link = "/Other/UncwPics"
		Results = text + pics

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_terminalcommands():
	with open("../src/data/Other/TerminalCommands.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		creation = content["Creation"]
		navigation = content["Navigation"]
		display = content["Display"]
		delete = content["Delete"]
		programming = content["Programming"]
		practice = content["Practice"]

		Title = "Terminal Commands ⌨️"
		Link = "/Other/TerminalCommands"
		Results = text + creation + navigation + display + delete + programming + practice

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_generaltips():
	with open("../src/data/Other/GeneralTips.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		tips = content["GeneralTips"]

		Title = "General Tips 🧘🏻"
		Link = "/Other/GeneralTips"
		Results = text + tips

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_memes():
	with open("../src/data/Other/Memes.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		memes = content["Memes"]

		Title = "Memes 😂"
		Link = "/Other/Memes"
		Results = text + memes

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_csstuffilike():
	with open("../src/data/Other/CsStuffILike.json", "r") as file:
		content = json.load(file)

		text = content["Text"]
		csStuff = content["CsStuff"]
		code = content["Code"]

		Title = "CS Stuff I Like ❤️"
		Link = "/Other/CompSciStuff"
		Results = text + csStuff + code

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }

def get_home():
	with open("../src/data/Home.json", "r") as file:
		content = json.load(file)

		home = content["Home"]

		Title = "Home 🏠"
		Link = "/"
		Results = home

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	
def get_contact_me():
	with open("../src/data/Contact.json", "r") as file:
		content = json.load(file)

		contact = content["Contact"]

		Title = "Contact Me ✉️"
		Link = "/ContactMe"
		Results = contact

		ensure_string(Title)
		ensure_string(Link)
		ensure_list(Results, Title)

		return { "Title": Title, "Link": Link, "Results": Results }
	

classestoavoid = get_classestoavoid()
classrecommendations = get_classrecommendations()
usefulcertifications = get_usefulcertifications()
cscdescriptions = get_cscdescriptions()
classesivetaken = get_classesivetaken()
compsciminor = get_compsciminor()
compsciminor = get_compsciminor()
vscodeshortcuts = get_vscodeshortcuts()
visualstudiocode = get_visualstudiocode()
settings = get_settings()
uiux_tips = get_uiux_tips()
compscitips = get_compscitips()


displaylinks = get_display_links()
node = get_node()
vue = get_vue()
react = get_react()
angular = get_angular()
templates = get_templates()
ghpages = get_gh_pages()
viteghpages = get_vite_gh_pages()
aws = get_aws()
docker = get_docker()
flasksqlite3 = get_flask_sqlite3()
deploysqlite = get_deploy_sqlite()
flaskpostgresql = get_flask_postgresql()
deploypostgresql = get_deploy_postgresql()
reactspring = get_react_spring()
deployspring = get_deploy_spring()

complexmysql = get_complex_mysql()
deploymysql = get_deploy_mysql()

intellij = get_intellij()
eclipse = get_eclipse()
cisco = get_cisco()
php = get_php()
tiktok = get_tiktok()
youtube = get_youtube()

googleapi = get_google_api()
redditapi = get_reddit_api()
spotifyapi = get_spotify_api()
openai = get_openai_api()
linkedin = get_linkedin_api()
redditbot = get_reddit_bot()
redditbotaws = get_reddit_bot_aws()

swiftfirebase = get_swift_firebase()
developermode = get_developermode()
basicsqlite = get_basic_sqlite()
prism = get_prism()
swiftdata = get_swift_data()


postman = get_postman()
flashdrive = get_flash_drive()
pyserver = get_python_server()
nodeserver = get_node_server()

emailjs = get_emailjs()

pyicloud = get_pyicloud()

oauth = get_oauth()

excel = get_excel()
exepython = get_executable_python()

vscodeextensions = get_vscodeextensions()
github = get_github()
offersreceived = get_offersreceived()
howtogetajob = get_howtogetajob()
interviewtips = get_interviews()
wheretoapply = get_wheretoapply()
careerpathadvice = get_careerpathadvice()
resumetemplatetext = get_resumetemplatetext()
whatislinkedin = get_whatislinkedin()
linkedintips = get_linkedintips()
setupprofile = get_setupprofile()
setupjobalerts = get_setupjobalerts()
contacts = get_contacts()
keyboardshortcuts = get_keyboardshortcuts()
appstodownload = get_appstodownload()
uncwpics = get_uncwpics()
terminalcommands = get_terminalcommands()
generaltips = get_generaltips()
memes = get_memes()
csstuffilike = get_csstuffilike()
home = get_home()
contactme = get_contact_me()


all_data = [
	home, 

	wheretoapply,
	resumetemplatetext,
	howtogetajob,
	offersreceived,
	interviewtips,
	careerpathadvice,

	whatislinkedin,
	setupprofile,
	setupjobalerts,
	linkedintips,
	contacts,

	classrecommendations,
	classesivetaken,
	cscdescriptions,
	classestoavoid,
	compsciminor,
	usefulcertifications,

	visualstudiocode,
	github,
	settings,
	uiux_tips,
	vscodeextensions,

	displaylinks,
	node,
	vue,
	react,
	angular,
	templates,
	ghpages,
	viteghpages,
	aws,
	docker,
	flasksqlite3,
	deploysqlite,
	flaskpostgresql,
	deploypostgresql,
	reactspring,
	deployspring,
	complexmysql,
	deploymysql,

	intellij,
	eclipse,
	cisco,
	php,
	tiktok,
	youtube,

	googleapi, 
	redditapi,
	spotifyapi,
	openai,
	linkedin,
	redditbotaws,

	swiftfirebase,
	swiftdata, 
	developermode,

	postman,
	flashdrive,
	pyserver,
	nodeserver,
	emailjs,
	pyicloud,
	oauth,

	basicsqlite,
	excel,
	prism,
	exepython,

	vscodeshortcuts,
	compscitips,

	generaltips,
	appstodownload,
	csstuffilike,
	terminalcommands,
	keyboardshortcuts,
	memes,
	uncwpics,

	contactme
]


remove_md = RemoveMarkdown(all_data)
real_json = remove_md.undo_all_links()


with open("delete.json", "w", encoding='utf-8') as file:
	json.dump(real_json, file, ensure_ascii=False, indent=4)

with open("../src/data/SearchData.json", "w", encoding='utf-8') as file:
	json.dump(real_json, file, ensure_ascii=False, indent=4)
	
escape_html_in_json("delete.json")
escape_html_in_json("../src/data/SearchData.json")

replace_strs("delete.json")
replace_strs("../src/data/SearchData.json")

# Shows unaccounted for escaped html chars 
HtmlCharCollector.show_results("../src/data/SearchData.json")

print("Files created!")
