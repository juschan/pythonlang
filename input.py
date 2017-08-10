#input
msg = input("Tell me your name:")
print("Your name is " + msg)

msg = input("Tell me your age:")
age = int(msg)
if age<20:
    print("You are young")
else:
    print("You are old")

#while loops
current = 5
while current <=10 :
    print(current)
    current = current + 1

#use break to break out of current loop
#use continue to continue to next iteration of loop

#do not use for loops to modify lists/dictionaries within the loop
#use while loops instead
