from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import NotificationSerializer
from django.contrib.auth.models import User

class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    message = models.TextField()
    user = models.ForeignKey(User)
    
