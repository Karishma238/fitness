# Generated by Django 4.1.2 on 2023-03-13 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0006_subexercise_delete_workoutexercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='')),
                ('Exer_Name', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.workoutcategory')),
            ],
            options={
                'db_table': 'CatExercise',
            },
        ),
    ]
