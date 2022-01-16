# basic_api/models.py
from django.db import models

# list
Grade = [
    ('excellent', 1),
    ('average', 0),
    ('bad', -1)
]


# DataFlair
class DRFPost(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/%Y/%m/%d")

    uploaded = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return self.name
