#lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[0:3])
print(bicycles[0:-2])

#append to list
bicycles.append("racer")
print(bicycles)

#insert
bicycles.insert(1,"duo")
print(bicycles)

#remove
del bicycles[1]
print(bicycles)

#pop - remove last item on list and returns it
popped_item = bicycles.pop()
print(popped_item)

#pop - remove item from any position and return it
popped_item = bicycles.pop(2)
print(popped_item)

#remove item by value
#create error if item not in list
bicycles.remove("specialized")
print(bicycles)

#sort list
bicycles.sort()
print(bicycles)

bicycles.append("racer")
bicycles.append("duo")

#sort list temporarily using sorted
print(sorted(bicycles))
print(bicycles)

#reverse list
bicycles.reverse()
print(bicycles)

#length of list
print(len(bicycles))
