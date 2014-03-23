from django import http

def home(request):
    return http.HttpResponse('<h1>Hello World!</h1>')
