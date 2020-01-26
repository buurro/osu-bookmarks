from django.http import HttpResponse


def index(request):
    out = 'wip'
    return HttpResponse(out)
