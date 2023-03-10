"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tasks import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login.html', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout.html', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro.html', views.Registros, name='Registros'),
    path('about.html', views.About, name='About'),
    path('registro_produ.html', views.Registro_produ, name='Registroprodu'),
    path('registro_vacas.html', views.Registro_vacas, name='Registrovacas'),
    path('perfilvacas.html', views.Perfilvacas, name='Perfilvacas'),
    path('lechetotal.html', views.Totalleche, name='Totalleche'),
    path('datosvacas.html/<a>', views.Datosvacas, name='Datosvacas'),
    path('ingleche.html', views.Ingresarleche, name='Ingresaleche'),
    path('prediccion.html', views.Prediccion, name='Prediccion'),
]
