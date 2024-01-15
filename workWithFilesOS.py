import os
from os import path
import datetime 
from datetime import date, time, timedelta

import time


def main():  
    # Print the name of OS
    print(os.name)

    #___________________________________________________________________

    # Check for item existance and type
    print("Item exists:", str(path.exists("textfile.txt")))
    print("Item is a file:", str(path.isfile("textfile.txt")))
    print("Item is a directory:", str(path.isdir("textfile.txt")))

    #___________________________________________________________________

    # Work with file paths
    print("Item's path:", path.realpath("textfile.txt"))
    print("Item's path and name:", path.split( path.realpath("textfile.txt")))

    #___________________________________________________________________

    # Get the modification time
    t= time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
    

    #___________________________________________________________________
    
    # Calculate how long ago the item was modified
    

    
if __name__ == "__main__":
    main()