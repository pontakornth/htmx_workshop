# Generated by Django 5.0.2 on 2024-02-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_background_color_alter_post_text_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='background_color',
            field=models.CharField(blank=True, default='#ffffff', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_color',
            field=models.CharField(blank=True, default='#000000', max_length=10, null=True),
        ),
    ]
