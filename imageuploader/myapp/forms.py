from email.mime import image
from socket import fromshare
from .models import Image
from django.forms import ModelForm
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo': ''}