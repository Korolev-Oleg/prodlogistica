from django.shortcuts import render
from django.http import HttpResponse

HttpResponse('', content_type='html')


def robots(request):
    return render(request, 'templates/robots.txt', content_type="text/plain")
