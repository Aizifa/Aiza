def squares_from_a_to_b(a, b):
    for i in range(a, b+1):
        yield i * i

a = int(input())
b = int(input())
sq = squares_from_a_to_b(a, b)
print(*sq)
