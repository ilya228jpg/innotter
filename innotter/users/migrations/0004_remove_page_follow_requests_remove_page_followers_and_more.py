# Generated by Django 4.0.6 on 2022-07-22 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220720_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='follow_requests',
        ),
        migrations.RemoveField(
            model_name='page',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='page',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='post',
            name='page',
        ),
        migrations.RemoveField(
            model_name='post',
            name='reply_to',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]