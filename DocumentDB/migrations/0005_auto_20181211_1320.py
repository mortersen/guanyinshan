# Generated by Django 2.0.1 on 2018-12-11 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentDB', '0004_auto_20181115_2311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='degreethesis',
            options={'ordering': ['-UpdateTime'], 'verbose_name': '学位论文信息表', 'verbose_name_plural': '学位论文信息表'},
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='abstract',
            new_name='Abstract',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='path',
            new_name='FilePath',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='issue',
            new_name='Issue',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='keywords',
            new_name='Keywords',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='pages',
            new_name='Pages',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='publisher',
            new_name='Publisher',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='tertiaryauthor',
            new_name='TertiaryAuthor',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='caption',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='updatetime',
            new_name='UpdateTime',
        ),
        migrations.RenameField(
            model_name='degreethesis',
            old_name='volume',
            new_name='Volume',
        ),
        migrations.RemoveField(
            model_name='degreethesis',
            name='isc35n',
        ),
        migrations.RemoveField(
            model_name='degreethesis',
            name='year',
        ),
        migrations.AddField(
            model_name='degreethesis',
            name='Isc35n',
            field=models.BooleanField(default=False, verbose_name='是否与陈三五娘相关'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='degreethesis',
            name='URL',
            field=models.URLField(default=False, verbose_name='链接地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='degreethesis',
            name='Year',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, verbose_name='发表年份'),
            preserve_default=False,
        ),
    ]