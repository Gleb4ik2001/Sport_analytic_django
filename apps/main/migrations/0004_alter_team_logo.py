# Generated by Django 4.2.3 on 2023-08-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_team_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/logos/', verbose_name='логотип'),
        ),
    ]