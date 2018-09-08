import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Todo
from django.shortcuts import render, get_object_or_404


error = {"message": "No todo list"}

@csrf_exempt
@require_http_methods(["GET", "POST"])
def todo_list(request):
    todo_json_list = []
    for todo in Todo.objects.all():
        todo_json_list.append(todo.to_dict())
    return JsonResponse(todo_json_list, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return JsonResponse(error)
    return JsonResponse(todo.to_dict())


# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def todo_detail(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#     return JsonResponse(todo.to_dict())