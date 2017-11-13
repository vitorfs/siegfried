from django import forms


class UploadArticlesForm(forms.Form):
    spreadsheet = forms.FileField()
