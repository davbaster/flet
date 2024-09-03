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

    def add_book(e):
        if not title_field.value:
            title_field.error_text = "Por favor ingrese un titulo"
            page.update()
            return
        new_book = ft.ListTile(
            title=ft.Text(title_field.value),
            subtitle=ft.Text(author_field.value if author_field.value else "Autor desconocido"),
            trailing=ft.PopupMenuButton(
                icon=ft.icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(text="Eliminar",
                                       on_click=lambda _: book_view.controls.remove(new_book) or
                                        page.update()), 
                ],
            ),
        )
        book_view.controls.append(new_book)
        title_field.value = ""
        author_field.value = ""
        title_field.error_text = None
        page.update()

    title_field = ft.TextField(label="Titulo del libro", width=300)
    author_field = ft.TextField(label="Autor", width=300)
    add_button = ft.ElevatedButton("Añadir nuevo libro", on_click=add_book)
    add_book_view = ft.Column([
                                ft.Text("Añadir nuevo libro", size=20, weight=ft.FontWeight.BOLD),
                                        title_field,
                                        author_field,
                                        add_button,
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
    
    page.add(app_bar, ft.Row([rail, ft.VerticalDivider(width=1), content], expand=True))

ft.app(target=main) 