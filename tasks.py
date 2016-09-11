from invoke import task, run
from datetime import datetime
import glob
import os
from os.path import splitext, basename, isfile

# render all md and copy stuff - this stages a working copy of the site in ..
@task
def build(ctx):
	# find all md files in . and render into .
	print("building:")
	file_list =  glob.glob('./*.md');
	print(file_list)
	file_list.remove("./README.md")
	for file in file_list:
		fileBase = basename(splitext(file)[0])# strip path and extension from file name
		print("   " + file + " -> " + fileBase +".html")
		run("pandoc -o " + fileBase + ".html -c style.css --data-dir . --template template.html --metadata date=" + datetime.now().strftime("%Y/%m/%d") + " ./" + fileBase + ".md")
