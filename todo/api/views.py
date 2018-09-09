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

@csrf_exempt
@require_http_methods(["POST"])
def todo_update(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except json.decoder.JSONDecodeError:
        return JsonResponse(error)
    except Todo.DoesNotExist:
        return JsonResponse(error)
    params = json.loads(request.body)
    Todo.objects.filter(pk=pk).update(
        title=params["title"],
        task=params["task"],)
    return JsonResponse(
        {"status": "update_succeed",
         "id": todo.id,
        "title": todo.title,
         "task": todo.task,
         "dead_time": todo.dead_time})

@csrf_exempt
@require_http_methods(["POST"])
def todo_delete(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return JsonResponse(error)
    id = todo.id
    title = todo.title
    todo.delete()
    return JsonResponse(
        {"status": "delete_succeed", "id": id, "title": title})


# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def todo_detail(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#     return JsonResponse(todo.to_dict())