from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.
file_path = '/home/student/Projects/DjangoCountries/country-by-languages.json'
with open(file_path, 'r') as in_file:
    for line in in_file.readlines():
        print(line)

def main_page(request) -> HttpResponse:
    return render(request, 'index.html')


def countries_list(request) -> HttpResponse:
    return render(request, 'countries-list.html')


def country_info(request, country: str) -> HttpResponse:
    context = {

    }
    return render(request, 'country.html', context)
