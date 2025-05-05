def build_person(first,last,age=None):
    """Return a dictionary of infromation about a rapper"""
    person = {'first name':first, 'last name':last}
    if age:
        person['age'] = age
    return person
#none is a special value, used when variable has no value assigned

