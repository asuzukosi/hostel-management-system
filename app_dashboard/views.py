from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse("Hello, and welcome to the school hostel management system SAAS")