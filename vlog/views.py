from django.shortcuts import render
from .models import VlogPost
from django.shortcuts import render, get_object_or_404

# Create your views here.

def vlog_page_view(request):
    vlog_list = VlogPost.objects.order_by("-vlog_post_time")
    return render(request,"vlog/vlog_page.html",{"vlog_list":vlog_list})



def single_vlog_post_view(request, vlog_id):
    vlog_post = get_object_or_404(VlogPost, id=vlog_id)
    return render(request, "vlog/single_vlog_post.html", {"vlog_post": vlog_post})
