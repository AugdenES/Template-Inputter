
import os
import string

def txtRun(path):
    if ".txt" in os.path.basename(path):

            ##
            ### READ given template file
            ##

            with open(path, "r+") as template:
                print("Reading from "+os.path.basename(path)+":") # Show users the program process for visualization 
            
                templateText = template.read() # Read the template file to later display to the user

                template.seek(0) # Reset pointer to beginning of file

                templateLines = template.readlines() # Read and obtain the list of lines from the file
                
                print("***************************\n")
                print("** Read  **")
                print(templateText+'\n')

                flag = input("What is your input flag? (e.g. '~COMPANY~' -> flag = '~'): ")
                while flag not in templateText or flag == '' or flag in string.ascii_lowercase+string.ascii_uppercase:
                    flag = input("ERROR: flag cannot be found or is invalid. Please enter your flag again. ")


            lineStringLengths = [] # Create array of string lengths of each line in tempateLines

            numFlags = [] # Create array that stores the number of flagged words in each line

            entriesDataDict = {} # Create dictionary to map flagged words to given input names or variables

            flagCount = 0 # Count the number of flagged words in each line to reduce running time for dictionary search

                    
            def templateFlagParser(line):
                nonlocal flagCount
 
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