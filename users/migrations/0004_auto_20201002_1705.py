# Generated by Django 3.1.2 on 2020-10-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201002_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], default='M', max_length=5),
        ),
    ]
