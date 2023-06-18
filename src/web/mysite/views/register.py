from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from mysite.forms.register import RegisterForm


class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': RegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save_and_telegram()
            login(self.request, user)
            messages.success(request, 'Регистрация прошла успешна')
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
