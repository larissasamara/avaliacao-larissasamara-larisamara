from django.urls import path
from .atendimentos import (
    atendimentos_por_profissional,
    atendimentos_por_paciente,
    atendimentos_por_periodo,
    atendimentos_por_convenio,
    atendimentos_por_tipo,
    atendimentos_por_diagnostico,
)

urlpatterns = [
    path("api/atendimentos/profissional/<int:profissional_id>/", atendimentos_por_profissional, name="atendimentos-por-profissional"),
    path("api/atendimentos/paciente/<int:paciente_id>/", atendimentos_por_paciente, name="atendimentos-por-paciente"),
    path("api/atendimentos/periodo/", atendimentos_por_periodo, name="atendimentos-por-periodo"),
    path("api/atendimentos/convenio/<int:convenio_id>/", atendimentos_por_convenio, name="atendimentos-por-convenio"),
    path("api/atendimentos/tipo/<str:tipo>/", atendimentos_por_tipo, name="atendimentos-por-tipo"),
    path("api/atendimentos/diagnostico/<int:diagnostico_id>/", atendimentos_por_diagnostico, name="atendimentos-por-diagnostico"),
]