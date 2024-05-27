from django.shortcuts import render

# Create your views here.

def tools(request):
    return render(request,'tools/test.html')

def calculateBMI(request):
    return render(request,"tools/bmi.html")