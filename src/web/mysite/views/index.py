from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from admin_web.models import Task


@login_required(login_url='/login/')
def indexView(request):
    user = request.user
    tasks = Task.objects.filter(user=user).all()
    context = {
        "tasks": tasks
    }
    return render(request, 'mysite/../../templates/mysite/index.html', context)
