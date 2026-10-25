
used = []
nf = int(input("Enter number of files: "))
for i in range(nf):
    name = input("\nEnter file name: ")
    index = int(input("Enter index block: "))
    if index in used:
        print("Index block is already allocated.")
        continue
    count = int(input("Enter number of data blocks: "))
    blocks = []
    free = True
    for j in range(count):
        b = int(input("Enter block number: "))
        if b in used or b == index or b in blocks:
            free = False
        blocks.append(b)
    if free:
        used.append(index)
        for b in blocks:
            used.append(b)
        print("File", name, ": index block =", index,
              ", data blocks =", blocks)
    else:
        print("Some blocks are already allocated. File", name,
              "is not allocated.")
print("\nAllocated blocks:", used)
