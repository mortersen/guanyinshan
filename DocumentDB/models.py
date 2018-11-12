from django.db import models

# Create your models here.

#创建期刊表
class Periodical(models.Model):
    author = models.CharField(max_length=100,verbose_name='作者')
    caption = models.CharField(max_length=200,verbose_name='题名')
    source = models.CharField(max_length=200,verbose_name='来自何期刊')
    year = models.CharField(max_length=10,verbose_name="出版年份")
    period = models.CharField(max_length=10,verbose_name='第几期出版')
    pageof = models.CharField(max_length=10,verbose_name='哪几页刊载')
    keywords = models.CharField(max_length=100,verbose_name='关键词')
    organization = models.CharField(max_length=50,verbose_name='作者所属机构')
    abstract = models.TextField(verbose_name='内容摘要')
    path = models.FileField(upload_to='PERIODICALS/%Y/%m',verbose_name='上传本地期刊文件')
    updatatime = models.DateTimeField(auto_now=True)
    isc35n = models.BooleanField(verbose_name='与陈三五娘有关')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "期刊数据表"
        verbose_name_plural = '期刊数据表'


#创建学位论文表
class DegreeThesis(models.Model):
    datatype = models.PositiveIntegerField(verbose_name='类型')
    caption = models.CharField(max_length=200,verbose_name='论文题目')
    author = models.CharField(max_length=100,verbose_name="论文作者")
    source = models.CharField(max_length=200,verbose_name="期刊名称")
    year = models.CharField(max_length=10,verbose_name='哪年出版的')
    pubtime = models.DateTimeField(verbose_name='出版时间')
    keywords = models.CharField(max_length=100,verbose_name='关键词')
    abstract =models.TextField(verbose_name='内容摘要')
    srcdatabase = models.CharField(max_length=50,verbose_name='来源数据库')
    updatatime = models.DateTimeField(auto_now=True)
    path = models.FileField(upload_to='DEGREETHESIS/%Y/%m',verbose_name='上传本地学位论文文件')
    dataformat = models.CharField(max_length=20,verbose_name='数据格式，默认PDF')
    isc35n = models.BooleanField(verbose_name='与陈三五娘有关')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "学位论文信息表"
        verbose_name = "学位论文信息表"

#创建报纸表
class Newspaper(models.Model):
    title = models.CharField(max_length=200,verbose_name='标题名')
    secondarytitle = models.CharField(max_length=100,verbose_name='报刊名称')
    pubdate = models.DateField(verbose_name='出版日期')
    edition = models.CharField(max_length=20,verbose_name='第几版次')
    page = models.CharField(max_length=10,verbose_name='哪几页面刊载')
    abstract = models.TextField(verbose_name='内容摘要')
    path = models.FileField(upload_to='NEWSPAPER/%Y/%m',verbose_name='上传本地报纸文件')
    updatatime = models.DateTimeField(auto_now=True)
    dataformat = models.CharField(max_length=20,verbose_name="数据格式，默认PDF")
    isc35n = models.BooleanField(verbose_name='是否与陈三五娘有关')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "报纸信息表"
        verbose_name_plural = "报纸信息表"


#创建图书资源表
class Books(models.Model):
    title = models.CharField(max_length=100,verbose_name="书名")
    author = models.CharField(max_length=50,verbose_name='创作者或作者')
    keywords = models.CharField(max_length=100,verbose_name='关键词')
    abstract = models.TextField(verbose_name='内容那个摘要')
    createdate = models.DateField(verbose_name='创作日期')
    dataformat = models.CharField(max_length=20,verbose_name='数据格式，默认PDF')
    source = models.CharField(max_length=50,verbose_name='图书来源')
    path = models.FileField(upload_to='BOOKS/%Y/%m',verbose_name='上传本地图书文件')
    updatatime = models.DateTimeField(auto_now=True)
    bak = models.CharField(max_length=200,verbose_name='备注信息')
    isc35n = models.BooleanField(verbose_name='是否与陈三五娘有关')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '图书信息表'
        verbose_name = "图书信息表"

#创建其他文献资源表
class OtherDocument(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题或名称')
    author = models.CharField(max_length=100,verbose_name='作者或转载处')
    abstract = models.TextField(verbose_name='内容介绍')
    createdate = models.DateField(verbose_name='收录整理日期')
    dataformat = models.CharField(max_length=30,verbose_name='数据格式,默认PDF')
    source = models.CharField(max_length=50,verbose_name='文献来源')
    path = models.FileField(upload_to='OTHERDOCUMENT/%Y/%m',verbose_name='上传本地文献，默认PDF')
    updatetime =models.DateTimeField(auto_now=True)
    bak = models.CharField(max_length=200,verbose_name="备注信息")
    isc35n = models.BooleanField(verbose_name='是否与陈三五娘有关')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '其他文献资源信息表'
        verbose_name_plural = '其他文献资源信息表'