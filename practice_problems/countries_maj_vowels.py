with open("countries.txt") as file:
    results = []
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for line in file:
        line = line.strip("\n")
        length = len(line)
        vowel_total = 0
        for vowel in vowels:
            vowel_total += line.count(vowel)
        if vowel_total > (length // 2):
            results.append(line)
print(results)