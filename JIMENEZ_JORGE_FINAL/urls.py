"""
URL configuration for JIMENEZ_JORGE_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from evfinal_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    #DATOS DE AUTOR
    path('jorgito/',views.Jorgito),

    #FORMULARIOS
    path('formulario_inscritos/',views.cinscritos),
    path('formulario_instituciones/',views.cinstitucion),

    #ESTOS PATH SON DE LOS FUNCTION BASE VIEW
    path('institucion/',views.Institucion_list),#este path lista todos los estudiantes
    path('institucion_detalle/<int:id>',views.Institucion_detalle),#este es para ver individual

    #ESTOS PATH SON DE LOS CLASS BASE VIEW
    path('inscritos_class/',views.InscritosList_class.as_view()), # nose cual es la diferencia
    path('inscritos_class_deta/<int:id>',views.Inscritos_detalle_class.as_view()), #NOSE CUAL ES LA DIFERENCIA
]


