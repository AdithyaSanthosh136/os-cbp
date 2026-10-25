
n = int(input("Enter number of processes: "))
bt = []
pr = []
p = []
for i in range(n):
    b = int(input("Enter burst time of P" + str(i + 1) + ": "))
    q = int(input("Enter priority of P" + str(i + 1) + ": "))
    bt.append(b)
    pr.append(q)
    p.append("P" + str(i + 1))
for i in range(n):
    for j in range(i + 1, n):
        if pr[j] < pr[i]:
            pr[i], pr[j] = pr[j], pr[i]
            bt[i], bt[j] = bt[j], bt[i]
            p[i], p[j] = p[j], p[i]
wt = [0] * n
tat = [0] * n
for i in range(1, n):
    wt[i] = wt[i - 1] + bt[i - 1]
for i in range(n):
    tat[i] = wt[i] + bt[i]
print("\nProcess\tPriority\tBT\tWT\tTAT")
for i in range(n):
    print(p[i], "\t", pr[i], "\t\t", bt[i], "\t", wt[i], "\t", tat[i])
print("\nAverage Waiting Time =", round(sum(wt) / n, 2))
print("Average Turnaround Time =", round(sum(tat) / n, 2))
