import json
from MainApp.models import Countries


file_path = '/home/student/Projects/DjangoCountries/country-by-languages.json'
with open(file_path, 'r') as in_file:
    for line in in_file.readlines():
        print(line)
    # data = json.load(in_file)

