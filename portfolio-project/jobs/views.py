from django.shortcuts import render

# Create your views here.

def jason(request):
    return render(request,'jobs/home.html')



def home(request):
    return render(request,'jobs/home.html')