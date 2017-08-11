from name_function import get_formatted_name

print("Enter q to quit")
while True:
    first = input("Give me first name: ")
    if first == 'q':
        break
    last = input("Give me last name: ")   
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("Your formatted name: " + formatted_name)
