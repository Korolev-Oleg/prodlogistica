from django.http import HttpResponse


def protected_static(request):
    # if request.user.is_staff:
    response = HttpResponse()
    response['Content-Type'] = ''
    response['X-Accel-Redirect'] = request.path
    return response

    # else:
    #     return HttpResponse(status=400)
