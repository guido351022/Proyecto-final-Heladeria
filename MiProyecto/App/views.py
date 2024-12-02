from django.shortcuts import render, redirect
from App.models import *
from .forms import Crear_Cliente_forms, Crear_Helado_forms, Crear_Pedido_forms, Crear_Sabor_forms,UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.contrib import admin
from django.core.paginator import Paginator
from django.conf import settings


def mostrar_index(request):

    return render(request, 'App/index.html')
def mostrar_cliente(request):

    cliente = Cliente.objects.all()

    context = {'cliente': cliente}

    return render(request, 'App/Cliente.html', context=context)

def mostrar_helado(request):

    helado = Helado.objects.all()

    context = {'helado': helado}

    return render(request, 'App/Helado.html', context=context)

def mostrar_sabor(request):

    sabor = Sabor.objects.all()

    context = {'sabor': sabor}

    return render(request,'App/Sabor.html', context=context)

def mostrar_pedido(request):

    pedido = Pedido.objects.all()

    context = {'pedido': pedido}

    return render(request, 'App/Pedido.html', context=context)



from django.shortcuts import render, redirect
from .forms import Crear_Cliente_forms
from .models import Cliente

def crear_cliente(request):
    if request.method == 'POST':
        form = Crear_Cliente_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            cliente = Cliente(
                nombre=formulario_limpio['nombre'],
                apellido=formulario_limpio['apellido'],
                email=formulario_limpio['email']
            )
            cliente.save()

            return redirect('Cliente')

    else:
        form = Crear_Cliente_forms()

    return render(request, 'App/Crear_Cliente.html', {'form': Crear_Cliente_forms})

def crear_helado(request):
    if request.method == 'POST':
        form = Crear_Helado_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            helado = Helado(
                nombre=formulario_limpio['nombre'],
                precio=formulario_limpio['precio'],
                sabor=formulario_limpio['sabor']
            )
            helado.save()

            return redirect('Helado')
    else:
        form = Crear_Helado_forms()

    return render(request, 'App/Crear_Helado.html', {'form': Crear_Helado_forms})

def crear_sabor(request):
    if request.method == 'POST':
        form = Crear_Sabor_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            sabor = Sabor(nombre=formulario_limpio['nombre'])
            sabor.save()

            return redirect('Sabor')
    else:
        form = Crear_Sabor_forms()

    return render(request, 'App/Crear_Sabor.html', {'form': Crear_Sabor_forms})


def crear_pedido(request):
    if request.method == 'POST':
        form = Crear_Pedido_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            pedido = Pedido(
                cliente=formulario_limpio['cliente'],
                fecha=formulario_limpio['fecha']
            )
            pedido.save()

            return redirect('Pedido')
    else:
        form = Crear_Pedido_forms()

    return render(request, 'App/Crear_Pedido.html', {'form': Crear_Pedido_forms})

def buscar_cliente(request):

    if request.GET.get('apellido', False):
        apellido = request.GET['apellido']
        cliente= Cliente.objects.filter(apellido__icontains=apellido)

        return render(request, 'App/Buscar_Cliente.html', {'cliente': cliente})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/Buscar_Cliente.html',{'respuesta': respuesta})



def buscar_helado(request):

    if request.GET.get('nombre', False):
        helado = request.GET['nombre']
        helado = Helado.objects.filter(nombre__icontains=helado)

        return render(request, 'App/Buscar_Helado.html', {'helado': helado})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Helado.html', {'respuesta': respuesta})


def buscar_sabor(request):

    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        sabor = Sabor.objects.filter(nombre__icontains=nombre)

        return render(request, 'App/Buscar_Sabor.html', {'sabor': sabor})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Sabor.html', {'respuesta': respuesta})


def buscar_pedido(request):
    if request.GET.get('cliente', False):
        cliente = request.GET['cliente']
        pedido = Pedido.objects.filter(cliente__nombre__icontains=cliente)

        return render(request, 'App/Buscar_Pedido.html', {'pedido': pedido})
    else:
        respuesta = 'No hay datos'
    
    return render(request, 'App/Buscar_Pedido.html', {'respuesta': respuesta})


def actualizar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        form = Crear_Cliente_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            cliente.nombre = formulario_limpio['nombre']
            cliente.apellido = formulario_limpio['apellido']
            cliente.email = formulario_limpio['email']
            cliente.save()
            
            return redirect('Cliente')
        
    else:
        form = Crear_Cliente_forms(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'email': cliente.email})

    return render(request, 'App/Actualizar_Cliente.html', {'form': Crear_Cliente_forms})


def actualizar_helado(request, helado_id):
    helado = Helado.objects.get(id=helado_id)
    if request.method == 'POST':
        form = Crear_Helado_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            helado.nombre = formulario_limpio['nombre']
            helado.precio = formulario_limpio['precio']
            helado.sabor = formulario_limpio['sabor']
            helado.save()
            
            return redirect('Helado')
        
    else:

        form = Crear_Helado_forms(initial={'nombre': helado.nombre, 'precio': helado.precio, 'sabor': helado.sabor})

    return render(request, 'App/Actualizar_Helado.html', {'form': Crear_Helado_forms})

def actualizar_sabor(request, sabor_id):
    sabor = Sabor.objects.get(id=sabor_id)
    if request.method == 'POST':
        form = Crear_Sabor_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            sabor.nombre = formulario_limpio['nombre']
            sabor.save()
            
            return redirect('Sabor')
        
    else:
        form = Crear_Sabor_forms(initial={'nombre': sabor.nombre})

    return render(request, 'App/Actualizar_Sabor.html', {'form': Crear_Sabor_forms})

def actualizar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        form = Crear_Pedido_forms(request.POST)
        
        if form.is_valid(): 
            formulario_limpio = form.cleaned_data
            
            pedido.cliente = formulario_limpio['cliente']
            pedido.fecha = formulario_limpio['fecha']
            pedido.save()
            
            return redirect('Pedido')
        
    else:
        form = Crear_Pedido_forms(initial={'cliente': pedido.cliente, 'fecha': pedido.fecha})

    return render(request, 'App/Actualizar_Pedido.html', {'form': Crear_Pedido_forms})


def elimilar_cliente(request, cliente_id):

    cliente = Cliente.objects.get(id=cliente_id)
    
    cliente.delete()

    return redirect('Cliente')


def elimilar_helado(request, helado_id):

    helado = Helado.objects.get(id=helado_id)
    
    helado.delete()

    return redirect('Helado')

def elimilar_sabor(request, sabor_id):

    sabor = Sabor.objects.get(id=sabor_id)
    
    sabor.delete()

    return redirect('Sabor')

def eliminar_pedido(request, pedido_id):
    
    pedido = Pedido.objects.get(id=pedido_id)
    
    pedido.delete()
    
    return redirect('Pedido')


def registro_usuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso , Bienvenido/a.')
            return render(request, 'App/index.html')
    else:
            form = UserRegisterForm()

    return render(request, 'App/registro.html',{'form':form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            # Autenticación del usuario
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                # Redirige al index con un mensaje de bienvenida
                return render(request, 'App/index.html', {"mensaje": f"Bienvenido {usuario}"})
            else:
                # Si el usuario no es autenticado, muestra un mensaje de error
                messages.error(request, "Error, datos incorrectos")
                return render(request, "App/login.html", {'form': form})
        
        else:
            # Si el formulario no es válido, muestra un mensaje de error
            messages.error(request, "Error, formulario erroneo")
            return render(request, "App/login.html", {'form': form})
    
    # Si la petición es GET, muestra el formulario vacío
    form = AuthenticationForm()
    return render(request, "App/login.html", {'form': form})
    

def logout_request(request):
    logout(request)
    return render(request, "App/index.html", {"mensaje": "Has cerrado sesion exitosamente."})

def politica_privacidad(request):
    return render(request, 'App/Politica_Privacidad.html')

def terminos_condiciones(request):
    return render(request, 'App/Terminos_Condiciones.html')


def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        if nombre and email and mensaje:
            MensajeContacto.objects.create(
            nombre =nombre,
            email =email,
            mensaje =mensaje
            )

            send_mail(
                'Gracias por contactarnos',
                f'Hola {nombre}, hemos recibido tu mensaje y te contactaremos pronto',
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )

            messages.success(request, 'Mensaje enviado exitosamente.')
            return redirect('pagina_de_gracias')
        else:
            messages.error(request, 'Por favor, llene todos los campos.')

    return render(request, 'App/contacto.html')

def pagina_de_gracias(request):
    return render(request, 'App/gracias.html')

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_envio')
    search_fields = ('nombre', 'email')


def listar_mensajes(request):
    mensajes = MensajeContacto.objects.all().order_by('-fecha_envio')
    paginator = Paginator(mensajes, 10)  # Mostrar 10 mensajes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'App/listar_mensajes.html', {'page_obj': page_obj})

def about(request):
    return render(request, 'App/about.html')