from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Convenio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Diagnostico(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Atendimento(models.Model):
    TIPO_ATENDIMENTO_CHOICES = [
        ("consulta", "Consulta"),
        ("exame", "Exame"),
        ("terapia", "Terapia"),
    ]

    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_atendimento = models.DateTimeField()
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, blank=True, null=True)
    tipo_atendimento = models.CharField(max_length=50, choices=TIPO_ATENDIMENTO_CHOICES)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.SET_NULL, blank=True, null=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Atendimento ({self.id}) - {self.data_atendimento} - {self.paciente}"
