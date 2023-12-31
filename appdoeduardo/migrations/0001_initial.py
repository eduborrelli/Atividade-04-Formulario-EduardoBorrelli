# Generated by Django 3.2.13 on 2023-09-04 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='common_sectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
                ('importance', models.CharField(choices=[('V', 'Very important'), ('I', 'Important'), ('N', 'Necessary')], max_length=1)),
                ('difficulty', models.CharField(choices=[('H', 'Hard'), ('M', 'Medium'), ('E', 'Easy')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='top15',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=30)),
                ('fuel', models.CharField(max_length=20)),
                ('placement', models.IntegerField()),
            ],
        ),
    ]
