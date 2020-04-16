from django.shortcuts import render, render_to_response


# Create your views here.
def robots(request):
    return render_to_response('robots.txt', content_type="text/plain")
