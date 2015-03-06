import glob

filetype = raw_input("What is the file extension to be combied?: ") #Asks the user for the extension used by files to be combined
filetype = "*." + filetype                                          #Adds a wildcard and . to the filetype to be used by the glob function
filenameList = glob.glob(filetype)                                  #Returns a list of all txt files in the directory the program is in
print filenameList

cFilename = raw_input("What should the combined file be called?: ") #Asks the user for what the combined filename should be

combFile = open(cFilename, "w")                                     #Creates and opens a file called whatever the user entered and sets the open mode to write

for x in filenameList:                                              #Goes through the list of files and opens each one, adds its contents to combFile and closes it
    copyFile = open(x, "r")
    lineStr = copyFile.readline()                                   #Gets the first line from the file to be copied and sets the value of lineStr to it
    while lineStr != "":                                            #Loops through the file until a line that is empty
        #lineStr = lineStr[:-1]                                     #Removes the endline character from the line
        combFile.write(lineStr)                                     #Writes the line to be copied to the new file
        lineStr = copyFile.readline()                               #Gets the new line to be copied
    copyFile.close()                                                #Closes the file once it has been fully copied
    combFile.write("\n")                                            #Adds a newline character to the first line of the next file is copied onto a new line
    
    
combFile.close()                                                    #Closes the combined file
