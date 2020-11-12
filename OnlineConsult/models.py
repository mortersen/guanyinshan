from django.db import models

# Create your models here.
class Consult(models.Model):#留言数据模型

    Title = models.CharField(max_length=200,verbose_name='标题')
    Context = models.TextField(verbose_name='留言内容')
    Contact = models.CharField(max_length=100,verbose_name='联系方式')
    UpdateTime = models.DateTimeField(auto_now=True,verbose_name='留言时间')

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '留言板'
        verbose_name = "留言板"