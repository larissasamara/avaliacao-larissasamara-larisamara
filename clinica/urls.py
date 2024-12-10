from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from clinica_api import urls as clinica_urls

schema_view = get_schema_view(
    openapi.Info(
        title="API de Atendimentos",
        default_version="v1",
        description="Documentação da API de Atendimentos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suporte@exemplo.com"),
        license=openapi.License(name="Licença MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('clinica/', include(clinica_urls)),

    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
