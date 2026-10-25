
used = []  
nf = int(input("Enter number of files: "))
for i in range(nf):
    name = input("\nEnter file name: ")
    start = int(input("Enter starting block: "))
    length = int(input("Enter number of blocks: "))
    free = True
    for b in range(start, start + length):
        if b in used:
            free = False
    if free:
        print("File", name, "is allocated to blocks:", end=" ")
        for b in range(start, start + length):
            used.append(b)
            print(b, end=" ")
        print()
    else:
        print("Blocks are already allocated. File", name, "is not allocated.")
print("\nAllocated blocks:", used)
