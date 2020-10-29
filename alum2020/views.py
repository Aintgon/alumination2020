from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def gall(request):
    return render(request,'gall.html')
