from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import random
import string
# Create your models here.


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slugify(instance, slug):
    """
    checking if slug exist adding string to slug
    """
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug
        unique_slug += random_string_generator(size=4)
    return unique_slug


class Category(models.Model):
    title = models.CharField('category title ', max_length=40)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField('title', max_length=60)
    short_description = models.CharField('short description', max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    create_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wirter = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField('comment title')
    create_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.text[:10]} - {self.author} - {self.post}'
