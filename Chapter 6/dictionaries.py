fav_lang = {
 'jen':'python',
 'sarah':'c',
 'edward':'rust',
 'phil':'python',
 }
friends = ['edward', 'phil']

for name in sorted(fav_lang.keys()):
    print(f"Hi {name.title()}.\n")

    if name in friends:
        language = fav_lang[name].title()
        print(f"\t{name}, i see you love {language}")

    if "jen" not in fav_lang.keys():
        print("john please take the poll!")