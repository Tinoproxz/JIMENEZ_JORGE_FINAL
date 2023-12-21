from django.shortcuts import render,redirect
from .models import Inscritos,Instituciones
from . import forms
from .forms import InscritosForm,InstitucionesForm
from .serializers import InscritosSerializer,InstitucionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404,JsonResponse


#VISTAS
def index (request):
    data={'title':'SEMINARIO GASTRONOMICO'}
    return render (request,'index.html')

def cinstitucion(request):
    form = InstitucionesForm()
    if request.method == 'POST':
        form = InstitucionesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    data = {'title':'Instituciones', 'formu': form}
    return render(request, 'formularios.html', data)

def cinscritos(request):
    form = InscritosForm()
    if request.method == 'POST':
        form = InscritosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    data = {'title':'Inscritos', 'formu': form}
    return render(request, 'formularios.html', data)

def Jorgito(request):
    dato = {
        'RUT':'21.073.398-1',
        'Nombre': 'Jorge Jimenez',
        'Sección': 'IEI-171-N4',
    }
    return JsonResponse(dato)


#CLASS BASE VIEWS
#INSCRITOS

class InscritosList_class(APIView):
    def get(self, request):
        inscri =Inscritos.objects.all()
        serial = InscritosSerializer(inscri,many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial = InscritosSerializer(data= request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status = status.HTTP_201_CREATED)
        return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
class Inscritos_detalle_class(APIView):
    def get_object(self, id):
        try:
            return Inscritos.objects.get(pk=id)
        except Inscritos.DoesNotExist:
            raise Http404()

    
    def get(self,request,id):
        inscri = self.get_object(id)
        serial = InscritosSerializer(inscri)
        return Response(serial.data)
    
    def put (self,request,id):
        inscri= self.get_object(id)
        serial = InscritosSerializer(inscri,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        inscri = self.get_object(id)
        inscri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# FUNCTION BASE VIEWS
#INSTITUCIONES
@api_view(['GET','POST'])
def Institucion_list(request):
    if request.method == 'GET':
        insti = Instituciones.objects.all()
        serial = InstitucionSerializer(insti,many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','PUT','DELETE'])
def Institucion_detalle(request,id):
    try:
        insti = Instituciones.objects.get(pk=id)
    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #PARA OBTENER LOS DATOS
    if request.method == 'GET':
        serial = InstitucionSerializer(insti)
        return Response(serial.data)
    
    #PARA EDITAR DATOS
    if request.method == 'PUT':
        serial = InstitucionSerializer(insti,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #PARA BORRAR LOS DATOS
    if request.method == 'DELETE':
        insti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

