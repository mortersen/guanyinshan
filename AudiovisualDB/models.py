from django.db import models

# Create your models here.

class Video(models.Model):#视频数据模型

    TYPE_CHOICE = \
        (
            ('XQ', '戏曲'),
            ('TY', '闽南童谣'),

        )
    TypeOf = models.CharField(max_length=2, choices=TYPE_CHOICE, default='XQ', verbose_name='视频分类')
    Title = models.CharField(max_length=200,verbose_name='视频名称')
    FilePath = models.FileField(upload_to='VIDEO/%Y/%m', verbose_name='上传本地视频文件')
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '视频资源表'
        verbose_name = "视频资源表"


class Audio(models.Model):#音频数据模型
    TYPE_CHOICE = \
        (
            ('GY', '闽南歌谣'),
            ('GS', '闽南故事'),
            ('KL','闽南顺口溜'),
        )
    TypeOf = models.CharField(max_length=2, choices=TYPE_CHOICE, default='GY', verbose_name='音频分类')
    Title = models.CharField(max_length=200,verbose_name='音频名称')
    FilePath = models.FileField(upload_to='AUDIO/%Y/%m', verbose_name='上传本地音频文件')
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '音频资源表'
        verbose_name = "音频资源表"
