# Generated by Django 4.0.6 on 2022-07-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('is_done', models.BooleanField()),
                ('tags', models.ManyToManyField(related_name='tags', to='tasks.tag')),
            ],
        ),
    ]
