# Generated by Django 4.1.2 on 2022-10-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_artist_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ('name',), 'verbose_name': 'Artist', 'verbose_name_plural': 'Artists'},
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Artists or Band name'),
        ),
        migrations.AddIndex(
            model_name='artist',
            index=models.Index(fields=['name'], name='music_artis_name_e97718_idx'),
        ),
    ]