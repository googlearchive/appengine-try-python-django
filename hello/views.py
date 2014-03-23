from django import http

def home(request):
    return http.HttpResponse('Hello World!')
