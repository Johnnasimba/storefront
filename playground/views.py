from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def calc(a, b):
    return a + b
def say_hello(request):
    results = calc(2, 8)
    return render(request, 'hello.html', {'play': 'John', 'results': results})
