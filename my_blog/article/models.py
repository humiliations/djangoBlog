from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# timezone用于处理时间相关事务
from django.utils import timezone


# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者，参数on_delete用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题
    title = models.CharField(max_length=100)
    # 文章正文,textField用于保存大量文本
    body = models.TextField()
    # 文章创建时间,创建数据时默认写入当前时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间，每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # 表示数据应以创建时间倒序排列
        ordering = ('-created',)

    def __str__(self):
        return self.title
