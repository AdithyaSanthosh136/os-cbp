
used = []
nf = int(input("Enter number of files: "))
for i in range(nf):
    name = input("\nEnter file name: ")
    count = int(input("Enter number of blocks: "))
    blocks = []
    free = True
    for j in range(count):
        b = int(input("Enter block number: "))
        if b in used or b in blocks:
            free = False
        blocks.append(b)
    if free:
        for b in blocks:
            used.append(b)
        print("File", name, "is allocated as:", end=" ")
        for j in range(count):
            print(blocks[j], "->", end=" ")
        print("END")
    else:
        print("Some blocks are already allocated. File", name,"is not allocated.")
print("\nAllocated blocks:", used)
