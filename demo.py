"""
demo.py
Spring 2020 PJW

Define a function that computes the sum of squares of a
list of numbers and returns the result.
"""

#  Define the function. Use type hinting to indicate that the argument
#  is expected to be a list and the return value will be a float

def sumsq(values: list) -> float:
    total = 0
    for item in values:
        total = total + item**2
    return total

#  Use it on a couple of lists

d1 = [1,2,5,3,1]
d2 = [-2,-3,5,1,-1]

d1_ssq = sumsq(d1)
print('\ninput data:',d1)
print('sum of squares:',d1_ssq)

d2_ssq = sumsq(d2)
print('\ninput data:',d2)
print('sum of squares:',d2_ssq)

#  Define a function that reads numbers from a file and returns them
#  as a list. Use type hinting to indicate the argument should be a
#  string and the function returns a list.

def readlist(filename: str) -> list:
    values = []
    fh = open(filename)
    for line in fh:
        line = line.strip()
        values.append( int(line) )
    return values

#  Use the function to read a test file and then compute its
#  sum of squares.

d3 = readlist('demo.txt')

d3_ssq = sumsq(d3)
print('\ninput data:',d3)
print('sum of squares:',d3_ssq)
