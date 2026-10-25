
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))
print("\nEnter allocation matrix:")
alloc = []
for i in range(n):
    row = input("P" + str(i) + ": ").split()
    for j in range(m):
        row[j] = int(row[j])
    alloc.append(row)
print("\nEnter request matrix:")
request = []
for i in range(n):
    row = input("P" + str(i) + ": ").split()
    for j in range(m):
        row[j] = int(row[j])
    request.append(row)
work = input("\nEnter available resources: ").split()
for j in range(m):
    work[j] = int(work[j])
finish = [False] * n
for k in range(n):
    for i in range(n):
        if finish[i] == False:
            possible = True
            for j in range(m):
                if request[i][j] > work[j]:
                    possible = False
                    break
            if possible:
                for j in range(m):
                    work[j] = work[j] + alloc[i][j]
                finish[i] = True
                break
deadlock = []
for i in range(n):
    if finish[i] == False:
        deadlock.append("P" + str(i))
if len(deadlock) == 0:
    print("\nNo deadlock detected.")
else:
    print("\nDEADLOCK DETECTED.")
    print("Deadlocked processes:", deadlock)
