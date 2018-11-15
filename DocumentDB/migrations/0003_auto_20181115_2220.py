# Generated by Django 2.0.1 on 2018-11-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentDB', '0002_auto_20181113_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periodical',
            old_name='period',
            new_name='issue',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='source',
            new_name='journal',
        ),
        migrations.RenameField(
            model_name='periodical',
            old_name='pageof',
            new_name='pages',
        ),
        migrations.AddField(
            model_name='periodical',
            name='data',
            field=models.DateField(null=True, verbose_name='出版日期YYYY-MM-DD'),
        ),
        migrations.AddField(
            model_name='periodical',
            name='memo',
            field=models.CharField(default=12, max_length=10, verbose_name='总共几页'),
            preserve_default=False,
        ),
    ]
