from django.contrib import admin
from django.urls import path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),    
    path('pessoa/', PessoaView.as_view(), name='pessoa_list'),# Página principal agora é a listagem de pessoas
    path('delete/<int:id>/', DeletePessoaView.as_view(), name='delete_pessoa'),  # Excluir pessoa             # RF01
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),                       # RF02
    path('instituicao/', InstituicaoEnsinoView.as_view(), name='instituicao'),        # RF03
    path('areasaber/', AreaSaberView.as_view(), name='areasaber'),                    # RF04
    path('curso/', CursoView.as_view(), name='curso'),                                # RF05
    path('turma/', TurmaView.as_view(), name='turma'),                                # RF06
    path('disciplina/', DisciplinaView.as_view(), name='disciplinas'),               # RF07
    path('matricula/', MatriculaView.as_view(), name='matricula'),                    # RF08
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),                    # RF09
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),                 # RF10
    path('turno/', TurnoView.as_view(), name='turnos'),                              # RF11
    path('cidade/', CidadeView.as_view(), name='cidade'),                             # RF12
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),                 # RF13
    path('cursodisciplina/', CursoDisciplinaView.as_view(), name='cursodisciplina'),  # RF14
    path('avaliacaotipo/', AvaliacaoTipoView.as_view(), name='avaliacaotipo'),        # RF15

   
   
]
