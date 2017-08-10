try:
    print(5/0)
except ZeroDivisionError:
    print("Cannot divide by zero")


print("Give me two numbers to divide.")
print("Enter q to quit")

while True:
    first=input("\nFirst Number:")
    if first == 'q':
        break
    second = input("\nSecond Number:")
    if second == 'q':
        break
    #Exception handling
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(answer)



#file not found exception example
file = 'alice.txt'

try:
    with open(file) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass # fail silently
else:
    #do something useful, like count words
    words = contents.split()
    num_words = len(words)
    print("file has about " + str(num_words) + 'words')


#create a function, count_words(filename) to do counting
#use list to go through
#filenames = [...]
#for file in filenames: 
#count_words(file)
