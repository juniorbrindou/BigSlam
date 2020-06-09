# Generated by Django 3.0.7 on 2020-06-07 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rencontre', models.CharField(max_length=255)),
                ('stade', models.CharField(max_length=255)),
                ('date_start', models.DateTimeField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='League', to='league.League')),
            ],
            options={
                'verbose_name': 'Rencontre (VS)',
                'verbose_name_plural': 'Rencontres (VS)',
            },
        ),
    ]