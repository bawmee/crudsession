from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.TextField(max_length = 50, default='제목 없음')
    body = models.TextField(null = False)
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField('date publishde')

    def sum(self):
        return self.body[:15]