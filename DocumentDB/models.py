from django.db import models

# Create your models here.

#创建期刊表
class Periodical(models.Model):
    TYPE_CHOICE = \
        (
            ('MC','民间传说'),
            ('MG','民间歌谣'),
            ('MS','民间故事'),
            ('XQ','戏曲'),
            ('YM','民间谚语（谜语）'),
            ('QT','其他'),
        )
    TypeOf = models.CharField(max_length=2,choices=TYPE_CHOICE,default='QT',verbose_name='期刊分类')
    Author = models.CharField(max_length=100,verbose_name='作者')
    Title = models.CharField(max_length=200,verbose_name='文章标题')
    #URL = models.URLField(verbose_name='链接地址')
    Journal = models.CharField(max_length=200,verbose_name='期刊名称')
    Year = models.CharField(max_length=10,verbose_name="出版年份")
    #Date = models.DateField(null=True,verbose_name='出版日期YYYY-MM-DD')
    Volume = models.CharField(max_length=10,verbose_name='第几卷')
    Issue = models.CharField(max_length=10,verbose_name='第几期')
    Pages = models.CharField(max_length=10,verbose_name='哪几页刊载')
    Memo = models.CharField(max_length=10,verbose_name='总共几页')
    Keywords = models.CharField(max_length=100,verbose_name='关键词')
    AuthorAffiliation = models.CharField(max_length=50,verbose_name='作者所属机构')
    Abstract = models.TextField(verbose_name='内容摘要')
    FilePath = models.FileField(upload_to='PERIODICALS/%Y/%m',verbose_name='上传本地期刊文件')
    UpdateTime = models.DateTimeField(auto_now=True)
    #Isc35n = models.BooleanField(verbose_name='与陈三五娘有关')

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name = "期刊数据表"
        verbose_name_plural = '期刊数据表'


#创建学位论文表
class Dissertation(models.Model):
    TYPE_CHOICE = \
        (
            ('MC', '民间传说'),
            ('MG', '民间歌谣'),
            ('MS', '民间故事'),
            ('XQ', '戏曲'),
            ('YM', '民间谚语（谜语）'),
            ('QT', '其他'),
        )
    TypeOf = models.CharField(max_length=2, choices=TYPE_CHOICE, default='QT', verbose_name='论文分类')
    #datatype = models.PositiveIntegerField(verbose_name='类型')
    Title = models.CharField(max_length=200,verbose_name='论文题目')
    Author = models.CharField(max_length=50,verbose_name="论文作者")
    TertiaryAuthor = models.CharField(max_length=50,verbose_name='指导教师')
    Publisher = models.CharField(max_length=50,verbose_name="发表单位")
    Year = models.CharField(max_length=10,verbose_name='发表年份')
    Volume = models.CharField(max_length=10,verbose_name="学位层次")
    Pages = models.CharField(max_length=10,verbose_name='在哪几页')
    Memo = models.CharField(max_length=10,verbose_name='共有几页')
    #Issue = models.CharField(max_length=10,verbose_name='期')
    #pubtime = models.DateTimeField(verbose_name='出版时间')
    Keywords = models.CharField(max_length=100,verbose_name='关键词')
    Abstract =models.TextField(verbose_name='内容摘要')
    #srcdatabase = models.CharField(max_length=50,verbose_name='来源数据库')
    UpdateTime = models.DateTimeField(auto_now=True)
    FilePath = models.FileField(upload_to='DEGREETHESIS/%Y/%m',verbose_name='上传本地学位论文文件')
    #dataformat = models.CharField(max_length=20,verbose_name='数据格式，默认PDF')
    #URL = models.URLField(verbose_name='链接地址')
    #Isc35n = models.BooleanField(default=False,verbose_name='是否与陈三五娘相关')

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = "学位论文信息表"
        verbose_name = "学位论文信息表"


#创建图书资源表
class Books(models.Model):
    Title = models.CharField(max_length=100,verbose_name="书名")
    Author = models.CharField(max_length=50,verbose_name='创作者或作者')
    Year = models.CharField(max_length=10,verbose_name='出版年份')
    Series = models.CharField(max_length=100,verbose_name='丛书名')
    Publisher = models.CharField(max_length=50,verbose_name='出版社')
    Keywords = models.CharField(max_length=100,verbose_name='关键词')
    Abstract = models.TextField(verbose_name='内容摘要')
    #createdate = models.DateField(verbose_name='创作日期')
    #dataformat = models.CharField(max_length=20,verbose_name='数据格式，默认PDF')
    #source = models.CharField(max_length=50,verbose_name='图书来源')
    FilePath = models.FileField(upload_to='BOOKS/%Y/%m',verbose_name='上传本地图书文件')
    Memo = models.CharField(max_length=10, verbose_name='共有几页')
    UpdateTime = models.DateTimeField(auto_now=True)
    #bak = models.CharField(max_length=200,verbose_name='备注信息')
    #isc35n = models.BooleanField(verbose_name='是否与陈三五娘有关')
    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '图书信息表'
        verbose_name = "图书信息表"

#创建会议论文资源表
class ConferencePapers(models.Model):

    Title = models.CharField(max_length=200,verbose_name='论文标题')
    Author = models.CharField(max_length=50,verbose_name='论文作者')
    Year = models.CharField(max_length=10, verbose_name='发表年份')
    SecondaryTitle = models.CharField(max_length=200,verbose_name='会议名称')
    Publisher = models.CharField(max_length=50, verbose_name='出版社')
    Keywords = models.CharField(max_length=100, verbose_name='关键词')
    Abstract = models.TextField(verbose_name='内容摘要')
    FilePath = models.FileField(upload_to='CON_PAPERS/%Y/%m', verbose_name='上传本地会议论文文件')
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-UpdateTime']
        verbose_name_plural = '会议论文信息表'
        verbose_name = "会议论文信息表"
