# Generated by Django 2.0.1 on 2018-11-13 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-updatetime'], 'verbose_name': '图书信息表', 'verbose_name_plural': '图书信息表'},
        ),
        migrations.AlterModelOptions(
            name='degreethesis',
            options={'ordering': ['-updatetime'], 'verbose_name': '学位论文信息表', 'verbose_name_plural': '学位论文信息表'},
        ),
        migrations.AlterModelOptions(
            name='newspaper',
            options={'ordering': ['-updatetime'], 'verbose_name': '报纸信息表', 'verbose_name_plural': '报纸信息表'},
        ),
        migrations.AlterModelOptions(
            name='otherdocument',
            options={'ordering': ['-updatetime'], 'verbose_name': '其他文献资源信息表', 'verbose_name_plural': '其他文献资源信息表'},
        ),
        migrations.AlterModelOptions(
            name='periodical',
            options={'ordering': ['-updatetime'], 'verbose_name': '期刊数据表', 'verbose_name_plural': '期刊数据表'},
        ),
        migrations.RenameField(
            model_name='books',
            old_name='updatatime',
            new_name='updatetime',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='updatatime',
            new_name='updatetime',
        ),
        migrations.RenameField(
            model_name='newspaper',
            old_name='updatatime',
            new_name='updatetime',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='updatatime',
            new_name='updatetime',
        ),
    ]
