from django.urls import path,include
from django.views.generic import TemplateView
from . import views

app_name='reqs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/',TemplateView.as_view(template_name='reqs/about.html'),name='about'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/detail',views.FileView.as_view(),name='file_detail'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.reqs_logout)
]