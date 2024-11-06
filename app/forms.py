from django import forms
from app.models import *

class TopicModelform(forms.ModelForm):
   class Meta:
    model=Topic
    fields='__all__'

class WebpageModelform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['Topic_name','name','url']
        #exclude=['email']
        #labels={'Topic_name':'TN'}
        #widgets={'url':forms.PasswordInput}
        #help_texts={'Topic_name':'This is parent Column'}


class AccessrecordModelform(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields='__all__'

                

