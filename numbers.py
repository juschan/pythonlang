#off by one - prints from 1 to 4 only
for value in range(1,5):
	print(value)

	
#create list of numnbers
numbers = list(range(1,6))
print(numbers)

#stats
print("Min: " + str(min(numbers)))
print("Max: " + str(max(numbers)))
print("Sum: " + str(sum(numbers)))

#list comprehension, squaring numbers
squares = [value**2 for value in range(1,11)]
print(squares)

#equivalent to
sq=[]
for value in range(1,11):
	sq.append(value**2)
print(sq)

#copying lists vs referencing same list
#copy list
original = ['a', 'b', 'c']

#copy
new = original[:]

#reference
ref = original	
