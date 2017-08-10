#keyword with: closses the file once access is not needed
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
#read line by line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#make a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())

    #work with file contents
    print(len(line.rstrip()))
    
    #limit each line's output
    print(line[:5])
