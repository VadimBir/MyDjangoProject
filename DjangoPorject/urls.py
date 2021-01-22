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
from django.conf.urls import include, url
from polls import views


from django.contrib.auth import views as auth_view


urlpatterns = [

    path('', views.home_views, name='home'),
    path('notemplate/', views.home_tmplt_view, name='home2'),
    #path(r"^accounts/", include("django.contrib.auth.urls")),
    path('myapp/', include('myapp.urls')),
    #path('myappUsers/', include('django.contrib.auth.urls')),
    #path('myappUsers/', include('myappUsers.urls')),


    #url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", views.dashboard_view, name="dashboard"),
    #url(r"^register/", views.register, name="register"),
    #url(r"^account/profile/", views.dashboard_view, name="dashboard"),



    #path('change_password/'), views.ChangePasswd, name="change_password"
    path('login/', auth_view.LoginView.as_view(template_name='login.html') ,name='login'),
    path('logout/',  auth_view.LogoutView.as_view(template_name='logout.html'), name='user_logout'),



    path('admin/', admin.site.urls),



]
