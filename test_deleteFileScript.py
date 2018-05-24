#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import deleteFileScript
import json

with open('filesList.json', 'r') as file:
	data = json.load(file)
	filesList = data[0]['files'].split(",")
	filesExc = data[0]['excluded'].split(",")
	pathABS = data[0]['pathABS']
	pathFiles = data[0]['pathFiles']

class TestDeleteFileScript(unittest.TestCase):
	
	def test_deleteFiles(self):
		self.assertEqual(deleteFileScript.deleteFile(""), False)
# Valida la eliminación de los achivos especificados: assert(4 , 4)
	def test_deleteAllFiles(self):
		self.assertEqual(deleteFileScript.deleteAllFiles(filesList,filesExc,pathABS,pathFiles), 4)

# Opción cuando no hay archivos para eliminar dentro del directorio especificado en fileList.json
	# def test_deleteAllFilesWithoutFiles(self):
	# 	self.assertEqual(deleteFileScript.deleteAllFiles(filesList,filesExc,pathABS,pathFiles), 0)



if __name__ == "__main__":
	unittest.main()