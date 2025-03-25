# Generated by Django 5.1.6 on 2025-03-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahrschule_muller', '0005_review_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='phone_number',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='message',
            name='url',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='form_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
