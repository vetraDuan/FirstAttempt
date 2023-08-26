from django.db import models


# Create your models here.


class Questions(models.Model):
    """
    包含一个问题和一个发布日期
    """
    question_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    """
    包含一个文本描述和一个投票数
    另外 添加外键到Questions。
    """
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
