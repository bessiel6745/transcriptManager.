"""
Authors: Bessie Li
Consulted: n/a
Date: 11/7/23
Purpose: transcript Manager 

"""

def onlyEvents(fileinput, fileoutput):
    """this function opens a file and transfers into the output file if it isn't a message"""
    with open(fileinput, "r") as f:
        n = f.read()
        m = n.splitlines()
    with open(fileoutput, "w") as f1:
        for x in m:
            if ":" not in x:
                f1.write(x+"\n")
                
                
def listSenders(inputfile, outputfile):
    """this function reads the first file and adds the user to the output file if it's not already in there"""
    list = []
    with open(inputfile, "r") as f:
        for x in f:
            if ":" in x:
                first = x.split(":")
                second = first[0].strip()
                if second not in list:
                    list.append(second)
    with open(outputfile, "w") as f1:
        for y in list:
            f1.write(y+"\n")
            
def messagesWithWord(inputf, string, output):
    """this function opens the input file and puts user and message in the output file if the string is in the message"""
    list = []
    with open(inputf, "r") as f:
        for x in f:
            if ":" in x:
                first = x.split(":")
                second = first[1].strip()
                if string.lower() in second.lower():
                    list.append(x)
    with open(output, "w") as f1:
        for y in list:
            f1.write(y)
            
def messagesFromUser(inputfile1, username, outputfile2):
    """this function opens a file and puts in the message from that file into the output if username is in the user"""
    list = []
    with open(inputfile1, "r") as f:
        for x in f:
            if ": " in x:
                first = x.split(": ")
                if username.lower() in first[0].strip().lower() :
                    second = first[1].strip()
                    list.append(second)
    with open(outputfile2, "w") as f1:
        for y in list:
            f1.write(y+"\n")
