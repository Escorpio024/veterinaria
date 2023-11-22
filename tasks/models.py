from django.db import models

class Persona(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    rol = models.CharField(max_length=20, choices=[('administrador', 'administrador'), ('medico veterinario', 'medico veterinario'), ('dueño de mascota', 'dueño de mascota'), ('vendedor', 'vendedor')])

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    persona_cedula = models.ForeignKey(Persona, on_delete=models.CASCADE)
    edad = models.IntegerField()
    especie = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    caracteristicas = models.CharField(max_length=200)

class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    medicamento = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    fecha = models.DateField()

class Hc(models.Model):
    id_hc = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=200)
    sistematogia = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=200)
    procedimiento = models.CharField(max_length=200)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=200)

class MedFact(models.Model):
    id_medfact = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valor_vto = models.IntegerField()

class FacturaVet(models.Model):
    id_factura = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.IntegerField()

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    rol = models.CharField(max_length=20)
