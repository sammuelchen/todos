from django.db import models


# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)  # 标题
    description = models.TextField(blank=True)  # 描述
    completed = models.BooleanField(default=False)  # 完成状态
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at'] # 按创建时间降序排列
