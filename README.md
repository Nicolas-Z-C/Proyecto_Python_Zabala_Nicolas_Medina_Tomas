# Proyecto Python - Campuslands ERP
## Sistema de Gestión de Datos Académicos

**Autores:** 
- Tomás Felipe Medina Prada
- Nicolás Zabala Castañeda

**Fecha:** 25 de Agosto de 2025

---

## 📖 Descripción

Sistema ERP (Enterprise Resource Planning) desarrollado en Python para la gestión integral de datos académicos en Campuslands. Este proyecto permite administrar de manera eficiente la información académica, incluyendo estudiantes, cursos, profesores y recursos educativos.

## 🎯 Objetivos

- Desarrollar un sistema de gestión académica completo
- Implementar funcionalidades CRUD para entidades académicas
- Proporcionar una interfaz intuitiva para la administración de datos
- Garantizar la integridad y seguridad de la información académica

## 🚀 Características Principales

- **Gestión de Estudiantes**: Registro, actualización y consulta de información estudiantil
- **Administración de Cursos**: Control de materias, horarios y contenidos académicos
- **Gestión de Profesores**: Administración del personal docente y sus asignaciones
- **Reportes Académicos**: Generación de reportes y estadísticas
- **Base de Datos**: Almacenamiento seguro y estructurado de información
- **Interfaz de Usuario**: Sistema amigable para la interacción con los datos

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Base de Datos**: SQLite/MySQL
- **Framework**: Flask/Django (según implementación)
- **Interfaz**: HTML/CSS/JavaScript
- **Librerías**: 
  - pandas (para manejo de datos)
  - sqlite3/mysql-connector (conexión BD)
  - datetime (manejo de fechas)
  - json (manejo de datos JSON)

## 📋 Requisitos Previos

```bash
Python 3.8 o superior
pip (gestor de paquetes de Python)
```

## ⚙️ Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Nicolas-Z-C/Proyecto_Python_Zabala_Nicolas_Medina_Tomas.git
cd Proyecto_Python_Zabala_Nicolas_Medina_Tomas
```

2. **Crear entorno virtual** (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**
```bash
python setup_database.py
```

## 🚀 Uso

1. **Ejecutar la aplicación**
```bash
python main.py
```

2. **Acceder al sistema**
- Abrir navegador en `http://localhost:5000`
- Utilizar credenciales de administrador por defecto

## 📁 Estructura del Proyecto

```
Proyecto_Python_Zabala_Nicolas_Medina_Tomas/
├── src/
│   ├── models/          # Modelos de datos
│   ├── controllers/     # Lógica de negocio
│   ├── views/          # Interfaces de usuario
│   └── utils/          # Utilidades y helpers
├── database/
│   └── migrations/     # Scripts de base de datos
├── static/
│   ├── css/           # Estilos
│   ├── js/            # JavaScript
│   └── images/        # Recursos gráficos
├── templates/         # Plantillas HTML
├── tests/            # Pruebas unitarias
├── docs/             # Documentación
├── requirements.txt  # Dependencias
├── main.py          # Archivo principal
└── README.md        # Este archivo
```

## 🧪 Pruebas

Ejecutar las pruebas unitarias:
```bash
python -m pytest tests/
```

## 📊 Funcionalidades

### Módulo de Estudiantes
- ✅ Registro de nuevos estudiantes
- ✅ Actualización de información personal
- ✅ Consulta de historiales académicos
- ✅ Gestión de matriculación

### Módulo de Cursos
- ✅ Creación y edición de cursos
- ✅ Asignación de profesores
- ✅ Programación de horarios
- ✅ Gestión de contenidos

### Módulo de Profesores
- ✅ Registro de docentes
- ✅ Asignación de materias
- ✅ Seguimiento de desempeño
- ✅ Gestión de horarios

### Reportes y Analytics
- ✅ Reportes de rendimiento académico
- ✅ Estadísticas de inscripciones
- ✅ Análisis de datos académicos
- ✅ Exportación de información

## 🤝 Contribuciones

1. Fork del proyecto
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📞 Contacto

- **Tomás Felipe Medina Prada** - [GitHub](https://github.com/)
- **Nicolás Zabala Castañeda** - [GitHub](https://github.com/Nicolas-Z-C)

**Link del Proyecto**: [https://github.com/Nicolas-Z-C/Proyecto_Python_Zabala_Nicolas_Medina_Tomas](https://github.com/Nicolas-Z-C/Proyecto_Python_Zabala_Nicolas_Medina_Tomas)

## Agradecimientos

- Campuslands por el apoyo en el desarrollo del proyecto
- Comunidad de Python por las herramientas y recursos
- Profesores y mentores que guiaron el proceso de aprendizaje

---

*Desarrollado con ❤️ por Tomás Felipe Medina Prada y Nicolás Zabala Castañeda*

