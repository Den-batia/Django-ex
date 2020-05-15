from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
import time

# Create your models here.
def new_slug(s):
    new_s = slugify(s, allow_unicode=True)
    return new_s + '-' + str(int(time.time()))

class Man(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    text = models.TextField(max_length=200, default='None')
    slug = models.SlugField(max_length=50, default=None, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.slug = new_slug(self.text)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.slug

class AuthCode(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pk')
    auth_code = models.IntegerField()

    def __str__(self):
        return self.user.username



