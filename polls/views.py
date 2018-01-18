from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print("afjejab")
    return HttpResponse("Got started sadafw")
    
def testView(request):
    return HttpResponse("This is a test page")

# Create your views here.
