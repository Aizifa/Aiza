from itertools import permutations
def print_permutations():
    x=input()
    y=permutations(x)
    for i in y:
        print(''.join(i))
print_permutations()        