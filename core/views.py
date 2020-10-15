from django.shortcuts import render
from RedeSocial.models import Rede, Banner, Banner2, Banner3, Institucional, Aniversario


def index(request):
    tabela = Rede.objects.get(pk=1)
    banner = Banner.objects.all()
    banner2 = Banner2.objects.all()
    banner3 = Banner3.objects.all()
    aniver = Aniversario.objects.all()

    print(request.user.has_perm('RedeSocial.view_banner'))
    #print(request.user.get_all_permissions())
    print(request.user)

    return render(request, 'index.html', {'RedeSocial':tabela, 'banner': banner, 'banner2': banner2,
                                          'banner3': banner3, 'aniver':aniver })

def JanelaProgramacao(request):

    return render(request, 'Janela.html', {})