# -*- encoding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(models.Model):

    nombre = models.CharField(max_length=25, null=False)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    numero = models.CharField(max_length=10, null=False)
    correo = models.CharField(max_length=25, null=False, unique=True)