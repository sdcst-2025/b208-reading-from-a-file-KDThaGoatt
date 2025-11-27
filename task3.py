#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

with open('task03.txt') as file:
    numbers = file.read().split('\n\n')

    sums = []
    sum = 0

    for i in numbers:
        numMod = i.replace('\n', ' ').split()

        sum = 0

        for i in numMod:
            sum += int(i)
        sums.append(sum)
    biggest = max(sums)
    print(f'The largest sum from the text file is {biggest}')