#!/usr/local/bin/python3

import argparse
import os 

parser = argparse.ArgumentParser(prog= "tempin', description='Enter path to template file")
parser.add_argument("path", help="enter the path to template file")
parser.add_argument("-s", "--save", help="save template path to specified name")
args = parser.parse_args()
temp = os.path.basename(args.path)

entriesData = [] # Array which holds flagged entry words of interest, without flags or unwanted text)

replaceData = [] # Array which holds are flagged entry words WITH flags. 

if os.path.isfile(args.path):
    print("File exists: "+temp)

    if ".txt" in os.path.basename(args.path):

        ##
        ### READ given template file
        ##

        with open(args.path, "r+") as template:
            print("Reading from "+temp+":") # Show users the program process for visualization 
            
            templateText = template.read() # Read the template file to later display to the user

            template.seek(0) # Reset pointer to beginning of file

            templateLines = template.readlines() # Read and obtain the list of lines from the file
                
            print("***************************\n")
            print("** Read  **")
            print(templateText+'\n')


        flag = input("What is your input flag? (e.g. '~COMPANY~' -> flag = '~'): ")

        lineStringLengths = [] # Create array of string lengths of each line in tempateLines

        updatedLines = [] # Create array of updated lines based on given user input for flagged words

        numFlags = [] # Create array that stores the number of flagged words in each line

        entriesDataDict = {} # Create dictionary to map flagged words to given input names or variables

        flagCount = 0 # Count the number of flagged words in each line to reduce running time for dictionary search

                    
        def templateFlagParser(line):
            global flagCount
 
            if flag in line:

                flagCount += 1

                firstFlag = line.index(flag) + len(flag) # Obtain word index of first Character after the first flag
                secondFlag = line[firstFlag:].index(flag) + firstFlag # Obtain beginning word index of the second flag

                flaggedWord = line[firstFlag:secondFlag] # String between flags
                replaceWord = line[line.index(flag):secondFlag + len(flag)] # String between and including flags

                if replaceWord not in entriesDataDict:
                    updatedWord = input(flaggedWord + "? ") # Obtain desired name or variable input from the user
                    entriesDataDict[replaceWord] = updatedWord # Save user input to dictionary

                templateFlagParser(line[(secondFlag + len(flag)):]) # Recursively call function to line immediateling following current replaceWord

            else:
                numFlags.append(flagCount)
                flagCount = 0

                            
        ##
        ### PARSE templateText to fill in each replaceWord with given user's input
        ##

        for tLine in templateLines:       
            lineStringLengths.append(len(tLine))

            templateFlagParser(tLine)
        
        for key in entriesDataDict.keys():
            if key in templateText:
                templateText = templateText.replace(key, entriesDataDict[key])
  
        ##
        ### WRITE new file from user inputs for their template
        ##

        newFileName = input("What would you like to name your new template file? ")
                      
        with open(newFileName+".txt", "w") as newFile:
            newFile.write(templateText)

else:
    print('\nERROR: File does not exist')
