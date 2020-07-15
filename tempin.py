#!/usr/local/bin/python3

import argparse
import os
from txtExtension import txtRun

parser = argparse.ArgumentParser(prog= "tempin', description='Enter path to template file")

parser.add_argument("path", help="enter the FULL path to template file")

parser.add_argument("-s", "--save", help="save template path to specified name")

args = parser.parse_args()

if os.path.isfile(args.path):
    print("File exists: "+os.path.basename(args.path))

    with open("templateNamesFile.txt", "a+") as tnf:
        tnf.seek(0)
        tnfText = tnf.read()

        if args.path not in tnfText:
            saveName = input("What would you like to save your path name to for quicker access? (Saved to templateNamesFile.txt) ")

            tnf.write(saveName + ": " + args.path+ "\n")
        else:
            tnf.seek(0)
            for line in tnf.readlines():
                if args.path in line:
                    print("File already exists and named as '" + line[:line.index(":")] + "'")
                    break
    
    txtRun(args.path)

else:
    if os.path.isfile("templateNamesFile.txt"):
        with open("templateNamesFile.txt") as tnf:
            tnfLines = tnf.readlines()
            for line in tnfLines:
                if args.path == line[:line.index(":")]:
                    print("Saved file '" + args.path + "' exists")
                    aftColonIndex = line.index(":")+2

                    nlsIndex = line.index("\n")

                    obtainedFile = line[aftColonIndex:nlsIndex]

                    txtRun(obtainedFile)

                    break

                else:
                    if line == tnfLines[len(tnfLines)-1]:
                        print("\nERROR: no such file named '" + str(args.path) + "' was found" )
                    
                    

    else:
        print('\nERROR: File does not exist')