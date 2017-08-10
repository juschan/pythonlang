#dictionary
alien_0 = { 'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#add new key-value pairs
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0['x_position'])
print(alien_0['y_position'])
print(alien_0)
 
#modify values in dictionary
alien_0['y_position']=50
print(alien_0['y_position'])

#remove
del alien_0['y_position']
print(alien_0)

#loop through dictionary
for key, value in alien_0.items():
    print(key)
    print(value)
    
#loop through keys
for key in alien_0.keys():
    print(key)
    
#loop through keys - default
for key in alien_0:
    print(key)

#loop through keys in order:
for key in sorted(alien_0.keys()):
    print(key)

#loop through values:
for val in alien_0.values():
    print(val)
