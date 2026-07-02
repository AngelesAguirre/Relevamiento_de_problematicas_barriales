# Trabajo Integrador Final
# Proyecto: Observatorio Barrial
# Alumna: Ángeles Aguirre

# Diccionario con categorías y subcategorías disponibles
Categorias = {
    "1": {"Nombre": "Alumbrado y señalización",
          "Subcategorias": ["Luminaria quemada",
                            "Semáforo vehicular",
                            "Semáforo peatonal",
                            "Cables caídos"]},
    "2": {"Nombre": "Veredas y accesibilidad",
          "Subcategorias": ["Rampa rota",
                            "Rampa obstruida",
                            "Cordón roto",
                            "Vereda rota",
                            "Vereda obstruida"]},
    "3": {"Nombre": "Infraestructura vial",
          "Subcategorias": ["Bache",
                            "Calle anegada",
                            "Obstrucción vial",
                            "Carril reducido",
                            "Calzada deteriorada"]},
    "4": {"Nombre": "Higiene urbana",
          "Subcategorias": ["Basural",
                            "Residuos acumulados",
                            "Contenedor desbordado"]}}


# Diccionario con estados posibles del reclamo
Estados = {"1": "Activo",
           "2": "Revisado",
           "3": "En proceso de reparación",
           "4": "Resuelto"}