# Generated by Django 3.2.3 on 2021-09-02 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0014_auto_20210901_1220'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='username',
            field=models.CharField(default=20, max_length=30),
            preserve_default=False,
        ),
    ]