from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator
from MainApp.models import Countries


# Create your views here.
countries_from_bd = Countries.objects.all()
file_path = '/home/student/Projects/DjangoCountries/country-by-languages.json'
countries = {}
countries_alphabetical_list = []
language_list = []

with open(file_path, 'r') as in_file:
    for line in in_file.readlines():
        ln = line.strip()
        if ln.find('country') > -1:
            country = ln[12:-2]
            letter = country[0]
            if not countries_alphabetical_list.count(letter):
                countries_alphabetical_list.append(letter)
            countries[country] = []
        if len(ln) > 2 and ln.find('languages') == -1 and ln.find('country') == -1:
            lang = ln.strip('",')
            if language_list.count(lang) == 0:
                language_list.append(lang)
            countries[country].append(lang)

countries_alphabetical_list.sort()
language_list.sort()





def main_page(request) -> HttpResponse:
    return render(request, 'index.html')


def countries_list(request) -> HttpResponse:
    page = request.GET.get('page')
    pag = Paginator(list(countries.keys()), 10)
    page_obj = pag.get_page(page)
    context = {
        "page": page,
        "page_obj": page_obj,
        'countries_alphabetical_list': countries_alphabetical_list,
    }
    return render(request, 'countries-list.html', context)


def country_info(request, country: str) -> HttpResponse:
    languages = countries[country]
    context = {
        'country': country,
        'languages': languages
    }
    return render(request, 'country.html', context)


def countries_that_start(request, letter: str) ->HttpResponse:
    countries_list = []

    for country in countries:
        if country.startswith(letter):
            countries_list.append(country)

    context = {
        'letter': letter,
        'countries_list': countries_list
    }
    return render(request, 'countries-that-start-with.html', context)


def language_page(request) ->HttpResponse:
    context = {
        'language_list': language_list
    }
    return render(request, 'language-page.html', context)


def countries_that_speaking(request, language:str) ->HttpResponse:
    countries_list = list()
    for cntr in countries:
        if countries[cntr].count(language) > 0:
            countries_list.append(cntr)
        countries_list.sort()

    context = {
        'language': language,
        'countries_list': countries_list
    }
    return render(request, 'countries-that-speaking.html', context)


