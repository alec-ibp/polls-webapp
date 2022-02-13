from . import views

from django.urls import path

urlpatterns = [
    path("", views.index, name="Description of the view in this case of index"),
    path("<int:question_id>/", views.details, name="Question details"),
    path("<int:question_id>/results", views.results, name="Question results"),
    path("<int:question_id>/votes", views.votes, name="Question votes")
    ]