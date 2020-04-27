import markdown
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
from django.utils.html import strip_tags


# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='文章分类')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签分类'
        verbose_name_plural = verbose_name


# 文章
class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name='标题')
    body = models.TextField(verbose_name='正文')
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
    created_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='修改时间')
    excerpt = models.CharField(max_length=100, blank=True, verbose_name='文章摘要')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章分类')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        verbose_name = '发布管理'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    # 截取文章正文前面54个字符为文章摘要
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


# Banner图
class Banner(models.Model):
    title = models.CharField(max_length=70, verbose_name='标题')
    description = models.TextField(verbose_name='Banner图文本信息')
    banner = models.ImageField(upload_to='banner/%Y%m%d/', blank=True)
    created_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    class Meta:
        verbose_name = 'Banner图管理'
        verbose_name_plural = verbose_name


# 心灵鸡汤
class ChickenSoup(models.Model):
    description = models.TextField(verbose_name='心灵鸡汤文字描述')

    class Meta:
        verbose_name = '鸡汤'
        verbose_name_plural = verbose_name


# 关于我
class AboutMe(models.Model):
    description = models.TextField(verbose_name='我的信息')

    class Meta:
        verbose_name = '关于我'
        verbose_name_plural = verbose_name
