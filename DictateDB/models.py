from django.db import models

# Create your models here.

class OperaText(models.Model):#戏曲数据模型

    Title = models.CharField(max_length=200,verbose_name='题名')
    Abstract = models.TextField(verbose_name='简介')
    From = models.CharField(max_length=200,verbose_name='资源来源')
    Memo = models.CharField(max_length=20,verbose_name='页数')
    Author = models.CharField(max_length=50,verbose_name='作者')
    FilePath = models.FileField(upload_to='OPERATEXT/%Y/%m', verbose_name='上传本地戏曲文本文件')
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '戏曲文本资料表'
        verbose_name = "戏曲文本资料表"


class FolkSong(models.Model):#歌谣数据模型
    Title = models.CharField(max_length=200, verbose_name='题名')
    From = models.CharField(max_length=200, verbose_name='资源来源')
    Memo = models.CharField(max_length=20, verbose_name='页数')
    Author = models.CharField(max_length=50, verbose_name='作者')
    FilePath = models.FileField(upload_to='FOLKSONG/%Y/%m', verbose_name='上传本地歌谣文本文件')
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '歌谣文本资料表'
        verbose_name = "歌谣文本资料表"


class SongBook(models.Model):#歌册数据模型
    Title = models.CharField(max_length=200, verbose_name='题名')
    Abstract = models.TextField(verbose_name='简介')
    From = models.CharField(max_length=200, verbose_name='资源来源')
    Memo = models.CharField(max_length=20, verbose_name='页数')
    Author = models.CharField(max_length=50, verbose_name='作者')
    FilePath = models.FileField(upload_to='SONGBOOK/%Y/%m', verbose_name='上传本地歌册文件')
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '歌册资料表'
        verbose_name = "歌册资料表"


class SouthernMusic(models.Model):#南音曲谱数据模型
    Title = models.CharField(max_length=200, verbose_name='题名')
    From = models.CharField(max_length=200, verbose_name='资源来源')
    Memo = models.CharField(max_length=20, verbose_name='页数')
    Author = models.CharField(max_length=50, verbose_name='作者')
    FilePath = models.FileField(upload_to='SOUTHERNMUSIC/%Y/%m', verbose_name='上传本地南音曲谱文件')
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '南音曲谱资料表'
        verbose_name = "南音曲谱资料表"
