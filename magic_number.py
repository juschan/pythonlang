answer = 17

if answer!=42:
    print("error")
elif answer!=33:
    print("wrong again")
else:
    print("correct")


#instead of answer > 5 and answer <20
if 5 < answer < 20:
    print("within range")

#check if value in list
banned_users = ['andrew', 'john', 'jane']

print('john' in banned_users)
print('ass' in banned_users)

user = 'ass'
if user not in banned_users:
    print(user)



#working with empty lists
toppings = []

if toppings:
    print([x for x in toppings])
else:
    print("no toppings")


#multiple lists
req_toppings = ["cheese", "mushrooms", "tomatoes"]
avail_toppings = ["cheese", "egg", "pineapple"]

for req in req_toppings:
    if req in avail_toppings:
        print(req + " is available and will be added")
    else:
        print(req + " is not available")
        
