# -*- encoding:utf-8 -*-
from Usuarios.models import Usuario
from rest_framework.response import Response
from rest_framework.views import APIView

class nose(APIView):
    def post(self, request):
        response = {}

        usuario_prueba = Usuario()
        usuario_prueba.nombre = 'josue'
        usuario_prueba.apellido_paterno = 'garcia'
        usuario_prueba.apellido_materno = 'villar'
        usuario_prueba.save()
        return Response(response)
