#!/usr/bin/python3
from PyPDF2 import PdfFileReader, PdfFileWriter
import os, subprocess
from tools.util import Tool, Colours
path = os.getcwd() #Get the current working directory
filesDir = os.path.join(path, "Files/")
# List all files in the 
files = os.listdir(filesDir)
files.sort()
c =Colours()

#Loop through all the files in the directory
print (c.BLINK + c.BOLD + c.WARNING+"Encrypting file please wait..." +c.END)

try:

    for items in range (len(files)):
        inputFile = PdfFileReader(filesDir + files[items])
        outputFile = PdfFileWriter()
        numberOfPages = inputFile.numPages
    # Loop through the pages and in the input file(s)

        for page in range (numberOfPages):
            pageNumber = inputFile.getPage(page)
            outputFile.addPage(pageNumber)

        password = Tool.generatePassword()

        outputFile.encrypt(password)
        newOutputPath = os.path.join(path, "Encrypted")
        folderName = f"/{files[items]}/"
        folderName = folderName[:-4]
        fileName = f"{files[items]}"
        outputFilePath = newOutputPath + folderName+'/'
        outputFileFolder = outputFilePath + fileName 
        try:

            os.makedirs(outputFilePath)
        except FileExistsError:
            print( c.WARNING+ "A file with name %s already exists and not will be ovewritten" %fileName + c.END)
            continue

        outputFilePassword = outputFilePath+f"/{files[items]}"+".txt"


        with open (outputFileFolder, "wb") as f:
            outputFile.write(f)
            print (c.SUCCESS + "Successfully encrypted file as " + c.BOLD +fileName + c.END )

        with open (outputFilePassword, 'w') as p:
            p.write(password)
            print (c.SUCCESS + "Successfully generated password for " + c.BOLD +fileName + c.END )
except KeyboardInterrupt:
    subprocess.call('clear', shell=True)
    print(c.DANGER +"\nCtrl + C detected \n Program terminated without completing task" +c.END)


