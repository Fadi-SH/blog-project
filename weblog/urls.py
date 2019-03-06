from django.urls import path
from . import views


urlpatterns = [
    path('', views.weblog, name='weblog'),
    path('<slug>/', views.weblog_detail, name='weblog_detail'),

]
