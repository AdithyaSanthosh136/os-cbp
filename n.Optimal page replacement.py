ref = input("Enter reference string: ").split()
for i in range(len(ref)):
    ref[i] = int(ref[i])
f = int(input("Enter number of frames: "))
frame = []
faults = 0
print("\nPage\tFrames\t\tStatus")
for i in range(len(ref)):
    page = ref[i]
    if page in frame:
        print(page, "\t", frame, "\t", "Hit")
    else:
        if len(frame) < f:
            frame.append(page)
        else:
            far = -1
            pos = 0
            for j in range(len(frame)):
                if frame[j] in ref[i + 1:]:
                    nxt = ref[i + 1:].index(frame[j])
                else:
                    nxt = len(ref)
                if nxt > far:
                    far = nxt
                    pos = j
            frame[pos] = page
        faults = faults + 1
        print(page, "\t", frame, "\t", "Fault")
print("\nTotal page faults =", faults)
print("Total page hits =", len(ref) - faults)
