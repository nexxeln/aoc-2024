with open(0) as f:
    lines = f.readlines()

left = []
right = []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

s = sum(abs(a - b) for a, b in zip(left, right))

print(s)
