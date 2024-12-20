from django.urls import path
from App import views

urlpatterns = [
    path('', views.mostrar_index, name='Home'),
    path('cliente/', views.mostrar_cliente, name='Cliente'),
    path('helado/', views.mostrar_helado, name='Helado'),
    path('sabor/', views.mostrar_sabor, name='Sabor'),
    path('pedido/', views.mostrar_pedido, name='Pedido'),
    path('crear_cliente/', views.crear_cliente, name= 'Crear Cliente'),
    path('crear_helado/', views.crear_helado, name='Crear Helado'),
    path('crear_sabor/', views.crear_sabor, name='Crear Sabor'),
    path('crear_pedido/', views.crear_pedido, name='Crear Pedido'),
    path('buscar_cliente/', views.buscar_cliente, name='Buscar Cliente'),
    path('buscar_helado/', views.buscar_helado, name='Buscar Helado'),
    path('buscar_sabor/', views.buscar_sabor, name='Buscar Sabor'),
    path('buscar_pedido/', views.buscar_pedido, name='Buscar Pedido'),
    path('actualizar_cliente/<cliente_id>/', views.actualizar_cliente, name='Actualizar Cliente'),
    path('actualizar_helado/<helado_id>/', views.actualizar_helado, name='Actualizar Helado'),
    path('actualizar_sabor/<sabor_id>/', views.actualizar_sabor, name='Actualizar Sabor'),
    path('actualizar_pedido/<pedido_id>/', views.actualizar_pedido, name='Actualizar Pedido'),
    path('eliminar_cliente/<cliente_id>/', views.elimilar_cliente, name='Eliminar Cliente'),
    path('eliminar_helado/<helado_id>/', views.elimilar_helado, name='Eliminar Helado'),
    path('eliminar_sabor/<sabor_id>/', views.elimilar_sabor, name='Eliminar Sabor'),
    path('eliminar_pedido/<pedido_id>/', views.eliminar_pedido, name='Eliminar Pedido'),
    path('registro/', views.registro_usuario, name='Registro'),
    path('login/', views.login_request, name = 'Login'),
    path('logout/', views.logout_request, name = 'Logout'),
    path('politica_privacidad/', views.politica_privacidad, name= 'Politica Privacidad'),
    path('terminos_condiciones/', views.terminos_condiciones, name= 'Terminos Condiciones'),
    path('contacto/', views.contacto, name='contacto'),
    path('gracias/', views.pagina_de_gracias, name='pagina_de_gracias'),
    path('mensajes/', views.listar_mensajes, name='lista_mensajes'),
    path('about/',views.about, name='sobre_nosotros'),
]
