from django.db import models

# Create your models here.
class Blog(models.Model):
    TAG = (
        ('Streetstlye','Streetstlye'),
        ('Craft','Craft'),
        ('Fashion','Fashion'),
        ('Denim','Denim'),
        ('Lifestyle','Lifestyle'),
    )
    CATEGORIES = (
        ('Fashion','Fashion'),
        ('Beauty','Beauty'),
        ('Streetstlye','Streetstlye'),
        ('Lifestyle','Lifestyle'),
        ('DIY&Craft','DIY&Craft'),
    )
    name = models.CharField(max_length=100, null=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=200,null=True,choices=TAG)
    categories = models.CharField(max_length=200, default="null" , null=True,choices=CATEGORIES)
    images1  = models.ImageField(default="null",null=True, blank=True)
    detail = models.CharField(max_length=1000,null=True)
    detail1 = models.CharField(max_length=10000,null=True)

    def __str__(self):
        return str(self.name)
    @property
    def imageURL(self):
        try:
            url = self.images1.url
        except:
            url = ''
        return url
