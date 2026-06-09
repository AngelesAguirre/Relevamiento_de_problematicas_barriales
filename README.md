# Observatorio Barrial

## Sistema de Registro de Problemáticas Urbanas

### Descripción

**Observatorio Barrial** es un proyecto desarrollado en Python con el objetivo de registrar, organizar y gestionar problemáticas barriales vinculadas a deficiencias estructurales presentes en el espacio público.

La herramienta permite almacenar incidencias urbanas clasificadas por categorías y ubicación territorial, generando una base de datos estructurada que puede ser consultada, administrada y ampliada posteriormente.

El proyecto surge como Trabajo Integrador Final (TIF) del curso **Introducción a la Programación con Python**, adaptando los contenidos vistos durante la cursada a una temática relacionada con las Ciencias Sociales, la gestión territorial y el análisis de problemáticas urbanas.

---

## Objetivos del proyecto

* Registrar problemáticas detectadas en el espacio público.
* Clasificar incidencias según categorías y subcategorías.
* Organizar la información mediante estructuras de datos.
* Permitir la búsqueda, visualización y eliminación de registros.
* Aplicar herramientas básicas de programación en Python a una problemática social concreta.
* Sentar las bases para futuras ampliaciones orientadas al análisis territorial.

---

## Problemáticas contempladas

Actualmente el sistema permite registrar incidencias agrupadas en las siguientes categorías:

### Alumbrado y señalización

* Luminaria quemada
* Semáforo vehicular
* Semáforo peatonal
* Cables caídos

### Veredas y accesibilidad

* Rampa rota
* Rampa obstruida
* Cordón roto
* Vereda rota
* Vereda obstruida

### Infraestructura vial

* Bache
* Calle anegada
* Obstrucción vial
* Carril reducido
* Calzada deteriorada

### Higiene urbana

* Basural
* Residuos acumulados
* Contenedor desbordado

---

## Información registrada

Cada reclamo almacena la siguiente información:

* Categoría
* Subcategoría
* Provincia
* Municipio o partido
* Calle
* Altura

La información es almacenada mediante diccionarios y posteriormente incorporada a una lista principal que funciona como base de datos temporal del sistema.

---

## Funcionalidades actuales

### Carga de reclamos

Permite registrar nuevas incidencias urbanas mediante un sistema guiado de categorías y subcategorías.

### Visualización de reclamos

Permite consultar todos los registros almacenados durante la ejecución del programa.

### Búsqueda de reclamos

Permite localizar incidencias utilizando palabras clave relacionadas con:

* categoría;
* subcategoría;
* provincia;
* municipio;
* calle;
* altura.

### Eliminación de reclamos

Permite eliminar registros específicos previamente almacenados.

### Menú interactivo

Utiliza estructuras repetitivas para permitir múltiples operaciones durante una misma sesión.

---

## Herramientas de Python utilizadas

El proyecto fue desarrollado utilizando conceptos fundamentales trabajados durante el curso:

* Variables
* Funciones (`def`)
* Listas
* Diccionarios
* Diccionarios dentro de diccionarios
* Condicionales (`if`, `elif`, `else`)
* Bucles (`for`, `while`)
* Métodos de cadenas (`strip()`, `title()`, `lower()`)
* Validación de datos (`isdigit()`)
* Métodos de listas (`append()`, `pop()`)

---

## Posibles mejoras futuras

El proyecto fue concebido desde el inicio con posibilidades de expansión. Entre las mejoras consideradas se encuentran:

* Incorporación de fechas de relevamiento.
* Persistencia de datos mediante archivos CSV o bases de datos.
* Georreferenciación de incidencias.
* Visualización de problemáticas sobre mapas.
* Generación de estadísticas por categorías y zonas.
* Elaboración de reportes territoriales automatizados.
* Exportación de información para análisis posteriores.

---

## Contexto académico

Este proyecto fue desarrollado como parte del Trabajo Integrador Final de la asignatura **Introducción a la Programación con Python**, aplicando herramientas básicas de programación a una problemática vinculada con la gestión territorial y el relevamiento de deficiencias urbanas.

---

## Autoría

**Ángeles Aguirre**

Estudiante de Ciencia Política

Universidad de Buenos Aires (UBA)
