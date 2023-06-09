# Generated by Django 3.2.18 on 2023-04-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('physics_marks', models.IntegerField()),
                ('chemistry_marks', models.IntegerField()),
                ('maths_marks', models.IntegerField()),
                ('computer_science_marks', models.IntegerField()),
                ('percentage_marks', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
