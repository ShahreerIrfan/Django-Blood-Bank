from django.shortcuts import render
from .models import VlogPost

# Create your views here.

def vlog_page_view(request):
    vlog_list = VlogPost.objects.order_by("-vlog_post_time")
    return render(request,"vlog/vlog_page.html",{"vlog_list":vlog_list})

