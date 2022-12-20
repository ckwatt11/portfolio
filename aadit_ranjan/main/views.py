from django.shortcuts import render

# Create your views here.

def renderHomePage(req):
    # req -> request
    return render(req, 'main/homepage.html')