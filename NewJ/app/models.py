from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
import time

# Create your models here.
def new_slug(s):
    new_s = slugify(s, allow_unicode=True)
    return new_s + '-' + str(int(time.time()))

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Содержание', max_length=500)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        print(args, kwargs)
        if not self.id:
            self.slug = new_slug(self.text)
        # super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

class AuthCode(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auth_code = models.IntegerField()

    def __str__(self):
        return self.user.username



