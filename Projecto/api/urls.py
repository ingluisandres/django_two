from django.urls import path
from .views import CompanyView, UsuarioView, UsuariosByAgeView, UsuariosByLastNameView

urlpatterns=[
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),
    path('usuarios/', UsuarioView.as_view(), name='usuario_list'),
    path('usuarios/<int:id>', UsuarioView.as_view(), name='usuario_process'),
    path('usuarios/age/', UsuariosByAgeView.as_view(), name='usuarios_by_age'),
    path('usuarios/lastname/', UsuariosByLastNameView.as_view(), name='usuarios_by_lastname')
]