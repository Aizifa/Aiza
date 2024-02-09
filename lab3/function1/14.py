from function1 import histogram, solve, my_function

fr = int(input('Enter temperature: '))
print(my_function(fr))


nh = int(input('Enter numheads: '))
nl = int(input('Enter numlegs: '))
ch,rb  = solve(nh, nl)
print(f'chickens: {ch}, rabbits: {rb}')


gist = input()
gist = gist.split()
gist = [int(num) for num in gist]
histogram(gist)