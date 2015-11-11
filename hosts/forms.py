__author__ = 'zhailb'
from django.forms import ModelForm
from models import Host
from django import forms

class AddHostForm(ModelForm):
    hostname = forms.CharField(max_length=64,min_length=8)
    ip = forms.GenericIPAddressField()
    os = forms.CharField(max_length=64,min_length=1,required=False)
    type = forms.CharField(max_length=64,min_length=1,required=False)
    class Meta:
        model = Host
        fields = ['hostname', 'ip', 'os', 'type']
