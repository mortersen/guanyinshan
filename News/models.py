from django.db import models

# Create your models here.

class Information(models.Model):
    caption = models.CharField(max_length=100,verbose_name='标题')
    content = models.TextField(verbose_name='正文内容')
    author = models.CharField(max_length=100,verbose_name='作者（转载处）')
    updatetime = models.DateTimeField(auto_now=True,verbose_name='创建或刚更新时间')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "图片关联信息"
        verbose_name_plural = "图片关联信息"

class R_Information_Photo(models.Model):
    information = models.ForeignKey(Information,on_delete=models.CASCADE,verbose_name='关联的图片')
    name = models.CharField(max_length=100,verbose_name='图片名称')
    path = models.ImageField(upload_to='PICS/%Y/%m/%d',verbose_name="上传本地图片")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "图片"
        verbose_name_plural = "图片"