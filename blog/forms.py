from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','age','body']

        labels={
            'name':'Name',
            'email':'Email Id',
            'age':'Age',
            'body':'Message'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }