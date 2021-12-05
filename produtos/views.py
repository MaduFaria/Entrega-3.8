from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import (
  CreateView,
  UpdateView,
  DeleteView,
)

from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from produtos.models import Produto
# Create your views here.

def index(request):
  return HttpResponse('Olá Django! (index)')

def ola(request):
  return HttpResponse('Olá, Django!') 

class CreateProdutoView(CreateView):
  model = Produto
  fields = ('codigo', 'nome_produto', 'preco', 'avaliacao_produto')
  template_name = 'create_produto.html'
  success_url = reverse_lazy('create_produto')

class ListProdutoView(ListView):
  model = Produto
  template_name = 'list_produto.html'
  context_object_name = 'produtos'

class DetailProdutoView(DetailView):
  model = Produto
  template_name = 'produto_detail.html'

class UpdateProdutoView(UpdateView):
  model = Produto
  template_name = 'produto_form.html'
  fields = ('name', 'description')
  template_name = 'create_produto.html'
  success_url = reverse_lazy('list_produto')

class DeleteProdutoView(DeleteView):
  model = Produto
  template_name = 'produto_confirm_delete.html'
  success_url = reverse_lazy('list_produto')
