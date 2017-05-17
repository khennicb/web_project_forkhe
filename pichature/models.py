from __future__ import unicode_literals

import datetime

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Chatroom(models.Model):
    name = models.CharField(max_length=200)
    chatroomUsers = models.ManyToManyField(User, related_name='chatroomUsers')
    chatroomAdmin = models.ManyToManyField(User, related_name='chatroomAdmin')
    
    def __str__(self):
        return self.name
    

#@python_2_unicode_compatible
#class ChatroomUser(models.Model):
#    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    
#    class Meta:
#        unique_together = ('chatroom', 'user')
#    
#@python_2_unicode_compatible
#class ChatroomAdmin(models.Model):
#    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    
#    class Meta:
#        unique_together = ('chatroom', 'user')


@python_2_unicode_compatible
class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    message_text = models.CharField(max_length=500)
    message_picture = models.CharField(max_length=5000, null=True, blank=True)
    
    def __str__(self):
        return self.message_text
    
# Create your models here.
