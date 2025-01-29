from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world! , You're At Home Page")
    return render(request, 'home.html')
    # We Can Have Folder For HTML Filee As Well
    # return render(request, 'folderName/home.html')

def about(request):
    # return HttpResponse("Hello, world! , You're At About Page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hello, world! , You're At Contact Page")
    return render(request, 'contact.html')