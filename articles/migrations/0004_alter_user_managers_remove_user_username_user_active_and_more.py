# Generated by Django 4.0.4 on 2022-04-25 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_subscriber',
            field=models.BooleanField(default=True, verbose_name='Подписчик'),
        ),
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]