alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    

#new example
aliens=[]

for alien_no in range(30):
    new_alien= {'color': 'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
    
for alient in aliens[:5]:
    print(alien)


#list in dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'cheese']
}

#dictionary in dictionary
users = {
    'user1': {
        'firstname': 'john',
        'lastname': 'smith',
        'location': 'UK'
    },
    'user2': {
        'firstname': 'mary',
        'lastname': 'bing',
        'location': 'USA'
    }
}
