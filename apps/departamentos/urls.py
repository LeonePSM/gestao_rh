from django.urls import path, include
from .views import (
    DepartamentosList,
    DepartamentosCreate,
    DepartamentosUpdate,
    DepartamentosDelete
)

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list departamentos'),
    path('novo', DepartamentosCreate.as_view(), name='create departamentos'),
    path('update/<int:pk>', DepartamentosUpdate.as_view(), name='update departamentos'),
    path('delete/<int:pk>', DepartamentosDelete.as_view(), name='delete departamentos'),
]
