from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self): # Python 2 还要定义 __unicode__
        return self.name


class Page(models.Model):
    category = models.ForeignKey(
        'rango.Category',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self): # Python 2 还要定义 __unicode__
        return self.title