from .models import Todo
from django.views.generic import CreateView, ListView, DeleteView
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo

class TodoCreateViem(CreateView):
    model = Todo
    fields = ['nome', 'data_consulta','hora_consulta','dentista']
    
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')