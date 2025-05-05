def make_album(name,title, song_number= None):
    artist = {"artist name":name.title(), "Album title":title.title()}
    if song_number:
        artist["streams"] = song_number
    return artist 

while True:
    print("\nLets talk music")
    print("press 'q' to quit the questionnare at any point.")
    fav_artist = input("who is your favourite artist? ")
    if fav_artist.lower() == "q":
        break 
    fav_album =  input("what is your favourite album? ")
    if fav_album.lower() =="q":
        break

    new_input = make_album(fav_artist,fav_album)
    print(new_input)
