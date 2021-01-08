#!/usr/bin/python3
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from tools.util import Tool
path = os.getcwd() #Get the current working directory
inputFilePath = os.path.join(path, "free.pdf")
filesDir = os.path.join(path, "files")
#os.makedirs(filesDir)
files = os.listdir(filesDir)
files.sort()

#Loop through all the files in the directory

try:

    for items in range (len(files)):
        newInputPath = os.path.join(path, "files/")
        inputFile = PdfFileReader(newInputPath + files[items])
        outputFile = PdfFileWriter()
        numberOfPages = inputFile.numPages
    # Loop through the pages and in the input file(s)

        for page in range (numberOfPages):
            pageNumber = inputFile.getPage(page)
            outputFile.addPage(pageNumber)

        password = Tool.generatePassword()

        outputFile.encrypt(password)
        newOutputPath = os.path.join(path, "exported")
        #outputFilePath = newOutputPath+f"/{files[items]}"
        folderName = f"/{files[items]}"
        folderName = folderName[:-4]
        fileName = f"/{files[items]}"
        outputFilePath = newOutputPath + folderName
        outputFileFolder = outputFilePath + fileName
        # print(outputFileFolder)
        try:

            os.makedirs(outputFilePath)
        except FileExistsError:
            print("A file with same name %s already exists and not will be ovewritten" %folderName)
            continue
        # print(outputFilePath)
        outputFilePassword = outputFilePath+f"/{files[items]}"+".txt"


        with open (outputFileFolder, "wb") as f:
            outputFile.write(f)
            print ("Successfully encrypted file as %s \n" %f"{files[items]}" )

        with open (outputFilePassword, 'w') as p:
            p.write(password)
            print ("Successfully generated password as %s " %f"{files[items]}"+".txt" )
except KeyboardInterrupt:
    print("\nCtrl + C detected \n program quitted without completing task")


