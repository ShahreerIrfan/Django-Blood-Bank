from django.shortcuts import render

# Create your views here.
def suppoort(request):
    return render(request,'support/support.html')