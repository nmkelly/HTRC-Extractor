# HTRC-Extractor
HTRC Archive Extractor and Corpus Builder

Nicholas M Kelly, University of Iowa

nicholas-kelly@uiowa.ed

This python script should automate the process of extracting, organizing, and concatenating the individual HTRC volume archives into complete and assembled .txt volumes. 

If you run into issues with package dependencies, run the script in maintenance mode before running it in secure mode. 

You will need to make sure you extract your initial HTRC corpus before running this script. After this extraction, you should have a collection of folders containing .json and .zip files. 

When you activate the script, it will ask you to specify three folders.
1) The directory in which your corpus files are contained. This folder should contain all your volumes as compressed archives in subfolders.
2) The directory in which you would like your pages, full text, and metadata files placed. This will be created and organized as a author/volume folder and subfolder structure. Each volumes' full, assembled text will be saved here as "full.txt"
3) The directory in which you would like your collected full text files placed. This will be all of you volumes' full text files assembled together. Each will be named after its HTRC ID Number, something like "1234567.txt"

In the code for this script, you will find a section marked where you can insert your own text analysis functions. This will allow you to combine metadata pulled by this script with any text mining data you are intersted in. Some sample code for opening the txt file is included.

If you have any questions, suggestions, bug reports, etc... Please contact me at nicholas-kelly@uiowa.edu

Enjoy the tool and happy text mining. 

