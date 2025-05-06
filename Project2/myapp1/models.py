from django.db import models
from django.utils import timezone

# Create your models here.


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('BL', 'Black Tea'),
        ('GR', 'Green Tea'),
        ('WT', 'White Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="myapp1/")
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)



    def __str__(self):
        return super().__str__()