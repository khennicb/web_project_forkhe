from django.contrib import admin

from .models import Chatroom
from .models import Message

admin.site.register(Chatroom)
admin.site.register(Message)

# Register your models here.
