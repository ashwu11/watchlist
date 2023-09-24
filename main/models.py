from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True) # SET_NULL if we want items to remain
    title = models.CharField(max_length = 150)
    type = models.CharField(max_length = 50)
    thoughts = models.TextField(null = True, blank = True)
    status = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(null = True, blank = True, max_length=20)

    # set default value to title
    def __str__(self):
        return self.title
    
    # order results based on status
    class Meta:
        ordering = ['status']