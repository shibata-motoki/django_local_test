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
    if request.method == "GET":
        todo_json_list = [todo.to_dict() for todo in Todo.objects.all()]
        return JsonResponse(todo_json_list, safe=False)
    else: #POST
        params = json.loads(request.body)
        todo = Todo.objects.create(
            title=params["title"],
            task=params["task"])
        return JsonResponse({"id": todo.id})


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