# Generated by Django 3.1.2 on 2020-11-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('asunto', models.CharField(max_length=200)),
                ('mensaje', models.CharField(max_length=200)),
            ],
        ),
    ]