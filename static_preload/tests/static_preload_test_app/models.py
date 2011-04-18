from django.db import models

class Thingie(models.Model):
    content = models.CharField(max_length=50)
    expires = models.DateTimeField(null=True)
