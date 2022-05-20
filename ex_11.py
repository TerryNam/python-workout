from operator import itemgetter

def alphabetize_people(person):
    return sorted(person, key=itemgetter('first','last'))

people = [{'first':'Rueven', 'last':'Lerner','email':'reuven@lerner.co.il'},
        {'first':'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
        {'first':'Vladimir', 'last':'Putin', 'email': 'president@kremvax.re'},
        {'first':'Daymond', 'last': 'Alexis', 'email': 'daymondA@gmail.com'}]

print(alphabetize_people(people))