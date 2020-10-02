from django.db import models

class Rede(models.Model):
    instagram = models.CharField(verbose_name='Instagram', max_length=100)
    youtube = models.CharField(verbose_name='YouTube', max_length=100)
    linkedin = models.CharField(verbose_name='Linkedin', max_length=100)
    site = models.CharField(verbose_name='Site', max_length=100)

    def __str__(self):
        return 'Redes cadastradas'


class Banner(models.Model):
    titulo = models.CharField(verbose_name='Titulo', max_length=100)
    conteudo = models.CharField(verbose_name='Conteudo', max_length=100)
    imagem = models.ImageField(verbose_name='Imagem 1920x780', upload_to='media/')


    def __str__(self):
        return 'Banners 01'

class Banner2(models.Model):
    titulo = models.CharField(verbose_name='Titulo', max_length=100)
    conteudo = models.CharField(verbose_name='Conteudo', max_length=100)
    imagem = models.ImageField(verbose_name='Imagem 1920x780', upload_to='media/')


    def __str__(self):
        return 'Banners 02'

class Banner3(models.Model):
    titulo = models.CharField(verbose_name='Titulo', max_length=100)
    conteudo = models.CharField(verbose_name='Conteudo', max_length=100)
    imagem = models.ImageField(verbose_name='Imagem 1920x780', upload_to='media/')


    def __str__(self):
        return 'Banners 03'

class Institucional(models.Model):
    nome = models.CharField(verbose_name='Titulo', max_length=100)
    video = models.FileField(verbose_name='Apresentação', upload_to='media/')