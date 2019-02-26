from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # displays actual blog name in admin panel
    def __str__(self):
        return self.title

    # function returns first 110 characters of a blog summary; i.e preview
    def body_summary(self):
        return self.body[:110]

    def pub_date_short(self):
        return self.pub_date.strftime('%B %e, %Y')
