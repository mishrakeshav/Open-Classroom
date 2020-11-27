from django import forms

class CommentCreateForm(forms.Form):
    comment_text = forms.CharField(max_length=250)

class PrivateCommentForm(forms.Form):
    comment_text = forms.CharField(max_length=250)
