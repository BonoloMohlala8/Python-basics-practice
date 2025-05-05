print("Original list:")
countries = ["japan" , "england", "france", "dubai"]
print(countries)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print("\nAlphabetical list:")
print(sorted(countries))
#•	 Show that your list is still in its original order by printing it.
print("\nOriginal list again:\n")
print(countries)
#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print("\n temporarily reversed list: ")
print("Original list:")
sorted(countries)
countries.reverse()
print(countries)
print( " after reversal list:")
countries.reverse()
print(countries)

countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
print(len(countries))
print("i am inviting 4 people")
#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
#through 3-7 (page 46), use len() to print a message indicating the number
#of people you are inviting to dinner.
#3-10. Every Function: Think of something you could store in a list. For example,
#you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items
#and then uses each function introduced in this chapter at least once.