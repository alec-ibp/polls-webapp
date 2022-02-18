from .models import Choice, Question

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.

# def index(request):
#     """ 
#     /polls/
#     Args:
#         request: HTTP Request
#     Returns:
#         [Render]: request, template, Dict(Question.objects.all()) 
#     """
#     latest_question_list = Question.objects.all()
    
#     return render(
#         request, 
#         "polls/index.html", 
#         {
#             "latest_question_list": latest_question_list
#         })


# def details(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404

#     question = get_object_or_404(Question, pk=question_id)
#     return render(
#         request,
#         "polls/detail.html",
#         {
#             "question": question
#         }
#     )


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(
#         request,
#         "polls/results.html",
#         {
#             "question": question
#         }
#     )

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    
    def get_queryset(self):
        """ Return the last 5 publish question """
        return Question.objects.order_by("-publish")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Any Choice was selected"
            }
        )
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))