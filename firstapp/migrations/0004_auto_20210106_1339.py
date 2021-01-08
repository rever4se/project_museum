# Generated by Django 3.1.4 on 2021-01-06 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_card_db_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_db',
            name='exhibition_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='firstapp.exhibition_db'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author_db',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='card_db',
            name='create_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exhibition_db',
            name='finish_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exhibition_db',
            name='start_date',
            field=models.DateField(),
        ),
    ]
