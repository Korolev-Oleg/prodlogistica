from django.shortcuts import render, render_to_response
from django.http import HttpResponse

HttpResponse('', content_type='html')

# Create your views here.
def robots(request):
    request.get_full_path_info()
    return render_to_response('robots.txt {{ STATIC_URL }}', content_type="text/plain")
