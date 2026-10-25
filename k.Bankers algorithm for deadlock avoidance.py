
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))
print("\nEnter allocation matrix:")
alloc = []
for i in range(n):
    row = input("P" + str(i) + ": ").split()
    for j in range(m):
        row[j] = int(row[j])
    alloc.append(row)
print("\nEnter maximum matrix:")
maxm = []
for i in range(n):
    row = input("P" + str(i) + ": ").split()
    for j in range(m):
        row[j] = int(row[j])
    maxm.append(row)
work = input("\nEnter available resources: ").split()
for j in range(m):
    work[j] = int(work[j])
need = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(maxm[i][j] - alloc[i][j])
    need.append(row)
print("\nNeed matrix:")
for i in range(n):
    print("P" + str(i), ":", need[i])
finish = [False] * n
safe = []
for k in range(n):
    for i in range(n):
        if finish[i] == False:
            possible = True
            for j in range(m):
                if need[i][j] > work[j]:
                    possible = False
                    break
            if possible:
                for j in range(m):
                    work[j] = work[j] + alloc[i][j]
                finish[i] = True
                safe.append("P" + str(i))
                break
if len(safe) == n:
    print("\nThe system is in a SAFE state.")
    print("Safe sequence:", safe)
else:
    print("\nThe system is in an UNSAFE state. Deadlock may occur.")
