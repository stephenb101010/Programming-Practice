with open("countries.txt") as file:
    result = []
    vowels = ["a","e","i","o","u"]
    for line in file:
        line = line.strip("\n")
        end = len(line) - 1
        first = line[0].lower()      
        last = line[end]
        if (first in vowels) and (last in vowels):
            result.append(line)
print(result)