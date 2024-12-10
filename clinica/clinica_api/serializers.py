from rest_framework import serializers
from .models import Atendimento, Paciente, Profissional, Convenio, TipoAtendimento

class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = [
            "paciente",
            "profissional",
            "data",
            "diagnostico",
            "convenio",
            "tipo_atendimento",
        ]

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ["nome", "idade", "email"]

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ["nome", "especialidade", "crm"]

class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = ["nome", "numero_contrato"]

class TipoAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAtendimento
        fields = ["descricao"]
