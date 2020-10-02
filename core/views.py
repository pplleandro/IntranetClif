from django.shortcuts import render
from RedeSocial.models import Rede, Banner, Banner2, Banner3, Institucional


def index(request):
    tabela = Rede.objects.get(pk=1)
    banner = Banner.objects.all()
    banner2 = Banner2.objects.all()
    banner3 = Banner3.objects.all()
    videoInst = Institucional.objects.get()

    return render(request, 'index.html', {'RedeSocial':tabela, 'banner': banner, 'banner2': banner2,
                                          'banner3': banner3, 'videoInst': videoInst})