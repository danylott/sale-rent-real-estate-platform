# Generated by Django 3.2.8 on 2021-11-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_auto_20211116_1824"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="brand",
            new_name="author",
        ),
        migrations.AddField(
            model_name="product",
            name="genre",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="numOfPages",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="publishing",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
