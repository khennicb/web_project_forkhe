from __future__ import unicode_literals

import datetime

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Chatroom(models.Model):
    name = models.CharField(max_length=200)
    label = models.SlugField(unique=True, default='main')
    chatroomUsers = models.ManyToManyField(User, related_name='chatroomUsers')
    chatroomAdmin = models.ManyToManyField(User, related_name='chatroomAdmin')
    
    def __str__(self):
        return self.label
    
#    def get_main(self):
#        return self.get(label='main')


@python_2_unicode_compatible
class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    message_text = models.TextField()
    message_picture = models.TextField(null=True, blank=True)
    
    def message_picture_as_list(self):
        return self.message_picture.split(' ')
    
    def __str__(self):
        return '[{timestamp}] {user}: {message_picture}'.format(**self.as_dict())
        #return self.message_text
        
    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')
        
    def as_dict(self):
        return {'user': self.user, 'message_picture': self.message_picture, 'timestamp': self.formatted_timestamp}
    
