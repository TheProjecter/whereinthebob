from django.contrib.comments.forms import CommentSecurityForm
from django import forms
from django.contrib.comments.forms import CommentForm
from django.utils.encoding import force_unicode
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

import datetime

class myCommentForm(CommentForm):
	"""
	A lighter comment form.
	"""
	def get_comment_create_data(self):
		return dict(
			content_type = ContentType.objects.get_for_model(self.target_object),
			object_pk    = force_unicode(self.target_object._get_pk_val()),
			comment      = self.cleaned_data["comment"],
			submit_date  = datetime.datetime.now(),
			site_id      = settings.SITE_ID,
			is_public    = True,
			is_removed   = False,
		)
    
myCommentForm.base_fields.pop('email')
myCommentForm.base_fields.pop('url')
myCommentForm.base_fields.pop('name')
