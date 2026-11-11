ref = input("Enter reference string: ").split()
for i in range(len(ref)):
    ref[i] = int(ref[i])
f = int(input("Enter number of frames: "))
frame = []
last = []
faults = 0
print("\nPage\tFrames\t\tStatus")
for i in range(len(ref)):
    page = ref[i]
    if page in frame:
        last[frame.index(page)] = i
        print(page, "\t", frame, "\t", "Hit")
    else:
        if len(frame) < f:
            frame.append(page)
            last.append(i)
        else:
            pos = 0
            for j in range(len(frame)):
                if last[j] < last[pos]:
                    pos = j
            frame[pos] = page
            last[pos] = i
        faults = faults + 1
        print(page, "\t", frame, "\t", "Fault")
print("\nTotal page faults =", faults)
print("Total page hits =", len(ref) - faults)
