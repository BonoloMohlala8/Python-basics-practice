cities = {
       'New York': {
        'country': 'America',   
        'fact':'most of the poeple are obese',  
        'population':'10 million',
       },
       'Paris': {
        'country': 'france',   
        'fact':'they are hosting the 2024 olympics',  
        'population':'6 million',
       },
       'Tokyo': {
        'country': 'japan',   
        'fact':'they are the orginators of anime',  
        'population':'8 million', 
       },
}
for city, city_info in cities.items():
    print(f"\n{city}:")
    names = city_info['country']
    names1 = city_info['fact']
    names2 = city_info['population']
    print(f"here is a fun fact about {names}, {names1}. Furthermore the population stands at {names2}")