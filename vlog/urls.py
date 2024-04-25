from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.vlog_page_view, name='vlog'),
    path('vlog/<int:vlog_id>/', views.single_vlog_post_view, name='single_vlog_post'),
]