# Generated by Django 5.1.6 on 2025-03-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahrschule_muller', '0004_alter_review_url'),
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
        migrations.AddField(
            model_name='review',
            name='type',
            field=models.CharField(blank=True, max_length=200),
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
