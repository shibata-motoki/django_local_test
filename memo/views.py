from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

from .models import Memo
from .forms import MemoForm

def index(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MemoForm()
    return TemplateResponse(request, 'memo/index.html', {'form': form})

def memo_list(request):
    memo_list = Memo.objects.order_by('created_at')[:5]
    return TemplateResponse(request, 'memo/memo_list.html', {'memo_list': memo_list})

def memo_edit(request, pk):
    try:
        memo = Memo.objects.get(id=pk)
    except Memo.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MemoForm()
    return TemplateResponse(request, 'memo/index.html', {'form': form, 'memo': memo})

def memo_del(request, pk):
    try:
        memo = Memo.objects.get(id=pk)
    except Memo.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        memo.delete()
        return HttpResponseRedirect(reverse('memo_list'))
    return TemplateResponse(request, 'memo/memo_delete.html',
                               {'memo': memo})


def memo_detail(request, pk):
    try:
        memo = Memo.objects.get(pk=pk)
    except Memo.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'memo/memo_detail.html', {'memo': memo})