"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

with open("task02a.txt") as file:
    numbers = file.read().split()
    numbers = list(map(int, numbers))

    triples = []
    n = len(numbers)

    for i in range(0, n, 3):    
        nums = [numbers[i], numbers[i+1], numbers[i+2]]
        nums.sort()
        a = nums[0]
        b = nums[1]
        c = nums[2]
        if a**2 + b**2 == c**2:
            triples.append((a, b, c))
    amount = len(triples)
    question = input(f'There are {amount} Pythagorean triples in this text file, would you like to see them?: ')
    if question == 'Yes' or question == 'yes':
        print(f'The Pythagorean triples in this text file are: {triples}')
    else:
        print("invalid input")

                       
