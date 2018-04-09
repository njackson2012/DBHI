from django.http import HttpResponse

def helloworld(request):
	return HttpResponse("Hello world!")

def home(request):
	return HttpResponse("Welcome Home! Your request was: " + str(request))
