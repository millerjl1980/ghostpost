from django.forms import modelform_factory
from ghostpost.models import PostMessage

AddPostForm = modelform_factory(PostMessage, exclude=['up_vote', 'down_vote', 'sub_time', 'hidden_key'])