# Generated by Django 2.2.16 on 2022-12-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20221213_1556'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='Уникальная подписка',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='Уникальная подписка'),
        ),
    ]