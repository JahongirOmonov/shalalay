from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from utils.models import BaseModel

User = get_user_model()





class Journal(BaseModel):
    image = models.ImageField(upload_to='journal/images/%Y/%m/%d/')
    file = models.FileField(upload_to='journal/files/%Y/%m/%d/',
                            validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])

    source_year = models.SmallIntegerField()
    source_number = models.SmallIntegerField()

    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return f'Journal({self.source_year}-{self.source_number})'

    def get_update_url(self):
        return reverse('journal:journal_update',
                       kwargs={
                           'id': self.pk
                       })

    def get_delete_url(self):
        return reverse('journal:journal_delete',
                       kwargs={
                           'id': self.pk
                       })


class Article(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True,
                            unique_for_date='created_at')

    content = RichTextField()
    views = models.IntegerField(default=0, editable=False)

    authors = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('journal:article_detail',
                       kwargs={
                           'slug': self.slug,
                           'id': self.pk
                       })

    def get_update_url(self):
        return reverse('journal:article_update',
                       kwargs={
                           'slug': self.slug,
                           'id': self.pk
                       })

    def get_delete_url(self):
        return reverse('journal:article_delete',
                       kwargs={
                           'slug': self.slug,
                           'id': self.pk
                       })


class Editorial(BaseModel):
    image = models.ImageField(upload_to='journal/images/%Y/%m/%d/', blank=True, null=True)
    content = RichTextField()
    objects = models.Manager()
    # class Meta:
    #     ordering = ['-created_at']
    #     indexes = [
    #         models.Index(fields=['-created_at']),
    #     ]

    def __str__(self):
        return self.content




    def get_absolute_url(self):
        return reverse('journal:editorial_list',)

    def get_update_url(self):
        return reverse('journal:editorial_update',
                       kwargs={
                           'id': self.pk
                       })

    def get_delete_url(self):
        return reverse('journal:editorial_delete',
                       kwargs={
                           'id': self.pk
                       })


class Post(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True,
                            unique_for_date='created_at')

    content = RichTextField()
    # image = models.ImageField(upload_to='image/%Y/%m/%d/',
    #                           blank=True, null=True)
    mediaImage = models.FileField(upload_to='media/%Y/%m/%d/',
                                  validators=[FileExtensionValidator(['mp4', 'avi', 'mpeg', 'webm', 'png', 'jpeg', 'jpg', ])],
                                  blank=True, null=True)
    file_extension = models.CharField(max_length=10, blank=True, null=True)

    views = models.IntegerField(default=0, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',
                               blank=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('journal:post_detail',
                       kwargs={
                           'slug': self.slug,
                           'id': self.pk
                       })

    def get_update_url(self):
        return reverse('journal:post_update',
                       kwargs={
                           'slug': self.slug,
                           'id': self.pk
                       })

    def get_delete_url(self):
        return reverse('journal:post_delete',
                       kwargs={
                           'slug': self.slug,
                           'id': self.pk
                       })


class Contact(BaseModel):
    message = models.TextField(blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL,
                               blank=True, null=True)
    is_read = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.is_read)


class About(BaseModel):
    content = RichTextField()

    journal_name = models.CharField(max_length=127)
    journal_image = models.ImageField(upload_to='journal/about/images/%Y/%m/%d/')

    author_description = RichTextField()
    author_image = models.ImageField(upload_to='journal/about/images/%Y/%m/%d/')

    objects = models.Manager()


class SendingArticle(BaseModel):
    content = RichTextField()

    objects = models.Manager()


class SocialMedia(BaseModel):

    class SocialMediaChoice(models.TextChoices):
        FACEBOOK = 'facebook',
        TWITTER = 'twitter'
        LINKEDIN = 'linkedin'
        YOUTUBE = 'youtube'
        TELEGRAM = 'telegram'
        WHATSAPP = 'whatsapp'
        INSTAGRAM = 'instagram'
        GITHUB = 'github'

    class ColorChoice(models.TextChoices):
        RED = 'red'
        GREEN = 'green'
        BLUE = 'blue'
        PURPLE = 'purple'
        BLACK = 'black'
        WHITE = 'white'

    title = models.CharField(max_length=31, choices=SocialMediaChoice.choices,
                             unique=True)
    color = models.CharField(max_length=31, choices=ColorChoice.choices)
    url = models.URLField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('journal:social_media_update',
                       kwargs={
                           'id': self.pk
                       })

    def get_delete_url(self):
        return reverse('journal:social_media_delete',
                       kwargs={
                           'id': self.pk
                       })




