from django import forms
from .models import Suggestion

class suggestionFormForm(forms.ModelForm):

    class Meta:
        model = Suggestion
        fields = ('sug_name', 'body_text')