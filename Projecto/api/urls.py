from django.urls import path
from .views import CompanyView, UsuarioView

urlpatterns=[
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),
    path('usuarios/', UsuarioView.as_view(), name='usuario_list'),
    path('usuarios/<int:id>', UsuarioView.as_view(), name='usuario_process')
]