# Generated by Django 2.1.7 on 2019-04-29 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_globalsettings_logo_sub_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='addthis_pubid',
            field=models.CharField(blank=True, default='5bbcb76243b82dd4', help_text='This is the string that is AFTER `#pubid=`. Ex: ra-5bbcb76243b82dd4', max_length=25, null=True, verbose_name='AddThis PubId'),
        ),
    ]