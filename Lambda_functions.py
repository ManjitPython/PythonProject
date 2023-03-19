# # lambda arguments: expression
# # Using a lambda function to square a number
# square = lambda x: x**3
# print(square(5))  # Output: 25
# Using a lambda function with map() to square each element in a list
numbers = [1, 2, 3, 4, 5, ]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Using a lambda function with filter() to get even numbers from a list
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
