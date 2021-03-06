# Generated by Django 2.0.1 on 2018-12-12 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentDB', '0007_auto_20181211_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodical',
            options={'ordering': ['-UpdateTime'], 'verbose_name': '期刊数据表', 'verbose_name_plural': '期刊数据表'},
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='abstract',
            new_name='Abstract',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='organization',
            new_name='AuthorAffiliation',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='data',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='path',
            new_name='FilePath',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='isc35n',
            new_name='Isc35n',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='issue',
            new_name='Issue',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='journal',
            new_name='Journal',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='keywords',
            new_name='Keywords',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='memo',
            new_name='Memo',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='pages',
            new_name='Pages',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='caption',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='updatetime',
            new_name='UpdateTime',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='year',
            new_name='Year',
        ),
        migrations.RemoveField(
            model_name='periodical',
            name='type',
        ),
        migrations.AddField(
            model_name='periodical',
            name='TypeOf',
            field=models.CharField(choices=[('MC', '民间传说'), ('MG', '民间歌谣'), ('MS', '民间故事'), ('XQ', '戏曲'), ('MY', '民间谚语'), ('MM', '民间谜语'), ('QT', '其他')], default='QT', max_length=2, verbose_name='期刊分类'),
        ),
        migrations.AddField(
            model_name='periodical',
            name='URL',
            field=models.URLField(default=django.utils.timezone.now, verbose_name='链接地址'),
            preserve_default=False,
        ),
    ]
