from django.urls import path,include
from django.views.generic import TemplateView
from . import views

app_name='reqs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('reqs/<int:pk>/',views.PdfView.as_view(),name='pdf'),
    path('about/',TemplateView.as_view(template_name='reqs/about.html'),name='about'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.reqs_logout),
]