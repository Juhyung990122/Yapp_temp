from django.db import models

class Planet(models.Model):
    #DB교체하면서 필드값 옵션 변경
    uidList = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()