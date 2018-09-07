from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the memo index.")

def post_list(request):
    return render(request, 'anything/post_list.html', {})
