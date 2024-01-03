try:
    fh=open("textfile","w")
    fh.write("Test File")
finally:   
    fh.close()
    print("File is Clossing..")