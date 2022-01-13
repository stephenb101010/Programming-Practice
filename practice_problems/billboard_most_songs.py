with open("billboard100_2000.csv") as file:
    song_artist = {}
    for line in file:
        line = line.strip("\n")
        line = line.split(",")
        if line[0] == "rank":
            continue
        song_artist[line[1]] = line[2]
    artists = list(song_artist.values())
    number_songs = 0
    performer = ""
    for artist in artists:
        if artists.count(artist) >= number_songs:
            number_songs = artists.count(artist)
            performer = artist