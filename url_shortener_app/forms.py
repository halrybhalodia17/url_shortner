from django import forms

class URLForm(forms.Form):
    longurl = forms.URLField(max_length=200)
    customname = forms.CharField(max_length=30, required = False)


class loginform(forms.Form):
    email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=30)