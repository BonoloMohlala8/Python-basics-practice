from pathlib import Path

def count_words(path):
    '''Count the approximate number of words in a file'''
    try: 
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError: 
        print(f"Sorry, the file {path} doesn't exist")
    else: 
        #count number of words in the file
        words = contents.split()
        number_words = len(words)
        print(f"The file {path} has about {number_words} words in it.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames: 
    path = Path(filename)
    count_words(path)