from django.http import HttpResponse


def protected_static(request):
    # if request.user.is_staff:
    response = HttpResponse()
    response['Content-Type'] = ''
    response['X-Accel-Redirect'] = request.path
    response['Cache-Control'] = 'max-age=86400'
    return response

