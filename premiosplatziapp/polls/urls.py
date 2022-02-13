from . import views

from django.urls import path


app_name = "polls"

urlpatterns = [
    path("", views.index, name="Description of the view in this case of index"),
    path("<int:question_id>/", views.details, name="details"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/votes", views.votes, name="votes")
    ]