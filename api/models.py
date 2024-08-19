from django.db import models
from .helpers import StatusChoice




class Services(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.URLField(max_length=500)
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.title


class Busines(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.URLField(max_length=500)
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.title



class Users(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.URLField(max_length=500)
    level = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.first_name


class Clients(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.URLField(max_length=500)
    definition = models.TextField(null=True)
    level = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.first_name

class Comments(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    comment = models.TextField()
    image = models.URLField(null=True,max_length=1000)
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.comment


class FAQs(models.Model):
    question = models.TextField()
    answer = models.TextField()
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.question
