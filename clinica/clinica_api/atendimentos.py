from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Atendimento
from .serializers import AtendimentoSerializer

@api_view(["GET"])
def atendimentos_por_profissional(request, profissional_id):
    atendimentos = Atendimento.objects.filter(profissional_id=profissional_id)
    serializer = AtendimentoSerializer(atendimentos, many=True)
    return Response({"profissional_id": profissional_id, "quantidade": atendimentos.count(), "atendimentos": serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def atendimentos_por_paciente(request, paciente_id):
    atendimentos = Atendimento.objects.filter(paciente_id=paciente_id)
    serializer = AtendimentoSerializer(atendimentos, many=True)
    return Response({"paciente_id": paciente_id, "quantidade": atendimentos.count(), "atendimentos": serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def atendimentos_por_periodo(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if not start_date or not end_date:
        return Response({"error": "Os parâmetros start_date e end_date são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)
    
    atendimentos = Atendimento.objects.filter(data_atendimento__range=[start_date, end_date])
    serializer = AtendimentoSerializer(atendimentos, many=True)
    return Response({"start_date": start_date, "end_date": end_date, "quantidade": atendimentos.count(), "atendimentos": serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def atendimentos_por_convenio(request, convenio_id):
    atendimentos = Atendimento.objects.filter(convenio_id=convenio_id)
    serializer = AtendimentoSerializer(atendimentos, many=True)
    return Response({"convenio_id": convenio_id, "quantidade": atendimentos.count(), "atendimentos": serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def atendimentos_por_tipo(request, tipo):
    atendimentos = Atendimento.objects.filter(tipo_atendimento=tipo)
    serializer = AtendimentoSerializer(atendimentos, many=True)
    return Response({"tipo": tipo, "quantidade": atendimentos.count(), "atendimentos": serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def atendimentos_por_diagnostico(request, diagnostico_id):
    atendimentos = Atendimento.objects.filter(diagnostico_id=diagnostico_id)
    serializer = AtendimentoSerializer(atendimentos, many=True)
    return Response({"diagnostico_id": diagnostico_id, "quantidade": atendimentos.count(), "atendimentos": serializer.data}, status=status.HTTP_200_OK)
