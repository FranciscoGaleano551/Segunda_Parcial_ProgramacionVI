import flet as ft

# Definir una contraseña fija
CONTRASENA_CORRECTA = "Fran12345"  # Cambia esto a la contraseña que desees

# Lista para almacenar los nombres y edades
lista_entradas = []

# Función para procesar los datos ingresados por el usuario
def procesar_datos(nombre, edad, resultado):
    try:
        edad = int(edad)
        if edad >= 18:
            mensaje = f"Hola {nombre}, eres mayor de edad."
        else:
            mensaje = f"Hola {nombre}, eres menor de edad."
        
        # Agregar la entrada a la lista
        lista_entradas.append((nombre, edad))
        
        # Actualizar la lista de entradas en la interfaz
        actualizar_lista()

        resultado.value = mensaje
        resultado.update()
    except ValueError:
        resultado.value = "Por favor, ingresa una edad válida (número)."
        resultado.update()

def actualizar_lista():
    # Limpiar la lista actual
    lista_resultados.value = ""
    # Agregar las entradas de la lista a la visualización
    for nombre, edad in lista_entradas:
        lista_resultados.value += f"{nombre} - {edad} años\n"
    lista_resultados.update()

# Función para mostrar la sección de verificación de edad
def mostrar_verificacion_de_edad(page):
    # Limpiar la página
    page.clean()

    # Campo de entrada para el nombre
    nombre_input = ft.TextField(label="Nombre", width=200)
    
    # Campo de entrada para la edad
    edad_input = ft.TextField(label="Edad", width=200)
    
    # Campo de texto para mostrar el resultado
    resultado = ft.Text(value="", color="black")
    
    # Botón para procesar los datos
    boton_procesar = ft.ElevatedButton(
        text="Procesar",
        on_click=lambda e: procesar_datos(nombre_input.value, edad_input.value, resultado),
    )

    # Botón para limpiar los campos
    def limpiar_campos(e):
        nombre_input.value = ""
        edad_input.value = ""
        resultado.value = ""
        nombre_input.update()
        edad_input.update()
        resultado.update()

    boton_limpiar = ft.ElevatedButton(
        text="Limpiar",
        on_click=limpiar_campos
    )

    # Botón para salir y volver a la pantalla de inicio de sesión
    def salir(e):
        page.clean()
        main(page)  # Regresar a la función principal para mostrar el inicio de sesión

    boton_salir = ft.ElevatedButton(
        text="Salir",
        on_click=salir
    )

    # Crear una columna para el formulario
    columna_formulario = ft.Column(
        controls=[
            ft.Text("BIENVENIDO A LA APLICACION PARA VERIFICAR LA EDAD", size=30, color="black"),
            nombre_input,
            edad_input,
            ft.Row(
                controls=[boton_procesar, boton_limpiar, boton_salir],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            resultado,
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    # Crear una columna para mostrar las entradas
    global lista_resultados
    lista_resultados = ft.Text(value="", color="black", size=14)

    columna_lista = ft.Column(
        controls=[
            ft.Text("Entradas:", size=20, color="black"),
            lista_resultados
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    # Agregar las columnas en un Row
    page.add(
        ft.Row(
            controls=[columna_formulario, columna_lista],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50  # Espacio entre las columnas
        )
    )

    # Centrar verticalmente el contenido
    page.vertical_alignment = ft.MainAxisAlignment.START  # Coloca el contenido en la parte superior

# Función principal que crea la interfaz de usuario
def main(page: ft.Page):
    page.title = "SEGUNDA PARCIAL"
    
    # Crear un contenedor para el fondo celeste
    fondo = ft.Container(
        width=page.width,
        height=page.height,
        bgcolor="lightblue"
    )

    # Crear un contenedor para la imagen de fondo
    imagen_fondo = ft.Image(
        src="C:\\Users\\TOSHIBA\\P6 Python - Francisco Galeano\\Logo.JPG", 
        width=400, height=300
    )

    # Crear un contenedor para el contenido centrado
    usuario_input = ft.TextField(label="Usuario", width=250)
    contrasena_input = ft.TextField(label="Contraseña", width=250, password=True)
    mensaje_error = ft.Text(value="", color="red")  # Mensaje de error

    contenido = ft.Column(
        controls=[
            imagen_fondo,  # Imagen en la parte superior
            ft.Text("Iniciar Sesión", size=24, color="black"),
            usuario_input,
            contrasena_input,
            ft.Row(
                controls=[ft.Checkbox(label="Recordar contraseña")],
                alignment=ft.MainAxisAlignment.CENTER  # Centrar el checkbox
            ),
            ft.ElevatedButton(
                text="Iniciar",
                on_click=lambda e: verificar_contrasena(page, contrasena_input.value, mensaje_error)
            ),
            mensaje_error
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    # Usar Stack para superponer el fondo y el contenido
    page.add(
        ft.Stack(
            [
                fondo,  # Fondo de color celeste
                contenido  # Contenido del inicio de sesión
            ]
        )
    )

    # Actualizar la página para mostrar los cambios
    page.update()

# Función para verificar la contraseña ingresada
def verificar_contrasena(page, contrasena, mensaje_error):
    if contrasena == CONTRASENA_CORRECTA:
        mensaje_error.value = ""  # Limpiar el mensaje de error
        mostrar_verificacion_de_edad(page)
    else:
        mensaje_error.value = "Contraseña incorrecta. Intenta nuevamente."
        mensaje_error.update()

# Ejecutar la aplicación
ft.app(target=main)

































