from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    body = RichTextUploadingField()

    # displays actual blog name in admin panel
    def __str__(self):
        return self.title

    def pub_date_short(self):
        return self.pub_date.strftime('%B %e, %Y')
