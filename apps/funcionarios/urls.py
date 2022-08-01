from django.urls import path
from .views import (
    FuncionariosList,
    FuncionariosEdit,
    FuncionariosDelete,
    FuncionariosNovos,
)

urlpatterns = [
    path('', FuncionariosList.as_view(), name="list funcionarios"),
    path('editar/<int:pk>', FuncionariosEdit.as_view(), name="update funcionarios"),
    path('deletar/<int:pk>', FuncionariosDelete.as_view(), name="delete funcionarios"),
    path('novo/', FuncionariosNovos.as_view(), name="create funcionarios"),
]
