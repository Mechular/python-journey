# https://www.learnpython.org/en/Basic_Operators
# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]
# all_numbers = odd_numbers + even_numbers
# print(all_numbers)

# modified loop to sort and print individually
# intro to .sort()

all_numbers = []
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7,9]
all_numbers = odd_numbers + even_numbers
all_numbers.sort()

for x in all_numbers:
    print(x)