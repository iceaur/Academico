from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField()
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE)
    ocupacao = models.ForeignKey('Ocupacao', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey('AreaSaber', on_delete=models.CASCADE)
    instituicao = models.ForeignKey('InstituicaoEnsino', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey('AreaSaber', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    instituicao = models.ForeignKey('InstituicaoEnsino', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f"{self.pessoa} - {self.curso}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"

class Avaliacao(models.Model):
    descricao = models.TextField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    avaliacao_tipo = models.ForeignKey('AvaliacaoTipo', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class Frequencia(models.Model):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    periodo = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Curso/Disciplina"
        verbose_name_plural = "Cursos/Disciplinas"
