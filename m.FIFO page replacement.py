ref = input("Enter reference string: ").split()
for i in range(len(ref)):
    ref[i] = int(ref[i])
f = int(input("Enter number of frames: "))
frame = []
faults = 0
print("\nPage\tFrames\t\tStatus")
for page in ref:
    if page in frame:
        print(page, "\t", frame, "\t", "Hit")
    else:
        if len(frame) < f:
            frame.append(page)
        else:
            frame.pop(0)
            frame.append(page)
        faults = faults + 1
        print(page, "\t", frame, "\t", "Fault")
print("\nTotal page faults =", faults)
print("Total page hits =", len(ref) - faults)
