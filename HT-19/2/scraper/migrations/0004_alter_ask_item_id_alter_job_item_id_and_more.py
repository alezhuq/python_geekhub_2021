# Generated by Django 4.0.1 on 2022-02-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_remove_ask_id_remove_job_id_remove_new_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='item_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='item_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='new',
            name='item_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='show',
            name='item_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
