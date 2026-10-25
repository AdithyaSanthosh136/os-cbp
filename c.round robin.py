
n = int(input("Enter number of processes: "))
bt = []
for i in range(n):
    b = int(input("Enter burst time of P" + str(i + 1) + ": "))
    bt.append(b)
tq = int(input("Enter time quantum: "))
rem = []
for i in range(n):
    rem.append(bt[i])
wt = [0] * n
tat = [0] * n
time = 0
while True:
    finished = True
    for i in range(n):
        if rem[i] > 0:
            finished = False
            if rem[i] > tq:
                time = time + tq
                rem[i] = rem[i] - tq
                print("P" + str(i + 1), "runs upto time", time)
            else:
                time = time + rem[i]
                rem[i] = 0
                wt[i] = time - bt[i]
                print("P" + str(i + 1), "completed at time", time)
    if finished:
        break
for i in range(n):
    tat[i] = wt[i] + bt[i]
print("\nProcess\tBT\tWT\tTAT")
for i in range(n):
    print("P" + str(i + 1), "\t", bt[i], "\t", wt[i], "\t", tat[i])
print("\nAverage Waiting Time =", round(sum(wt) / n, 2))
print("Average Turnaround Time =", round(sum(tat) / n, 2))
