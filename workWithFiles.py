#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    # myfile = open("textfile.txt", "w")
    # write some lines of data to the file
    # for i in range(10):
    #     myfile.write("This is some text\n")
    # close the file when done
    # myfile.close()
    #___________________________________________________________________

    # Open the file for appending text to the end
    # myfile = open("textfile.txt", "a")
    # for i in range(10):
    #     myfile.write("This is some NEW text\n")
    # myfile.close()
    #___________________________________________________________________

    # Open the file back up and read the contents
    # myfile = open("textfile.txt", "r")
    # if myfile.mode =='r':
    #     content = myfile.read()
    #     print(content)
    
    # # close the file when done
    # myfile.close()

    #___________________________________________________________________

    # Open the file back up and read the contents lines
    myfile = open("textfile.txt", "r")
    if myfile.mode =='r':
        fl= myfile.readlines()
        for x in fl:
            print(x)
    
    # close the file when done
    myfile.close()

    #___________________________________________________________________
    
    

    
if __name__ == "__main__":
    main()
