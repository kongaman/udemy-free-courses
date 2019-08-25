def writeToFile(setOfLinks, filemode):
    """
    Opens a file either to append (filemode = a) to an existing file or to overwtrite existing file (filemode = w)
    writes all the gathered links into that file
    """

    if filemode != "a" and filemode !="w":
        print("Inavalid Parameter! Filemode can only be \"a\" oder \"w\".")
    else:
        f = open("target/freeudemy.txt", "w+")
        for udemylink in setOfLinks:
            f.write(udemylink + "\r\n")
        f.close()