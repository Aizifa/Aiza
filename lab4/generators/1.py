import math
def squares(n):
    for i in range (1, int(math.sqrt(n))+1):
        yield i*i
n = int(input("input num "))  
square1 = squares(n)
for square in square1:
    print(square)

#OR   

N=int(input("input num "))
def generate_squares(N):
    for i in range(1, N + 1):
        yield i**2
squares_generator = generate_squares(N)
for square in squares_generator:
    print(square)        