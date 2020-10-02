# Generated by Django 2.2 on 2020-10-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedeSocial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('conteudo', models.CharField(max_length=100, verbose_name='Conteudo')),
                ('imagem', models.ImageField(upload_to='media/', verbose_name='Imagem 1920x780')),
            ],
        ),
    ]
