# Generated by Django 3.2.8 on 2021-11-19 04:04

from django.db import migrations, models
import django.db.models.deletion
import game.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
        ('tails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poke_caught', models.CharField(max_length=30)),
                ('poke_missed', models.CharField(max_length=30)),
                ('poke_pic', models.ImageField(upload_to='uploads/', verbose_name=game.models.Pokemon)),
                ('poke_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.pokemon')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tails.person')),
            ],
        ),
    ]