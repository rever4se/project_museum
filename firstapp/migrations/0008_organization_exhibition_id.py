# Generated by Django 3.1.4 on 2021-01-06 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_card_db_exhibition_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='exhibition_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstapp.exhibition_db'),
            preserve_default=False,
        ),
    ]
