# Generated by Django 4.0.2 on 2022-02-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='writer',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]