from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mascota, Usuario , Orden , Medicamento , Hc, MedFact , FacturaVet , Persona

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })

    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()

                usuario = Usuario(usuario=request.POST['username'], contraseña=request.POST['password1'], rol=request.POST['rol']) 
                usuario.save()

                login(request, user)

                if usuario.rol == 'administrador':
                    return redirect('/administrador/')
                elif usuario.rol == 'cliente':
                    return redirect('/cliente/') 
                elif usuario.rol == 'veterinario':
                    return redirect('/veterinario/')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            'error': 'Passwords do not match'
        })

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:

            try:
                usuario = Usuario.objects.get(usuario=username)
                if usuario.rol == 'administrador':
                    return redirect('/administrador/')
                elif usuario.rol == 'cliente':
                    return redirect('/cliente/') 
                elif usuario.rol == 'veterinario':
                    return redirect('/veterinario/')
                else:
                    return render(request, 'signin.html', {'error': 'Usuario sin rol, registrate de nuevo'})
            except Usuario.DoesNotExist:
                return render(request, 'signin.html', {'error': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'signin.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'signin.html')

def cliente(request):
    return render(request, 'cliente.html')

def veterinario(request):
    return render(request, 'veterinario.html')

def administrador(request):
    return render(request, 'administrador.html')

def menu(request):
    return render(request, 'menu.html')

'''funciones de todas las tablas'''

    
'''Personas'''
def mostrar_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', {'personas': personas})

@csrf_exempt
def eliminar_persona(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        persona = Persona.objects.filter(cedula=cedula)
        if persona.exists():
            persona.delete()
            return JsonResponse({'mensaje': 'Persona eliminada correctamente'})
        else:
            return JsonResponse({'mensaje': 'Persona no encontrada'}, status=404)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

@csrf_exempt
def agregar_persona(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        rol = request.POST.get('rol')

        persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, edad=edad, rol=rol)
        persona.save()

        return JsonResponse({'mensaje': 'Persona agregada correctamente'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

'''Mascotas'''
def mostrar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas.html', {'mascotas': mascotas})

@csrf_exempt
def eliminar_mascota(request):
    if request.method == 'POST':
        id_mascota = request.POST.get('id_mascota')
        mascota = Mascota.objects.filter(id_mascota=id_mascota)
        if mascota.exists():
            mascota.delete()
            return JsonResponse({'mensaje': 'Mascota eliminada correctamente'})
        else:
            return JsonResponse({'mensaje': 'Mascota no encontrada'}, status=404)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

@csrf_exempt
def agregar_mascota(request):
    if request.method == 'POST':
        persona_cedula = request.POST.get('persona_cedula', None)
        if persona_cedula is not None:
            try:
                persona_cedula = Persona.objects.get(cedula=persona_cedula)
            except Persona.DoesNotExist:
                return JsonResponse({'mensaje': 'Error: Persona no encontrada'}, status=404)

            edad = request.POST.get('edad')
            especie = request.POST.get('especie')
            raza = request.POST.get('raza')
            caracteristicas = request.POST.get('caracteristicas')

            mascota = Mascota(persona_cedula=persona_cedula, edad=edad, especie=especie, raza=raza, caracteristicas=caracteristicas)
            mascota.save()

            return JsonResponse({'mensaje': 'Mascota agregada correctamente'})
        else:
            return JsonResponse({'mensaje': 'Error: Cédula de persona no proporcionada'}, status=400)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

'''Medicamento'''
def mostrar_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos.html', {'medicamentos': medicamentos})

@csrf_exempt
def eliminar_medicamento(request):
    if request.method == 'POST':
        id_medicamento = request.POST.get('id_medicamento')
        medicamento = Medicamento.objects.filter(id_medicamento=id_medicamento)
        if medicamento.exists():
            medicamento.delete()
            return JsonResponse({'mensaje': 'Medicamento eliminado correctamente'})
        else:
            return JsonResponse({'mensaje': 'Medicamento no encontrado'}, status=404)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)


@csrf_exempt
def agregar_medicamento(request):
    if request.method == 'POST':
        medicamento = request.POST.get('medicamento')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')

        medicamento_obj = Medicamento(medicamento=medicamento, cantidad=cantidad, precio=precio)
        medicamento_obj.save()

        return JsonResponse({'mensaje': 'Medicamento agregado correctamente'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

'''Orden'''
def mostrar_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'ordenes.html', {'ordenes': ordenes})

@csrf_exempt
def eliminar_orden(request):
    if request.method == 'POST':
        id_orden = request.POST.get('id_orden')
        orden = Orden.objects.filter(id_orden=id_orden)
        if orden.exists():
            orden.delete()
            return JsonResponse({'mensaje': 'Orden eliminada correctamente'})
        else:
            return JsonResponse({'mensaje': 'Orden no encontrada'}, status=404)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

@csrf_exempt
def agregar_orden(request):
    if request.method == 'POST':
        id_orden = request.POST.get('id_orden')
        mascota_id = request.POST.get('mascota')
        veterinario_cedula = request.POST.get('veterinario')
        medicamento_id = request.POST.get('medicamento')
        fecha = request.POST.get('fecha')

        try:
            mascota = Mascota.objects.get(id_mascota=mascota_id)
            veterinario = Persona.objects.get(cedula=veterinario_cedula)
            medicamento = Medicamento.objects.get(id_medicamento=medicamento_id)
        except (Mascota.DoesNotExist, Persona.DoesNotExist, Medicamento.DoesNotExist) as e:
            return JsonResponse({'mensaje': 'Error: {}'.format(str(e))}, status=404)

        orden = Orden(id_orden=id_orden, mascota=mascota, veterinario=veterinario, medicamento=medicamento, fecha=fecha)
        orden.save()

        return JsonResponse({'mensaje': 'Orden agregada correctamente', 'id_orden': orden.id_orden})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

    
'''hc'''
def mostrar_hc(request):
    historias_clinicas = Hc.objects.all()
    return render(request, 'hcs.html', {'hcs': historias_clinicas})

@csrf_exempt
def eliminar_hc(request):
    if request.method == 'POST':
        id_hc = request.POST.get('id_hc')
        hc = Hc.objects.filter(id_hc=id_hc)
        if hc.exists():
            hc.delete()
            return JsonResponse({'mensaje': 'Historia clínica eliminada correctamente'})
        else:
            return JsonResponse({'mensaje': 'Historia clínica no encontrada'}, status=404)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)


@csrf_exempt
def agregar_hc(request):
    if request.method == 'POST':
        id_hc = request.POST.get('id_hc')
        mascota_id = request.POST.get('mascota')
        motivo = request.POST.get('motivo')
        sistematogia = request.POST.get('sistematogia')
        diagnostico = request.POST.get('diagnostico')
        procedimiento = request.POST.get('procedimiento')
        medicamento_id = request.POST.get('medicamento')
        dosis = request.POST.get('dosis')

        try:
            mascota = Mascota.objects.get(id_mascota=mascota_id)
            medicamento = Medicamento.objects.get(id_medicamento=medicamento_id)
        except (Mascota.DoesNotExist, Medicamento.DoesNotExist) as e:
            return JsonResponse({'mensaje': f'Error: {str(e)}'}, status=404)

        hc = Hc(id_hc=id_hc, mascota=mascota, motivo=motivo, sistematogia=sistematogia, diagnostico=diagnostico, procedimiento=procedimiento, medicamento=medicamento, dosis=dosis)
        hc.save()

        return JsonResponse({'mensaje': 'Historia clínica agregada correctamente'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)


'''medfact'''
def mostrar_medfact(request):
    medicamentos_factura = MedFact.objects.all()
    return render(request, 'medfact.html', {'medicamentos_factura': medicamentos_factura})

@csrf_exempt
def eliminar_medfact(request):
    if request.method == 'POST':
        id_medfact = request.POST.get('id_medfact')
        medfact = MedFact.objects.filter(id_medfact=id_medfact)
        if medfact.exists():
            medfact.delete()
            return JsonResponse({'mensaje': 'Medicamento de factura eliminado correctamente'})
        else:
            return JsonResponse({'mensaje': 'Medicamento de factura no encontrado'}, status=404)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)


@csrf_exempt
def agregar_medfact(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto', None)
        if producto_id is not None:
            try:
                producto = Medicamento.objects.get(id_medicamento=producto_id)
            except Medicamento.DoesNotExist:
                return JsonResponse({'mensaje': 'Medicamento no encontrado'}, status=404)

            id_medfact = request.POST.get('id_medfact')
            cantidad = request.POST.get('cantidad')
            valor_vto = request.POST.get('valor_vto')

            medfact = MedFact(id_medfact=id_medfact, producto=producto, cantidad=cantidad, valor_vto=valor_vto)
            medfact.save()

            return JsonResponse({'mensaje': 'Medicamento de factura agregado correctamente'})
        else:
            return JsonResponse({'mensaje': 'Campo "producto" no proporcionado en la solicitud'}, status=400)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
'''facturas'''

def mostrar_facturas(request):
    facturas = FacturaVet.objects.all()
    return render(request, 'facturas.html', {'facturas': facturas})

@csrf_exempt
def eliminar_factura(request):
    if request.method == 'POST':
        id_factura = request.POST.get('id_factura')
        factura = FacturaVet.objects.filter(id_factura=id_factura)
        if factura.exists():
            factura.delete()
            return JsonResponse({'mensaje': 'Factura eliminada correctamente'})
        else:
            return JsonResponse({'mensaje': 'Factura no encontrada'}, status=404)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)


@csrf_exempt
def agregar_factura(request):
    if request.method == 'POST':
        id_factura = request.POST.get('id_factura')
        mascota = request.POST.get('mascota')
        persona = request.POST.get('persona')
        orden = request.POST.get('orden')
        fecha = request.POST.get('fecha')
        total = request.POST.get('total')

        try:
            mascota = Mascota.objects.get(id_mascota=mascota)
            persona = Persona.objects.get(cedula=persona)
            orden = Orden.objects.get(id_orden=orden)
        except (Mascota.DoesNotExist, Persona.DoesNotExist, Orden.DoesNotExist) as e:
            return JsonResponse({'mensaje': f'Error: {str(e)}'}, status=404)

        factura = FacturaVet(id_factura=id_factura, mascota=mascota, persona=persona, orden=orden, fecha=fecha, total=total)
        factura.save()

        return JsonResponse({'mensaje': 'Factura agregada correctamente'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
