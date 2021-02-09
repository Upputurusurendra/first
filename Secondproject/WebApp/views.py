from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return HttpResponse('<h1>Hai sir how are you.....</h1>')

def Index_page(request,Id):
    return HttpResponse(f"Wellcome to my Webpage....-{Id}")
