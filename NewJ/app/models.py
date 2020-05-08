from django.db import models
import time

# Create your models here.
class Man(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    slug = models.SlugField(max_length=50, default=None, unique=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = self.slug + '-' + str(round(time.time()))
        print(self.slug)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.slug



