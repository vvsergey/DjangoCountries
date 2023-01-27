from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.
file_path = '/home/student/Projects/DjangoCountries/country-by-languages.json'
countries = {}
with open(file_path, 'r') as in_file:
    for line in in_file.readlines():
        ln = line.strip()
        if ln.find('country') > -1:
            country = ln[12:-2]
            countries[country] = []
        if len(ln) > 2 and ln.find('languages') == -1 and ln.find('country') == -1:
            countries[country].append(ln.strip('",'))

def main_page(request) -> HttpResponse:
    return render(request, 'index.html')


def countries_list(request) -> HttpResponse:
    context = {
        "countries": countries
    }
    return render(request, 'countries-list.html', context)


def country_info(request, country: str) -> HttpResponse:
    context = {

    }
    return render(request, 'country.html', context)
