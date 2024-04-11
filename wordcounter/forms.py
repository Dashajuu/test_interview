from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class WordCountForm(forms.Form):
    word = forms.CharField()