from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages


from django.views.generic import ListView
from django.urls import reverse_lazy


# Create your views here.

def home_views(request, *args, **kwargs):
    my_context = {
        "my_testText": "This is some text that I have",
        "my_nums": [1, 2, 3, 4, 5, 6],
        "my_boolean": True,
        "my_testNum": 15
    }
    return HttpResponse("<h1> Hello World2</h1>")
    #return render(request, "base2.html", my_context)

def home_tmplt_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World</h1>")


def dashboard_view(request):
    return render(request, "users/dashboard.html")


def LogoutView(request):
    # if not request.user.is_valid:
    #    return render(request, 'home')
    template_name = 'logout.html'
    success_url = reverse_lazy('home')
    return HttpResponse("<h1> You have been logged out2</h1>")

''' def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
        )
            {"form": UserCreationForm}
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        form.error_messages
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            login(request, user)
            return render(request, "users/dashboard.html")
        #print("Form is NOT valid")
        messages.error(request, "Error")
        return render(request, 'users/dashboard.html', {'form': form})

'''