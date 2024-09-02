import flet as ft

def main (page: ft.page):
    page.title = "Mi Biblioteca Personal"
    page.theme_mode = ft.ThemeMode.DARK


    def change_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        theme_icon_button.icon = ft.icons.DARK_MODE if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE
        page.update()

    theme_icon_button = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,
        tooltip="Cambiar tema",
        on_click=change_theme,
    )

    titulo = ft.Text("Biblioteca Personal")

    app_bar = ft.AppBar(
        title=titulo,
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[theme_icon_button],
    )

    #vistas
    book_view = ft.ListView(expand=1, spacing=10, padding=20)
    wishlist_view = ft.ListView(expand=1, spacing=10, padding=20)

    title_field = ft.TextField(label="Titulo del libro", width=300)
    author_field = ft.TextField(label="Autor", width=300)
    add_book_view = ft.Column([
                                ft.Text("Añadir nuevo libro", size=20, weight=ft.FontWeight.BOLD),
                                        title_field,
                                        author_field
                                        ], spacing=20
                             )

    #action del indice
    def destination_change(e):
        index = e.control.selected_index
        content.controls.clear()
        if index == 0:
            content.controls.append(book_view)
        elif index == 1:
            content.controls.append(add_book_view)
        elif index == 2:
            content.controls.append(wishlist_view)
        page.update()

    #menu izquierdo
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.BOOK, label="Mis Libros"),
            ft.NavigationRailDestination(icon=ft.icons.ADD, label="Añadir Libro"),
            ft.NavigationRailDestination(icon=ft.icons.FAVORITE, label="Lista de Deseos"),
            ],
        on_change=destination_change, 
    )

    #columna donde se va a mostrar el bookview
    content = ft.Column([book_view], expand=True)
    
    page.add(app_bar, rail)

ft.app(target=main)