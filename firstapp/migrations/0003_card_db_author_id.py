# Generated by Django 3.1.4 on 2021-01-04 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_db',
            name='author_id',
            field=models.ForeignKey(default=1970, on_delete=django.db.models.deletion.CASCADE, to='firstapp.author_db'),
            preserve_default=False,
        ),
    ]
