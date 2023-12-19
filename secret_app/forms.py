from django import forms

from .models import QuestionModel, CommentModel


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = ['username', 'question', 'hashtag']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['commit']
