from django.db import models

# Create your models here.
class BoardDB(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    context = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)
    good_count = models.IntegerField(default=0)
    bad_count = models.IntegerField(default=0)

