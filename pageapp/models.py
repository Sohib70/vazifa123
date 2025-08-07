from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories')
    tag = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    on_top = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=100,blank=False)
    comment = models.TextField(verbose_name = "Comment")
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author

class Rating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='ratings')
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.value)