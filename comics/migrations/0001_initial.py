# Generated by Django 2.1.3 on 2018-11-06 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Autores',
                'verbose_name_plural': 'Autores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.ManyToManyField(related_name='keyautor', to='comics.Autor', verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Comic',
                'verbose_name_plural': 'Comics',
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editoriales',
                'ordering': ['-nombre'],
            },
        ),
        migrations.AddField(
            model_name='comic',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyeditorial', to='comics.Editorial'),
        ),
    ]
