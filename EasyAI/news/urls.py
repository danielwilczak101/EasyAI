from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="News"),
    path('about/', views.about, name="About"),
    path('form/', views.form, name="Form"),
]
