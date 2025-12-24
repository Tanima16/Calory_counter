from django.forms import ModelForm
from .models import *

class ProfileModelForm(ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['name', 'gender', 'age', 'height', 'weight']