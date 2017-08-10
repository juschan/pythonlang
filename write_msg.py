filename='prog.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming\n')
    file_object.write('I love python\n')

with open(filename, 'a') as file_object:
    file_object.write('third message\n')
    file_object.write('fourth message\n')
