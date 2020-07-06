# Generated by Django 2.1.2 on 2020-06-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FolkSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='题名')),
                ('From', models.CharField(max_length=200, verbose_name='资源来源')),
                ('Memo', models.CharField(max_length=20, verbose_name='页数')),
                ('Author', models.CharField(max_length=50, verbose_name='作者')),
                ('FilePath', models.FileField(upload_to='CON_PAPERS/%Y/%m', verbose_name='上传本地歌谣文本文件')),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '歌谣文本资料表',
                'verbose_name_plural': '歌谣文本资料表',
                'ordering': ['-UpdateTime'],
            },
        ),
        migrations.CreateModel(
            name='OperaText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='题名')),
                ('Abstract', models.TextField(verbose_name='简介')),
                ('From', models.CharField(max_length=200, verbose_name='资源来源')),
                ('Memo', models.CharField(max_length=20, verbose_name='页数')),
                ('Author', models.CharField(max_length=50, verbose_name='作者')),
                ('FilePath', models.FileField(upload_to='CON_PAPERS/%Y/%m', verbose_name='上传本地戏曲文本文件')),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '戏曲文本资料表',
                'verbose_name_plural': '戏曲文本资料表',
                'ordering': ['-UpdateTime'],
            },
        ),
        migrations.CreateModel(
            name='SongBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='题名')),
                ('Abstract', models.TextField(verbose_name='简介')),
                ('From', models.CharField(max_length=200, verbose_name='资源来源')),
                ('Memo', models.CharField(max_length=20, verbose_name='页数')),
                ('Author', models.CharField(max_length=50, verbose_name='作者')),
                ('FilePath', models.FileField(upload_to='CON_PAPERS/%Y/%m', verbose_name='上传本地歌册文件')),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '歌册资料表',
                'verbose_name_plural': '歌册资料表',
                'ordering': ['-UpdateTime'],
            },
        ),
        migrations.CreateModel(
            name='SouthernMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='题名')),
                ('From', models.CharField(max_length=200, verbose_name='资源来源')),
                ('Memo', models.CharField(max_length=20, verbose_name='页数')),
                ('Author', models.CharField(max_length=50, verbose_name='作者')),
                ('FilePath', models.FileField(upload_to='CON_PAPERS/%Y/%m', verbose_name='上传本地南音曲谱文件')),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '南音曲谱资料表',
                'verbose_name_plural': '南音曲谱资料表',
                'ordering': ['-UpdateTime'],
            },
        ),
    ]