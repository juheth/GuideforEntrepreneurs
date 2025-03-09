import datetime

print("")
print("╔════════════════════════════════════════════════╗")
print("║                                                ║")
print("║               B I E N V E N I D O              ║")
print("║                                                ║")
print("╚════════════════════════════════════════════════╝")
print("")
contactos = {}
# Base de datos de usuarios y contraseñas (y ahora roles)
# Base de datos de usuarios y contraseñas (inicialización)
base_de_datos = {
    "admin": {"contraseña": "admin123", "rol": "administrador"},
    "usuario": {"contraseña": "usuario123", "rol": "usuario"},
    
}


# Inicio de sesión modificado
def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    usuario = input("Usuario → ").strip()
    contraseña = input("Contraseña → ").strip()

    if usuario in base_de_datos and base_de_datos[usuario]["contraseña"] == contraseña:
        rol = base_de_datos[usuario]["rol"]
        print(f"ACCESO OTORGADO ✓\nRol: {rol}\n")
        print("╔════════════════════════════════════════════════╗")
        print("║                                                ║")
        print("║               B I E N V E N I D O              ║")
        print("║                                                ║")
        print("╚════════════════════════════════════════════════╝")
        return rol  # Regresamos el rol del usuario para saber si es administrador
    else:
        print("ACCESO DENEGADO ✗")
        print("\n------------------------------------------------------------------")
        print("  ¡ERROR! Por favor, digita correctamente tu usuario o contraseña  ")
        print("------------------------------------------------------------------\n")
        return None
    
# Función para registrar un usuario normal
def registrar_usuario():
    print("\n--- REGISTRAR USUARIO ---")
    usuario = input("Nuevo nombre de usuario → ").strip()
    if usuario in base_de_datos:
        print("⚠️ El usuario ya existe. Intenta con otro nombre.")
        return
    
    contraseña = input("Nueva contraseña → ").strip()
    base_de_datos[usuario] = {"contraseña": contraseña, "rol": "usuario"}
    print(f"🎉 ¡Usuario {usuario} registrado con éxito! Ahora eres un usuario regular.")

# Función para registrar un administrador
def registrar_usuario_administrador():
    print("\n--- REGISTRAR ADMINISTRADOR ---")
    usuario = input("Nuevo nombre de administrador → ").strip()
    if usuario in base_de_datos:
        print("⚠️ El administrador ya existe. Intenta con otro nombre.")
        return
    
    contraseña = input("Nueva contraseña de administrador → ").strip()
    base_de_datos[usuario] = {"contraseña": contraseña, "rol": "administrador"}
    print(f"🎉 ¡Administrador {usuario} registrado con éxito! Ahora tienes acceso a opciones avanzadas.")


# Función para eliminar guía
def eliminar_guia():
    mostrar_guias()
    try:
        indice = int(input("\nIngrese el número de la guía que desea eliminar: ")) - 1
        if 0 <= indice < len(biblioteca):
            guia_eliminada = biblioteca.pop(indice)
            print(f"✅ Guía '{guia_eliminada['titulo']}' eliminada con éxito.")
        else:
            print("⚠️ Índice fuera de rango.")
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")

# Consulta de vacantes
ofertas = [
    {"titulo": "Desarrollador Web", "empresa": "TechCorp", "ubicacion": "Madrid", "descripcion": "Programación de páginas web"},
    {"titulo": "Diseñador Gráfico", "empresa": "CreativeStudio", "ubicacion": "Barranquilla", "descripcion": "Diseño de logos y publicidad"},
    {"titulo": "Vendedor", "empresa": "ComercialPro", "ubicacion": "Cartagena", "descripcion": "Atención a clientes y ventas"}
]

def mostrar_ofertas():
    print("\n=== OFERTAS DISPONIBLES ===")
    for i, oferta in enumerate(ofertas, 1):
        print(f"\nOferta #{i}:")
        print(f"Puesto: {oferta['titulo']}")
        print(f"Empresa: {oferta['empresa']}")
        print(f"Ubicación: {oferta['ubicacion']}")
        print(f"Descripción: {oferta['descripcion']}")
        print("-" * 30)
    input("\nPresiona Enter para continuar...")

def buscar_ofertas():
    busqueda = input("\nIntroduce el término a buscar: ").lower()
    print("\n= RESULTADOS DE LA BÚSQUEDA =")
    encontrado = False

    for oferta in ofertas:
        if (busqueda in oferta['titulo'].lower() or busqueda in oferta['empresa'].lower() or busqueda in oferta['ubicacion'].lower()):
            print(f"\nPuesto: {oferta['titulo']}")
            print(f"Empresa: {oferta['empresa']}")
            print(f"Ubicación: {oferta['ubicacion']}")
            print(f"Descripción: {oferta['descripcion']}")
            print("-" * 30)
            encontrado = True

    if not encontrado:
        print("No se encontraron ofertas que coincidan con tu búsqueda.")
    input("\nPresiona Enter para continuar...")

# Emprende tu propio negocio
def analizar_habilidades():
    habilidades = []
    print("\n🔍 Paso 1: Descubre tus habilidades y fortalezas")
    print("Escribe tus habilidades actuales. Ejemplo: comunicación, diseño gráfico, ventas, programación.")
    print("Cuando termines, escribe 'listo'.")
    
    while True:
        habilidad = input("Habilidad: ").strip()
        if habilidad.lower() == 'listo':
            break
        if habilidad:
            habilidades.append(habilidad)
        else:
            print("⚠️ Por favor, ingresa una habilidad válida.")
    
    if habilidades:
        print("\n✅ Tus habilidades principales son:")
        for i, h in enumerate(habilidades, 1):
            print(f"{i}. {h}")
    else:
        print("\n⚠️ No ingresaste habilidades. Intenta nuevamente.")
    return habilidades

def crear_idea_negocio(habilidades):
    print("\n💡 Paso 2: Crea tu idea de negocio")
    if not habilidades:
        print("⚠️ Necesitas identificar tus habilidades antes de continuar.")
        return ""
    print("Piensa en cómo combinar tus habilidades con necesidades del mercado.")
    mercado = input("¿Qué mercado o industria te interesa (tecnología, comida, moda, etc.)? :").strip()
    idea = input(f"Basándote en '{mercado}', describe tu idea de negocio: ").strip()
    print(f"\n🎯 Tu idea de negocio: {idea}")
    return idea

# Biblioteca Virtual: Educación Financiera
biblioteca = [
    {
        "titulo": "1. Cómo crear un plan de negocios",
        "resumen": "Aprende a estructurar y desarrollar un plan de negocios efectivo que te permita establecer una base sólida para tu emprendimiento.\n Desde la definición de objetivos hasta la identificación de oportunidades, esta guía te llevará paso a paso hacia el éxito empresarial."
    },
    {
        "titulo": "2. Finanzas personales para emprendedores",
        "resumen": "Descubre estrategias prácticas para gestionar tus finanzas personales mientras construyes tu empresa.\n Aprende a equilibrar ingresos, gastos y ahorros, asegurando la estabilidad económica que necesitas para lograr tus metas."
    },
    {
        "titulo": "3. Marketing digital básico",
        "resumen": "Sumérgete en el mundo del marketing digital y explora las herramientas fundamentales para promocionar tu negocio en línea.\n Aprende a captar la atención de tus clientes y a construir una presencia digital efectiva."
    },
    {
        "titulo": "4. Cómo gestionar un equipo pequeño",
        "resumen": "Desarrolla las habilidades necesarias para liderar y motivar equipos en pequeñas empresas. Descubre cómo fomentar la colaboración,\n resolver conflictos y alcanzar objetivos comunes con éxito."
    },
    {
        "titulo": "5. Herramientas para trabajar desde casa",
        "resumen": "Optimiza tu productividad con esta guía que reúne las mejores aplicaciones,\n técnicas y consejos para trabajar desde casa de manera eficiente y sin distracciones."
    }
]

def mostrar_guias():
    print("\n=== Guías disponibles ===")
    for guia in biblioteca:
        print(f"{guia['titulo']}")
        print(f"Resumen: {guia['resumen']}")
        print("-" * 30)
    print("=========================")
    
def buscar_por_categoria(categoria):
    print(f"\nGuías en la categoría '{categoria}':")
    encontrado = False
    for guia in biblioteca:
        if guia["categoria"].lower() == categoria.lower():
            print(f"- {guia['titulo']} - {guia['autor']}")
            encontrado = True
    if not encontrado:
        print("No se encontraron guías en esta categoría.")

def agregar_guia():
    print("\nAgregar nueva guía:")
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoría (Principiantes/Intermedios/Avanzados): ")
    biblioteca.append({"titulo": titulo, "autor": autor, "categoria": categoria})
    print("¡Guía agregada exitosamente!")
    
def agregar_vacante():
    print("\n--- AGREGAR VACANTE ---")
    titulo = input("Título del puesto: ")
    empresa = input("Nombre de la empresa: ")
    ubicacion = input("Ubicación: ")
    descripcion = input("Descripción del puesto: ")
    
    # Añadir la nueva vacante a la lista de ofertas
    nuevas_oferta = {
        "titulo": titulo,
        "empresa": empresa,
        "ubicacion": ubicacion,
        "descripcion": descripcion
    }
    ofertas.append(nuevas_oferta)
    print(f"✅ Vacante '{titulo}' agregada con éxito.")
    
    
def eliminar_vacante():
    mostrar_ofertas()
    try:
        indice = int(input("\nIngrese el número de la vacante que desea eliminar: ")) - 1
        if 0 <= indice < len(ofertas):
            vacante_eliminada = ofertas.pop(indice)
            print(f"✅ Vacante '{vacante_eliminada['titulo']}' eliminada con éxito.")
        else:
            print("⚠️ Índice fuera de rango.")
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")

# Gestión de contactos
def gestion_contactos():
    while True:
        print("\n=== Menú de Gestión de Contactos ===")
        print("1. Añadir contacto")
        print("2. Eliminar contacto")
        print("3. Ver contactos")
        print("4. Volver al menú principal")
        
        opcion = input("Selecciona una opción (1-4): ")
    
        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            if nombre in contactos:
                print("⚠️ El contacto ya existe.")
            else:
                telefono = input("Introduce número de teléfono: ")
                contactos[nombre] = telefono
                print(f"✅ Contacto {nombre} añadido con éxito.")
        
        elif opcion == "2":
            nombre = input("Nombre del contacto a eliminar: ")
            if nombre in contactos:
                del contactos[nombre]
                print(f"✅ Contacto {nombre} eliminado con éxito.")
            else:
                print("⚠️ El contacto no existe.")
        
        elif opcion == "3":
            if contactos:
                print("\n📋 Lista de Contactos:")
                for nombre, telefono in contactos.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("⚠️ No hay contactos en la lista.")
        
        elif opcion == "4":
            print("↩️ Volviendo al menú principal...")
            break
        
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")
            
            


# Menú Principal
# Menú Principal
def mostrar_menu_principal(rol):
    while True:
        print("╔════════════════════════════════════════════════╗")
        print("║                                                ║")
        print("║          🌟 BIENVENIDO A TU ASISTENTE 🌟       ║")
        print("║                                                ║")
        print("║          ELIJA LA OPCIÓN DE SU INTERÉS         ║")
        print("║                                                ║")
        print("║  1) Consultar vacantes                         ║")
        print("║  2) Emprende tu propio negocio                 ║")
        print("║  3) Educación financiera                       ║")
        print("║  4) Gestión de contactos                       ║")
        
        if rol == "administrador":  # Solo la empresa puede agregar o eliminar vacantes
            print("║  5) Agregar vacante                            ║")
            print("║  6) Eliminar vacante                          ║")
        
        print("║  7) Salir                                      ║")
        print("║                                                ║")
        print("╚════════════════════════════════════════════════╝")
        
        opcion = input("\nIngrese el número de la opción que desea realizar: ")

        if opcion == "1":
            print("\n=== Menú de Vacantes ===")
            print("1. Ver todas las vacantes")
            print("2. Buscar vacantes")
            print("3. Volver")
            subopcion = input("Elige una opción: ")
            if subopcion == "1":
                mostrar_ofertas()
            elif subopcion == "2":
                buscar_ofertas()
            elif subopcion == "3":
                continue
            else:
                print("⚠️ Opción no válida. Intenta nuevamente.")
        elif opcion == "2":
            print("\n¡Emprende tu propio negocio!")
            habilidades = analizar_habilidades()
            if habilidades:
                crear_idea_negocio(habilidades)
        elif opcion == "3":
            print("\n=== Educación Financiera ===")
            print("1. Ver guías disponibles")
            print("2. Agregar una nueva guía")
            print("3. Eliminar una guía existente")
            print("4. Volver")
            subopcion = input("Elige una opción: ")
            if subopcion == "1":
                mostrar_guias()
            elif subopcion == "2":
                agregar_guia()
            elif subopcion == "3":
                eliminar_guia()
            elif subopcion == "4":
                continue   
            else:
                print("⚠️ Opción no válida.")
        elif opcion == "4":
            print("\nGestiona tus contactos")
            gestion_contactos()
        elif opcion == "5" and rol == "administrador":  # Opción para agregar vacantes solo para empresas
            print("\n--- AGREGAR VACANTE ---")
            titulo = input("Título del puesto: ")
            empresa = input("Nombre de la empresa: ")
            ubicacion = input("Ubicación: ")
            descripcion = input("Descripción del puesto: ")
    
            # Añadir la nueva vacante a la lista de ofertas
            nuevas_oferta = {
                "titulo": titulo,
                "empresa": empresa,
                "ubicacion": ubicacion,
                "descripcion": descripcion
            }
            ofertas.append(nuevas_oferta)
            print(f"✅ Vacante '{titulo}' agregada con éxito.")
        elif opcion == "6" and rol == "administrador":  # Opción de eliminar vacantes solo para empresas
            eliminar_vacante()
        elif opcion == "7":
            print("\n¡Gracias por usar nuestro sistema! ¡Hasta pronto!")
            break
        else:
            print("\n⚠️ Opción no válida. Por favor, selecciona una opción válida.")


    # Programa principal
def main():
    while True:
        print("\n--- MENÚ INICIAL ---")
        print("1. Registrar usuario")
        print("2. Registrar como administrador")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Selecciona una opción → ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_usuario_administrador()
        elif opcion == "3":
            rol = iniciar_sesion()  # Rol de USUARIO REGULAR al iniciar sesion
            if rol:
                if rol == "administrador":
                    mostrar_menu_principal(rol)
                else:
                    mostrar_menu_principal(rol)
        elif opcion == "4":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")
main ()

    # GRACIA PAPADIOOOOOOOOO
    