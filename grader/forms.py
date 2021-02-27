from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class sample_form(forms.ModelForm):

    class Meta:
        model = sample_answer
        fields = ['sample']

class answer_form(forms.ModelForm):

    class Meta:
        model = student_answer
        fields = ['answer']