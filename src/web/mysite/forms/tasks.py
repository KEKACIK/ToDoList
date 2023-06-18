from django import forms


class TaskCreateForm(forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField(max_length=512)
