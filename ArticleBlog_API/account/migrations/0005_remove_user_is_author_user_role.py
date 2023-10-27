# Generated by Django 4.2.6 on 2023-10-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_author',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('reader', 'Reader'), ('author', 'Author')], default='author', max_length=20),
            preserve_default=False,
        ),
    ]