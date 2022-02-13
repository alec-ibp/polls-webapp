from .models import Question

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

# Create your views here.

def index(request):
    """ 
    /polls/
    Args:
        request: HTTP Request
    Returns:
        [Render]: request, template, Dict(Question.objects.all()) 
    """
    latest_question_list = Question.objects.all()
    
    return render(
        request, 
        "polls/index.html", 
        {
            "latest_question_list": latest_question_list
        })


def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404

    question = get_object_or_404(Question, pk=question_id)

    return render(
        request,
        "polls/detail.html",
        {
            "question": question
        }
    )


def results(request, question_id):
    return HttpResponse(f"This are the results for the question {question_id}")


def votes(request, question_id):
    return HttpResponse(f"This are the votes for the question {question_id}")