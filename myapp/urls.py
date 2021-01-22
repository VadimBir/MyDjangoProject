"""DjangoPorject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from polls import views
from .views import LogoutView, ChangePasswd, HomeView, PasswordDetailView, PasswordAddView, PasswordUpdateView, PasswordDeleteView, UserRegisterView
from django.contrib.auth import views as auth_view
from django.contrib.auth.models import User


#from django.contrib.auth_view import logout



#from .views import LogoutView
#from django.contrib.auth.views import PasswordChangeView



urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    #path('login/', auth_view.LoginView.as_view(template_name='login.html') ,name='login'),
    path('password/<int:pk>', PasswordDetailView.as_view(), name='password-info'),
    path('passoword_add/', PasswordAddView.as_view(), name='password_add'),
    path('password/passoword_update/<int:pk>/', PasswordUpdateView.as_view(), name='password_update'),
    path('password/passoword_delete/<int:pk>/', PasswordDeleteView.as_view(), name='password_delete'),
    
    
    path('userregister/', UserRegisterView.as_view(), name='userregister'),
    
    
    
    #path('notemplate/', views.home_tmplt_view, name=' home2'),
    #path('password/search/',SearchView.as_view(), name = 'search'),
    #path('password/', include('myappUsers.urls')),
    #path('password-change/', UserRegisterView.as_view(), name='password-change'),
    #url(r"^accounts/", include("django.contrib.auth.urls")),
    #url(r"^dashboard/", views.dashboard_view, name="dashboard"),
    #url(r"^register/", views.register, name="register"),
    #url(r"^account/profile/", views.dashboard_view, name="dashboard"),

    path('admin/', admin.site.urls),
    #path('password-change/',)     
    
    path('change_password/', ChangePasswd.as_view(template_name='change_password.html'), name='change_password'),
    #url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout') 
    #path('password/logout/', LogoutView.as_view(), name='logout'),
    #path('password/change_passwd/', ChangePasswd.as_view(), name='change_passwd'),

    path('logout/',  auth_view.LogoutView.as_view(template_name='logout.html'), name='user_logout'),
    #path('password_reset/', auth_view.password_reset, name='password_reset'),


]
