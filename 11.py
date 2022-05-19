from operator import itemgetter

people = [{'first':'Rueven', 'last':'Lerner','email':'reuven@lerner.co.il'},
        {'first':'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
        {'first':'Vladimir', 'last':'Putin', 'email': 'president@kremvax.re'},
        {'first':'Daymond', 'last': 'Alexis', 'email': 'daymondA@gmail.com'}]

def alphabetize_people(person):
    return sorted(person, key=itemgetter('first','last'))
print(alphabetize_people(people))