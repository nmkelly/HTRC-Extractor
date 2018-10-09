print("Starting HTRC Data Capsule Archive Extractor..")
print("If you've come across a bug or have a question, contact nicholas-kelly@uiowa.edu")
import tkinter
import os
import shutil
import json
import glob
import zipfile
from shutil import copyfile
from tkinter import filedialog
from tkinter.filedialog import askdirectory
#selecting input, output folders
print("Please select the directory in which your corpus files are contained. This folder should contain all your volumes as compressed archives in subfolders.")	
selectstart = filedialog.askdirectory()
print("Please select the folder in which you would like your pages, full text, and metadata archive placed.")
selectarchive = filedialog.askdirectory()
print("Please select the folder in which you would like your collected full text files placed.")
selectcollected = filedialog.askdirectory()
os.chdir(selectstart)
startloc = os.getcwd()
#Defining functions to be performed on each folder in HTRC archive
def scrapezip():
	#Pulling Metadata from JSON
	htnumber = os.path.basename(os.getcwd())
	jsonpath = (htnumber+".json")
	with open (jsonpath, 'r') as metadata:
		jsonscrape=json.load(metadata)
	scrapeauthor = jsonscrape["names"][0]
	scrapetitle = jsonscrape["title"]
	scrapeHTRCrecnum = jsonscrape["hathitrustRecordNumber"]
	#Make directory based on author name
	authordir = (selectarchive+"/"+scrapeauthor)
	if not os.path.exists(authordir):
	    os.makedirs(authordir)
	#Create subdirectory based on book names
	bookdir = (authordir+"/"+scrapetitle)
	if not os.path.exists(bookdir):
	    os.makedirs(bookdir)
	#Copy json for reference
	copyfile(jsonpath, (bookdir+"/"+scrapeHTRCrecnum+".json"))
	#Open, extract zip
	zippath = (htnumber+".zip")
	zip_ref = zipfile.ZipFile(zippath)
	zip_ref.extractall(bookdir)
	zip_ref.close()
	#Combine txt files in volume directory
	def extandcat():
		for (root, dirs, files) in os.walk(bookdir):
			for name in dirs:
				ctemppath=(os.path.join(root, name))
				print("Opening", ctemppath)
				os.chdir(ctemppath)
				filenames = glob.glob('*.txt')
				filesort = sorted(filenames)
				with open("full.txt", 'w') as f:
					for file in filesort:
						with open(file)as infile:
							f.write(infile.read()+'\n')
	#Copy assembled txt files to collected folder
				shutil.copy("full.txt", selectcollected+"/"+scrapeHTRCrecnum+".txt")
	#
	#NOTE: Here is a location where you can easily run additional scripts on your text file. 
	#Some very basic code is included to read in the full.txt file for use with nltk or other text analysis tools.  
	#txt = open("full.txt")
	#raw = txt.read()
	# your scripts here
	#
	extandcat()
#Run functions on each subfolder in archive folder
for (root, dirs, files) in os.walk(startloc):
        for name in dirs:
                temppath=(os.path.join(root, name))
                print("Opening", temppath)
                os.chdir(temppath)
                scrapezip()
print("Run complete. Check selected folders for text files, metadata, and pages.")
print("If you'd like to run your own scripts on the archives as they extract, check the documentation in the code for locations where you can easily insert scripts.")
