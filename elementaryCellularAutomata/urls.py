from django.urls import path

from . import views

app_name = "elementaryCellularAutomata"

urlpatterns = [
    path('form/', views.WolfForm.as_view(), name='form'),
    path('show/', views.show, name='show'),
]