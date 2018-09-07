from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'memo/index.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the anything index.")

def post_list(request):
    return render(request, 'anything/post_list.html', {})