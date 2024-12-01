with open(0) as f:
    lines = f.readlines()

left = []
right = []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

counts = {}
for n in right:
    counts[n] = counts.get(n, 0) + 1

s = sum(n * counts.get(n, 0) for n in left)

print(s)
