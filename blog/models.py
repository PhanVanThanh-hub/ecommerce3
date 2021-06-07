from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
def create_slug(title):  # new
    slug = slugify(title)
    qs = Blog.objects.filter(slug=slug)
    if qs:
        exists = qs.exists()
        if exists:
            slug = "%s-%s" % (slug, qs.first().id)
    return slug
class Category(models.Model):
   
    name = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=2000)
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
class Blog(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images1  = models.ImageField(default="null",null=True, blank=True)
    detail = models.CharField(max_length=1000,null=True)
    detail1 = models.CharField(max_length=10000,null=True)
    slug = models.SlugField(max_length=2000)


    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = create_slug(self.name)
        return super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name)
    @property
    def imageURL(self):
        try:
            url = self.images1.url
        except:
            url = ''
        return url
