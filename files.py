# def main():
#     # Open a file for writing and create it if it doesn't exist
#     myfile = open("textfile.txt", "w+")
#     # Open the file for appending text to the end

#     # Write some lines of data to the file
#     for i in range(10):
#         myfile.write('New line\n')
#     # Close the file when done
#     myfile.close()
#     # Open the file back up and read the contents


# def main():
#     # Open a file for writing and create it if it doesn't exist
    
#     # Open the file for appending text to the end
#     myfile = open("textfile.txt", "a+")
#     # Write some lines of data to the file
#     for i in range(10):
#         myfile.write('Again line\n')
#     # Close the file when done
#     myfile.close()
#     # Open the file back up and read the contents

# def main():
   
#     # Open the file back up and read the contents
#     myfile=open("textfile.txt", "r")
#     if myfile.mode == 'r':
#         contents = myfile.read()
#     print (contents)
#     myfile.close()

def main():
   
    # Open the file back up and read the contents
    myfile=open("textfile.txt", "r")
    if myfile.mode == 'r':
        fl=myfile.readlines()
        print (fl)
    myfile.close()

    

if __name__ == "__main__":
    main()