import flet as ft
import random

def main (page: ft.page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Tabs on flet"
    page.horizontal_aligment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Ejemplo de tabs en flet ", size = 24, color=ft.colors.WHITE)

    def generar_tareas():
        tareas = ["Hacer la compra", "Llamar al medico", "Estudiar para el examen",
                  "Hacer ejercicio", "Leer un libro", "Preparar la cena"]
        
        #return [random.sample(tareas) for _ in range(5)]
        return random.sample(tareas, 4) 
    

    #vista
    lista_tareas = ft.ListView(spacing=10, padding=20)

    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas():
            lista_tareas.controls.append(ft.Text(tarea, color=ft.colors.WHITE))
        page.update()

    actualizar_tareas()
    boton_actualizar = ft.ElevatedButton( "Actualizar Tareas", on_click= lambda _: actualizar_tareas())
    contenido_tareas = ft.Column([lista_tareas, boton_actualizar])

    #contenido para la pesta;a perfil
    campo_nombre = ft.TextField( label="Nombre: ", bgcolor=ft.colors.BLUE_GREY_700)
    campo_email = ft.TextField( label="Email: ", bgcolor=ft.colors.BLUE_GREY_700)
    boton_guardar = ft.ElevatedButton( "Guardar Perfil")
    contenido_perfil = ft.Column( [campo_nombre, campo_email, boton_guardar])

    #contenido para la pesta;a de configuracion
    switch_notificaciones = ft.Switch(label="Notificaciones", value=True)
    slider_volumen = ft.Slider(min=0, max=100, divisions=10, label="Volumen")
    contenido_config = ft.Column([switch_notificaciones, slider_volumen])

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tareas", icon=ft.icons.LIST_ALT, content=contenido_tareas),
            ft.Tab(text="Perfil", icon=ft.icons.PERSON, content=contenido_perfil),
            ft.Tab(text="Configuracion", icon=ft.icons.SETTINGS),
        ],
        expand=1
    )

    page.add(titulo, tabs)

ft.app(target=main)