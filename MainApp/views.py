from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.
file_path = '/home/student/Projects/DjangoCountries/country-by-languages.json'
file = open(file_path, 'r')
string_list = file.readlines()
print(string_list)

file.close()

def main_page(request) -> HttpResponse:
    return render(request, 'index.html')

