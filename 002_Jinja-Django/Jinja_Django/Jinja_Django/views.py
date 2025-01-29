from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world! , You're At Home Page")
    return render(request, 'website/home.html')
    # We Can Have Folder For HTML Filee As Well
    # return render(request, 'folderName/home.html')
