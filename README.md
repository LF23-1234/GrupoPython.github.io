📌 FitElitePro – Web Fitness Management System

FitnessPro es una aplicación web desarrollada con Django que permite gestionar usuarios, entrenadores, hábitos saludables y contenido informativo relacionado con fitness.
Este proyecto forma parte del Proyecto Final de Programación Web.

📚 Tabla de Contenidos

1- Caracteristicas
2- Tecnologias
3- Estructura
4- Instalación
5- Administrador
6- Créditos
7- Licencia

⭐ Características Principales
🔐 Autenticación

1- Registro de usuarios
2- Login / Logout
3- Perfil personal

🧑‍🏫 Sección de Entrenadores

1- Página de trainers
2- Información y especialidades

🥗 Hábitos Saludables

1- Recomendaciones y rutinas

📚 Artículos Informativos

1- Contenido educativo sobre salud y fitness

📞 Contacto

1- Formulario básico de contacto

🎨 Plantillas Modulares

1- base.html
2- Includes (header.html, footer.html)
3- Carpetas organizadas por secciones

🛠 Tecnologías Utilizadas

1- Python 3.14
2- Django 6.0
3- HTML5 / CSS3
4- JavaScript
5- Bootstrap
6- SQLite3

📁 Estructura del Proyecto
FitnesPro/
│
├── fitness_project/          # Configuración principal
│
├── fitness_app/              # Aplicación principal
│   ├── static/
│   ├── templates/
│   │   ├── fitness_app/      # Vistas del sistema
│   │   ├── includes/         # Header y footer
│   │   └── registration/     # Login y registro
│
├── db.sqlite3
├── manage.py
└── venv/

⚙ Instalación y Ejecución
1️⃣ Clonar el repositorio
git clone <url-del-repositorio>
cd FitnesPro

2️⃣ Crear entorno virtual
python -m venv venv

3️⃣ Activar entorno

En Windows:

venv\Scripts\activate

En Linux/Mac:

source venv/bin/activate

4️⃣ Instalar dependencias
pip install -r requirements.txt

5️⃣ Migraciones
python manage.py migrate

6️⃣ Ejecutar servidor
python manage.py runserver

Visita:

http://127.0.0.1:8000/

🔑 Usuario Administrador (Opcional)
python manage.py createsuperuser

Acceso al panel:

http://127.0.0.1:8000/admin/

👨‍💻 Créditos

Proyecto desarrollado por Luis Felipe 23-1234 y Penelope Minaya 23-0348
Asignatura: Programación Web I
Framework: Django

📜 Licencia

Este proyecto es de uso académico.
Puede ser modificado libremente para fines educativos.
