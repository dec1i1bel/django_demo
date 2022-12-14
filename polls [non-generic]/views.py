from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # ---------------
    # it works, too:
    # ===============================
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('question does not exist')
    # ===============================
    # the same is:
    question = get_object_or_404(Question, pk=question_id)
    # ---------------
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("voting on question %s." % question_id)
