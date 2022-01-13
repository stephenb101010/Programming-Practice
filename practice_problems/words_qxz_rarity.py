#Which of the letters Q, X, and Z is the least common?
with open("sowpods.txt") as file:
    rarest = "is the rarest."
    q_total = 0
    x_total = 0
    z_total = 0
    for line in file:
        line = line.replace("\n", "")
        for letter in line:
            if letter == "Q":
                q_total += 1
            elif letter == "X":
                x_total += 1
            elif letter == "Z":
                z_total += 1
if (q_total > x_total) and (q_total > z_total):
    print(f"Q {rarest}")
elif (x_total > q_total) and (x_total > z_total):
    print(f"X {rarest}")
else:
    print(f"Z {rarest}")