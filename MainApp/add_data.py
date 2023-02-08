import json
from MainApp.models import Countries

file_path = '/home/student/Projects/DjangoCountries/country-by-languages.json'
with open(file_path, 'r') as in_file:
    data = json.load(in_file)

for el in data:
    cnt = el['country']
    lang = ','.join(el['languages'])
    cntr = Countries(country=cnt, languages=lang)
    #cntr.save()








