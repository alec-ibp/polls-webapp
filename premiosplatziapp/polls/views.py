from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello Django")


def details(request, question_id):
    return HttpResponse(f"You are watching the question {question_id}")


def results(request, question_id):
    return HttpResponse(f"This are the results for the question {question_id}")


def votes(request, question_id):
    return HttpResponse(f"This are the votes for the question {question_id}")