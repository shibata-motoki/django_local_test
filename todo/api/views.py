import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Todo
from django.shortcuts import render

@csrf_exempt
@require_http_methods(["GET", "POST"])
def todo_list(request):
    todo_json_list = []
    for todo in Todo.objects.all():
        todo_json_list.append(todo.to_dict())
        return JsonResponse(todo_json_list, safe=False)