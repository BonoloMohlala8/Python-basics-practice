#Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
#  Make at least one new function call that includes the number of songs on an album.

def make_album(name,title, song_number= None):
    artist = {"artist name":name.title(), "Album title":title.title()}
    if song_number:
        artist["streams"] = song_number
    return artist 

music1 = make_album('Drake', 'take care')
music2 = make_album('kanye', 'vultures')
music3 = make_album('kendrick lamar', 'damn')
music4 = make_album('Brent faiyaz', 'sonder', 12_000_000)
print(music1)
print(music2)
print(music3)
print(music4)




