import flet as ft

def main(page):

    first_name = ft.TextField()
    last_name = ft.TextField()

    first_name.value = "Juan"
    last_name.value = "Valverde"

    first_name.disabled = True
    last_name.disabled = True
    page.add(first_name, last_name)

    # with columns
    c = ft.Column(controls=[
    first_name,
    last_name
    ])
    c.disabled = True
    page.add(c)

ft.app(target=main)