from django.conf import settings
from django.db import models
from django.utils import timezone


class Plant(models.Model):
    name = models.CharField(max_length=200, null=False)
    period = models.DurationField(null=False)
    image = models.ImageField(upload_to='images/',
                              default='static/no-img.jpg',
                              null=False)
    pub_date = models.DateTimeField(default=timezone.now,
                                    null=False)
    instructions = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=False)

    def __str__(self):
        return self.name
