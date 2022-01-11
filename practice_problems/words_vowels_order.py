with open("sowpods.txt") as file:
    words = []
    vowels = "AEIOU" #should this be a list?
    for line in file:
        line.strip("\n")
        #check each line that there is only one vowel
        #need temp to hold line while the loop runs?
        for letter in vowels:
            if line.count(letter) == 1:
                continue
            words.append(line)
print(words)