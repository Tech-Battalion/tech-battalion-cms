# Generated by Django 3.0.6 on 2020-05-30 19:10

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tech_news', '0008_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='tech_news.BlogCategory'),
        ),
    ]
