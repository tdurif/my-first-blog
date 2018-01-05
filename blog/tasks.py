from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User

@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
    me = User.objects.get(username='admin')
    total = x * (y * random.randint(3, 100))
    Post.objects.create(author=me, title='Sample title', text=total, published_date=timezone.now())
    return total

@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)
