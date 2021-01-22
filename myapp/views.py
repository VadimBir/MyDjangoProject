from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #, UserRegisterView
from .models import Password
from .forms import PasswordForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

#from django.contrib.auth_view 
#from django.contrib.auth import logout
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
    fields = ['Name_Tag', 'Password_String', 'Description']
    #fields = '__all__'
    #fields = ('nameTag', 'passwordStr', 'description')
    success_url = reverse_lazy('home')


class PasswordDeleteView(DeleteView):
    model = Password
    template_name = 'password_delete.html'
    success_url = reverse_lazy('home')


class SearchView(ListView):
    model = Password
    template_name = ''
    context_object_name= 'all_search_results'
    #def get_queryset(self):
    #    result super(SearchView,self).get_queryset
    #    query = self.request.GET.get('search')
    #    if query:
    #        postresult = Password.objects.filter(title_containts = query)
    #        result = postresult
    #       else:
    #            result = None
    #        return result


class LogoutView(ListView):
    # if not request.user.is_valid:
    #    return render(request, 'home')
    template_name = 'logout.html'
    #return HttpResponse("<h1> You have been logged out</h1>")
    #def get(self, request):
    #    logout(request)
    #    success_url = reverse_lazy('home')

class ChangePasswd(PasswordChangeView):
    model = Password
    template_name = 'base2.html'
    success_url = reverse_lazy('home')

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    