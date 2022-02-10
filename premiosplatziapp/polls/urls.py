from . import views

from django.urls import path

urlpatterns = [
    path("", views.index, name="Description of the view in this case of index")
]