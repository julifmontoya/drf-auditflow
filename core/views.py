from django.http import HttpResponse

def apiMsg(request):
    return HttpResponse("Welcome to my API!")