from django.urls import path

from . import views

app_name = "pasteAsMarkdown"

urlpatterns = [
    path('form/', views.PasteFormMarkdown.as_view() , name='form'),
    path('create/', views.create_url, name="create"),
    path('show/<str:path>', views.show, name='show'),
]