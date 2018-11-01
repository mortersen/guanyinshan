# Generated by Django 2.0.1 on 2018-11-01 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(verbose_name='正文内容')),
                ('author', models.CharField(max_length=100, verbose_name='作者（转载处）')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='创建或刚更新时间')),
            ],
            options={
                'verbose_name': '新闻资讯',
                'verbose_name_plural': '新闻资讯',
            },
        ),
        migrations.CreateModel(
            name='R_Information_Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='图片名称')),
                ('path', models.ImageField(upload_to='PICS/%Y/%m/%d', verbose_name='上传本地图片')),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.Information', verbose_name='关联的新闻')),
            ],
            options={
                'verbose_name': '新闻图片',
                'verbose_name_plural': '新闻图片',
            },
        ),
    ]
