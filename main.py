import logging
import deleteFileScript
import json

logging.basicConfig(filename='logs/pythonLog.log', level=logging.DEBUG)
opt = True
opt = True
allowed = None
denied = None

print("Processing files...")
print()

with open('filesList.json', 'r') as file:
	data = json.load(file)
	filesList = data[0]['files'].split(",")
	filesExc = data[0]['excluded'].split(",")
	pathABS = data[0]['pathABS']
	pathFiles = data[0]['pathFiles']
	deleteFileScript.deleteAllFiles(filesList,filesExc,pathABS,pathFiles)
print ()
print ("Process finalized...")