with open("sowpods.txt") as words:
    reversed_words = []
    for word in words:
        word = word.strip("\n")
        rev_word = word[::-1]
        reversed_words.append(rev_word)
with open("baby_names_2020_short.txt") as names:
    matches = []
    for name in names:
        name = name.strip("\n").upper()
        for word in reversed_words:
            if name == word:
                matches.append(name)
print(matches)

#This code runs slower than baby_scrabble_set.py
#Big O time for this code is O(n^2) and for the other is O(n)

#time python3 baby_scrabble_set.py
#{'LIAM', 'HENRY'}
#real	0m0.260s
#user	0m0.234s
#sys	0m0.013s

#$ time python3 baby_scrabble_list.py
#['LIAM', 'HENRY']
#real	0m1.042s
#user	0m1.026s
#sys	0m0.016s