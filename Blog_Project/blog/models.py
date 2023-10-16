from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    #lớp được Django hỗ trợ sẵn và được sử dụng để định nghĩa các tùy chọn cho Model
    class Meta:
        ordering = ('-date_created',)

    def __str__(self) :
        return self.title
    
    
