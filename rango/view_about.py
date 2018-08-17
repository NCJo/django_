from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    html = "Back to main page" + ' ' + '<a href=/rango/>Home</a>'
    return HttpResponse(html)