with open("sowpods.txt") as file:
    longest = ""
    for line in file:
        line = line.replace("\n", "")
        reversed_line = line[::-1]
        if line == reversed_line:
            if len(line) > len(longest):
                longest = line
print(longest)