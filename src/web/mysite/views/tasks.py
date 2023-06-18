from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from admin_web.models import Task
from mysite.forms import TaskCreateForm


class TaskCreateView(View):
    template_name = 'mysite/index.html'

    def post(self, request):
        form = TaskCreateForm(request.POST)

        if form.is_valid():
            Task(
                user=request.user, title=form.cleaned_data["title"], description=form.cleaned_data["description"]
            ).save()
            messages.success(request, 'Новая запись добавлена успешно!')
            return redirect('index')
        context = {'form': form}
        return redirect(request, self.template_name, context)


class TaskCompleteView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.close = True
        task.save()
        return redirect('index')


class TaskBackView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.close = False
        task.save()
        return redirect('index')


class TaskDeleteView(View):
    def get(self, request, task_id):
        Task.objects.get(id=task_id).delete()
        return redirect('index')
