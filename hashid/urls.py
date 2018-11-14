from django.urls import path

from . import views

app_name = "hashid"

urlpatterns = [
    path('form/', views.HashForm.as_view(), name='form'),
    path('show/', views.show, name='show'),
]