from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return render(request,'index.html')
def index_view(request):
    return render(request,'index.html')

def about_view(request):
    return HttpResponse('aoub')

def contact_view(request):
    return HttpResponse('contact') 