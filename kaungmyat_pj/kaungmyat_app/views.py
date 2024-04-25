from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def k(request):
    return render(request, 'k.html')

def s(request):
    return render(request,'s.html')

def n(request):
    return render(request,'n.html')

def m(request):
    return render(request,'m.html')

def o(request):
    return render(request,'o.html')