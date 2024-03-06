test_function = lambda x, y: x*y
#print(test_function(2, 3))

# filter
numbers = [1,2,3,4,5,6,7]

even_numbers = filter(lambda x: x%2 == 0, numbers)

print(list(even_numbers))


numbers = [1,2,3,4,5,6,7]

multiplied = list(filter(lambda x: x*2, numbers))

print(multiplied)