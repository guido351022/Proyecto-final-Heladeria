# heladeria_piculichi
Este es un proyecto desarrollado en Django que permite gestionar funcionalidades relacionadas con la administración de la heladeria. A continuación, se presenta el orden recomendado para probar las funcionalidades principales y dónde encontrarlas.

⚙️ Instalación y Configuración
1. Clonar el Repositorio
Clona el repositorio y accede al directorio del proyecto:

git clone <URL_DEL_REPOSITORIO>
cd heladeria_piculichi

# Crear y Activar el Entorno Virtual
Crea un entorno virtual y actívalo:

python -m venv (TU ENTORNO)

# En Windows:
venv\Scripts\activate

# En MacOS/Linux:
source venv/bin/activate

# Instalar Dependencias
Instala las dependencias necesarias:

pip install django
pip install mysqlclient pymysql
pip install django-crispy-forms
pip install crispy-bootstrap5

Alternativa si usas otro conector de MySQL:
pip install mysql-connector-python

# Configurar la Base de Datos
Asegúrate de que la configuración de la base de datos en settings.py sea correcta para tu entorno de desarrollo.

# Realizar Migraciones
Ejecuta las migraciones para preparar la base de datos:

python manage.py migrate

# Crear un Superusuario
Para acceder al panel de administración, crea un superusuario:

python manage.py createsuperuser

# Ejecutar el Servidor
Finalmente, inicia el servidor local para probar la aplicación:

python manage.py runserver

# 🚀 Funcionalidades Principales
Gestión de Pacientes: CRUD de la heladeria con información relevante: Programación y modificación de citas médicas.
Administración de Personal: .

# 📌 Nota
Este proyecto es una versión básica enfocada en la administración de una heladeria. Para soporte adicional o para contribuir, por favor, abre un Issue o un Pull Request.

¡Gracias por usar heladeria piculichi!
