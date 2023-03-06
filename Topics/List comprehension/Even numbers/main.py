# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]

# work with the variable 'my_numbers'
print([my_number for my_number in my_numbers if my_number % 2 == 0])
