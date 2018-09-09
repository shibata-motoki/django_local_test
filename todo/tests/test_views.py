import os

from django.test import TestCase
from django.urls import reverse

from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_local_test.mysite.settings'
import django
print(settings.INSTALLED_APPS)
django.setup()

from django_local_test.todo.models import Todo

class TestTodo(TestCase):
    def test_get(self):
        Todo.objects.create(title="テスト1", task="test1")
        Todo.objects.create(title="テスト2", task="test2")
        res = self.client.get(reverse('todo:todo_list'))
        self.assertTemplateUsed(res, 'todo/todo_list.html')
        self.assertContains(res, 'テスト1')
        self.assertContains(res, 'test1')
        self.assertContains(res, 'テスト2')
        self.assertContains(res, 'test2')
