# Generated by Django 2.2.2 on 2019-07-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0007_auto_20190704_0504")]

    operations = [
        migrations.AddField(
            model_name="guru",
            name="code",
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="guru",
            name="legal_name",
            field=models.CharField(
                blank=True, help_text="Legal name", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="guru",
            name="name",
            field=models.CharField(help_text="Name", max_length=255, unique=True),
        ),
    ]