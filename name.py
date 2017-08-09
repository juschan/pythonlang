#String manipulation.
name = "ada lovelace"

#Capitalise first letter
print(name.title())

#make upper case
print(name.upper())

#make lower case
print(name.lower())

#string concatenation
first_name = 'ada'
last_name = 'lovelace'
print(first_name + " " + last_name)

#tabs and new lines
new_msg= "\t" + first_name + "\n" + last_name
print(new_msg)

#strip out whitespace
#use rstrip or lstrip to remove from right and left sides
print(new_msg.strip())

#convert numbers to string
print("Happy " + str(23) + "rd Birthday!")
