import os
import requests

#builds a webslides project and adds some boilderplate to index.html	

project_name = input('What is the name of the webslides project? ')

webslides_project = 'webslides_' + project_name

os.mkdir(webslides_project)
os.chdir(webslides_project)
os.mkdir("images")
os.mkdir("css")
os.mkdir("js")


files = { 
	os.path.abspath('css/webslides.css'): 'https://raw.github.com/webslides/WebSlides/master/static/css/webslides.css',
	os.path.abspath('js/webslides.js'): 'https://raw.github.com/webslides/WebSlides/master/static/js/webslides.js',
	os.path.abspath('./index.html'): 'https://raw.github.com/nimmod/boilerplate/main/index.html'
}


for file in files:
	fileName = os.path.basename(file)
	r = requests.get(files[file])
	text_file = open(file, "w")
	print('requesting:' + files[file])
	request = requests.get(files[file])
	n = text_file.write(request.text)
 
	#close file
	text_file.close()

