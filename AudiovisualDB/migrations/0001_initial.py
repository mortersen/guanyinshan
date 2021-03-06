# Generated by Django 2.0 on 2020-06-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeOf', models.CharField(choices=[('GY', '闽南歌谣'), ('GS', '闽南故事'), ('KL', '闽南顺口溜')], default='GY', max_length=2, verbose_name='音频分类')),
                ('Title', models.CharField(max_length=200, verbose_name='音频名称')),
                ('FilePath', models.FileField(upload_to='CON_PAPERS/%Y/%m', verbose_name='上传本地音频文件')),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '音频资源表',
                'verbose_name_plural': '音频资源表',
                'ordering': ['-UpdateTime'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeOf', models.CharField(choices=[('XQ', '戏曲'), ('TY', '闽南童谣')], default='XQ', max_length=2, verbose_name='视频分类')),
                ('Title', models.CharField(max_length=200, verbose_name='视频名称')),
                ('FilePath', models.FileField(upload_to='CON_PAPERS/%Y/%m', verbose_name='上传本地视频文件')),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '视频资源表',
                'verbose_name_plural': '视频资源表',
                'ordering': ['-UpdateTime'],
            },
        ),
    ]
