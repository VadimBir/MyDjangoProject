from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Password
from .forms import PasswordForm
from django.urls import reverse_lazy, reverse
# Create your views here.


#def home_view(request):
 #   return render(request, 'home.html', {})


class HomeView(ListView):
    model = Password
    template_name = 'home.html'
    ordering = ['-id']


class PasswordDetailView(DetailView):
    model = Password
    template_name = "passwordinfo.html"


class PasswordAddView(CreateView):
    model = Password
    form_class = PasswordForm
    template_name = 'password_add.html'
    #fields = '__all__'
    #fields = ('nameTag', 'passwordStr', 'description')
    success_url = reverse_lazy('home')


class PasswordUpdateView(UpdateView):
    model = Password
    template_name = 'password_update.html'
    fields = ['nameTag', 'passwordStr', 'description']
    #fields = '__all__'
    #fields = ('nameTag', 'passwordStr', 'description')
    success_url = reverse_lazy('home')


class PasswordDeleteView(DeleteView):
    model = Password
    template_name = 'password_delete.html'
    success_url = reverse_lazy('home')
