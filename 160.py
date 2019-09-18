import itertools as it
import math as math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

""" i=1
for motive in it.permutations(notes, 4):
    print(i, " - ", motive)
    i+=1

variations = math.factorial(len(notes))/math.factorial(len(notes)-4)
print(variations) """

i=1
for motive in it.product(notes, repeat=4):
    print(i, " - ", motive)
    i+=1

variations = math.pow(len(notes), 4)
print(variations)
