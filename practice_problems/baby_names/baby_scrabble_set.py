with open("sowpods.txt") as words, open("baby_names_2020_short.txt") as names:
    reversed_words = set()
    names_set = set()
    for word in words:
        word = word.strip("\n")
        rev_word = word[::-1]
        reversed_words.add(rev_word)    
    for name in names:
        name = name.strip("\n")
        upper_name = name.upper()
        names_set.add(upper_name)
reversed_words.intersection_update(names_set)
print(reversed_words)
#This code runs faster than baby_scrabble_list.py
#Big O time for this code is O(n) and for the other is O(n^2)

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