from django.urls import path

from . import views

app_name = "pasteAsMarkdown"

urlpatterns = [
    path('test/', views.index, name="test")
]