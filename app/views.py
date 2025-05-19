from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PessoaView(View): 
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class OcupacaoView(View):  
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

class InstituicaoEnsinoView(View):  
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})

class AreaSaberView(View):  
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areas': areas})

class CursoView(View):  
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class TurmaView(View):  
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class DisciplinaView(View):  
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

class MatriculaView(View):  
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

class AvaliacaoView(View):  
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})

class FrequenciaView(View):  
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

class TurnoView(View):  
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turnoS.html', {'turnos': turnos})
    
class CidadeView(View):  
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class OcorrenciaView(View):  
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})

class CursoDisciplinaView(View):  
    def get(self, request, *args, **kwargs):
        cursos_disciplinas = CursoDisciplina.objects.all()
        return render(request, 'cursodisciplina.html', {'cursos_disciplinas': cursos_disciplinas})

class AvaliacaoTipoView(View): 
    def get(self, request, *args, **kwargs):
        tipos = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacaotipo.html', {'tipos': tipos})

class DeletePessoaView(View):
    def get(self, request, id, *args, **kwargs):
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        messages.success(request, 'Pessoa excluída com sucesso!')  # Success message
        return redirect('pessoas')
