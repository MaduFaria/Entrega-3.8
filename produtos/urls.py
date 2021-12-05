from django.urls import path

from produtos.views import (
    index, ola,
    CreateProdutoView,
    ListProdutoView,
    DetailProdutoView,
    UpdateProdutoView,
    DeleteProdutoView,
)

urlpatterns = [
    path('', index ,name="index"),
    path('ola/', ola , name="ola"),
    path('category/add',
            CreateProdutoView.as_view(),
            name='create_produto',
        ),
    path('category',
            ListProdutoView.as_view(),
            name='list_produto',
        ),
     path('category/<int:pk>',
            DetailProdutoView.as_view(),
            name='produto_detail'),

      path('category/<int:pk>/update',
            UpdateProdutoView.as_view(),
            name="produto_update"),
            
      path('category/<int>pk>/delete',
            DeleteProdutoView.as_view(),
            name="produto_delete"),
]