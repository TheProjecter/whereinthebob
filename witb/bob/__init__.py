from django.contrib.comments.models import Comment

from bob.forms import myCommentForm

def get_model():
    return Comment

def get_form():
    return myCommentForm
