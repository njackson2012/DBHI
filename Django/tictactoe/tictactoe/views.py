from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hello world!")

def home(request):
    return HttpResponse("Welcome page!")