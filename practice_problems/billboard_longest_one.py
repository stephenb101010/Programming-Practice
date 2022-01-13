with open("billboard100_2000.csv") as file:
    number_ones = []
    for line in file:
        line = line.strip("\n")
        line = line.split(",")
        song_artist =[]
        if line[0] == "rank":
            continue
        title = line[1]
        artist = line[2]
        if line[0] == "1":
            song_artist.append(title)
            song_artist.append(artist)
            number_ones.append(song_artist)
    number_ones.sort()
    longest_run = 0
    for entry in number_ones:
        if number_ones.count(entry) > longest_run:
            longest_run = number_ones.count(entry)
            artist_final = entry[1]
            song = entry[0]
    print(f"'{song}' by {artist_final} was number one for {longest_run} weeks.")