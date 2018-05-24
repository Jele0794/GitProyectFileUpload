import logging
import os

# Delete each file requested by the deleteAllFiles function
def deleteFile(route):
	if os.path.isfile(route):
		try:
			os.remove(route)
			logging.info("Successful delete: %s." % (route))
			return True
		except OSError as e:
			logging.error("Error: %s - %s." % (e.filename,e.strerror))
			return False
	else:
		logging.info("Route not exists: %s." % (route))
		return False

# Iterates in the files defined in the json file
def deleteAllFiles(filesList,filesExc,pathABS,pathFiles):
	deleted = 0
	nodeleted = 0
	for content in filesList:
		if (validator(content,filesExc)):
			if pathABS:
				route = pathFiles + os.sep + content
			else:
				route = os.getcwd() + os.sep + content
			if(deleteFile(route)):
				deleted = deleted + 1
			else:
				nodeleted = nodeleted + 1
	print("Deleted: %d - Not deleted %d." % (deleted, nodeleted))
	return deleted

# Validate that the file is not in the list of exceptions
def validator(archivo,filesExc):
	for file in filesExc:
		if (archivo == file):
			opt = False
			logging.info("The file %s is in the list of exceptions" % (file))
		else:
			opt = True
	return opt