import os

def writeToFile(setOfLinks, filemode):
    """
    Opens a file either to append (filemode = a) to an existing file or to overwtrite existing file (filemode = w)
    writes all the gathered links into that file
    """
    # check for directory
    if not os.path.isdir("target"):
        os.makedirs("target")
    # check for valid filemode
    if filemode != "a" and filemode !="w":
        print("Inavalid Parameter! Filemode can only be \"a\" oder \"w\".")
    else:
        f = open("target/freeudemy.txt", filemode)
        for udemylink in setOfLinks:
            f.write(udemylink + "\r\n")
        f.close()