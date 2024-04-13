import datetime

from django.db import models
from django.utils import timezone


# Create your models here.


class Questions(models.Model):
    """
    包含一个问题和一个发布日期
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # 是否当前发布的问卷

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """
    包含一个文本描述和一个投票数
    另外 添加外键到Questions。
    """
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
