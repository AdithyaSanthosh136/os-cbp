n = int(input("Enter number of processes: ")) 
bt = []
for i in range(n):
  b = int(input("Enter burst time of P" + str(i + 1) + ": "))
  bt.append(b)
wt = [0] * n 
tat = [0] * n
for i in range(1,n):
  wt[i] = wt[i - 1] + bt[i - 1]
for i in range(n):
  tat[i] = wt[i] + bt[i]
print("\nProcess\tBT\tWT\tTAT") 
for i in range(n):
  print("P" + str(i + 1), "\t", bt[i], "\t", wt[i], "\t", tat[i])
print("\nGantt Chart:") 
for i in range(n):
  print(wt[i], " P" + str(i + 1), " ", end="") 
print(tat[n - 1])
print("\nAverage Waiting Time =", round(sum(wt) / n, 2)) 
print("Average Turnaround Time =", round(sum(tat) / n, 2))
