from django import forms
from django.conf import settings

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        input_formats=settings.DATETIME_INPUT_FORMATS,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
