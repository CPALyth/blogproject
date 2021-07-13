from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    '''分类专栏'''
    name = models.CharField(max_length=50)


class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=50)


class Article(models.Model):
    '''文章'''
    title = models.CharField(max_length=70)
    body = models.TextField()

    # 创建时间 和 最后修改时间
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 摘要, 可以没有文章摘要
    abstrct = models.CharField(max_length=200, blank=True)

    # 分类 和 标签
    # 一篇文章只能对应一个分类，但是一个分类下可以有多篇文章, 一对多用ForeignKey
    # 一篇文章可以有多个标签，同一个标签下也可能有多篇文章, 多对多用
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
