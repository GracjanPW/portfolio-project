from django.db import models

# Create your models here.
class Blog(models.Model):
    title= models.CharField(max_length=30)
    date= models.DateTimeField()
    text= models.TextField(max_length=200)
    image= models.ImageField(upload_to='images/')

    def summary(self):
        return self.text[:100]

    def date_format(self):
        return self.date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
