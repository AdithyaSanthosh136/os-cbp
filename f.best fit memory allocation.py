
nb = int(input("Enter number of blocks: "))
block = []
for i in range(nb):
    b = int(input("Enter size of block " + str(i + 1) + ": "))
    block.append(b)
nf = int(input("Enter number of processes: "))
process = []
for i in range(nf):
    p = int(input("Enter size of process " + str(i + 1) + ": "))
    process.append(p)
alloc = [-1] * nf
for i in range(nf):
    best = -1
    for j in range(nb):
        if block[j] >= process[i]:
            if best == -1 or block[j] < block[best]:
                best = j
    if best != -1:
        alloc[i] = best
        block[best] = block[best] - process[i]
print("\nProcess\tSize\tBlock")
for i in range(nf):
    if alloc[i] == -1:
        print(i + 1, "\t", process[i], "\t", "Not Allocated")
    else:
        print(i + 1, "\t", process[i], "\t", alloc[i] + 1)
print("\nFree space left in each block:")
for j in range(nb):
    print("Block", j + 1, ":", block[j])
