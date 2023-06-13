la = [1, 3, 5]
lb = [2, 4, 6]
lx = [0, 0, 0]

r = map(lambda a, b, x: a * x + b, la, lb, lx)

print(list(r))
