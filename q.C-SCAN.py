n = int(input("Enter number of requests: "))
req = []
for i in range(n):
    r = int(input("Enter request " + str(i+1) + ": "))
    req.append(r)
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size (max cylinder): "))
left = []
right = []
for r in req:
    if r < head:
        left.append(r)
    else:
        right.append(r)
for i in range(len(left)):
    for j in range(i + 1, len(left)):
        if left[i] > left[j]:
            left[i], left[j] = left[j], left[i]
for i in range(len(right)):
    for j in range(i + 1, len(right)):
        if right[i] > right[j]:
            right[i], right[j] = right[j], right[i]
seek_sequence = []
for r in right:
    seek_sequence.append(r)
seek_sequence.append(disk_size - 1)
seek_sequence.append(0)
for r in left:
    seek_sequence.append(r)
print("\nSeek Sequence:")
total = 0
current = head
for s in seek_sequence:
    total = total + abs(s - current)
    current = s
    print(s, end=" ")
print("\n\nTotal Head Movement =", total)
