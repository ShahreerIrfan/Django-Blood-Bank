from django.shortcuts import render

# Create your views here.

def vlog_page_view(request):
    return render(request,"vlog/vlog_page.html")