from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=1, default='x')

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    identificacao = models.CharField(max_length=20)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.identificacao


class AlunoTurma(models.Model):
    identificacao = models.CharField(max_length=20)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.turma.identificacao + " - " + self.aluno.nome


class Avaliacao(models.Model):
    aluno_turma = models.ForeignKey(AlunoTurma, on_delete=models.CASCADE)
    identificacao = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.aluno_turma.turma.identificacao} - {self.aluno_turma.aluno.nome} - {self.identificacao} - {self.nota}"
