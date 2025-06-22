# # import flet as ft
# # import time

# # def main(page: ft.Page):
# #     page.title = "uptown stationary shop manager"

# #     page.vertical_aligment = ft.MainAxisAlignment.START
# #     page.vertical_aligment = ft.MainAxisAlignment.CENTER

# #     def add_item_click(e):
# #         print(f"Button clicked! Item name: {item_name_field.value}")
# #         item_name_field.value = ""
# #         page.update()

# #     item_name_field = ft.TextField(
# #         label="Item Name",
# #         hint_text="e.g., Pencil HB",
# #         width="300"
# #     )

# #     add_button = ft.ElevatedButton(
# #         text="Add Item",
# #         on_click=add_item_click
# #     )

# #     layout = ft.Column(
# #         controls=[
# #             ft.Text("Enter New Stationary Item:", size= 20),
# #             item_name_field,
# #             add_button
# #         ],
# #         alignment=ft.MainAxisAlignment.START,
# #         horizontal_alignment=ft.CrossAxisAlignment.CENTER
# #     )

# #     page.add(layout)



# #     hello_text = ft.Text(
# #         value="Hello, Flet",
# #         size=30,
# #         text_align=ft.TextAlign.CENTER,
# #     )

#     # page.add(hello_text)

#     # page.update()
#     # print("Hello from uptown-stationary")



# import flet as ft

# class Item(ft.Container):
#     def __init__(self, name, on_delete):
#         super().__init__(
#             content=ft.Row(
#                 controls=[
#                     ft.Text(name),
#                     ft.IconButton(
#                         icon=ft.Icons.DELETE_OUTLINE,
#                         on_click=lambda e: on_delete(self),
#                     ),
#                 ],
#                 alignment=ft.MainAxisAlignment.START,
#             ),
#             bgcolor=ft.colors.black,
#             padding=15,
#             margin=2,
#             border_radius=5,
#         )

# class StationeryApp(ft.Container):
#     def __init__(self):
#         super().__init__(
#             content=ft.Column(
#                 controls=[
#                     ft.TextField(hint_text="Enter item name", expand=True),
#                     ft.ElevatedButton("Add Item", on_click=self.add_item),
#                     ft.Column(),
#                 ],
#                 alignment=ft.MainAxisAlignment.START,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             ),
#             bgcolor=ft.colors.WHITE,
#             padding=15,
#             margin=15,
#             border_radius=15,
#         )
#         self.items = []

#     def add_item(self, e):
#         item_name = self.container[0].value.strip()
#         if item_name:
#             item = Item(item_name, self.remove_item)
#             self.items.append(item)
#             self.controls[2].controls.append(item)
#             self.controls[0].value = ""
#             self.update()

#     def remove_item(self, item):
#         self.items.remove(item)
#         self.controls[2].controls.remove(item)
#         self.update()

# def main(page: ft.Page):
#     page.title = "Uptown Stationery Shop Manager"
#     page.bgcolor = ft.colors.BLACK
#     page.add(StationeryApp())

# ft.app(target=main)

import flet as ft

class Item(ft.Container):
    def __init__(self, name, on_delete):
        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Text(name),
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        on_click=lambda e: on_delete(self),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            bgcolor=ft.colors.LIGHT_BLUE_50,
            padding=15,
            margin=2,
            border_radius=5,
        )

class StationeryApp(ft.Container):
    def __init__(self):
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.TextField(hint_text="Enter item name", expand=True),
                    ft.ElevatedButton("Add Item", on_click=self.add_item),
                    ft.Column(),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.WHITE,
            padding=15,
            margin=15,
            border_radius=15,
        )
        self.items = []

    def add_item(self, e):
        item_name = self.container[0].value.strip()
        if item_name:
            item = Item(item_name, self.remove_item)
            self.items.append(item)
            self.controls[2].controls.append(item)
            self.controls[0].value = ""
            self.update()

    def remove_item(self, item):
        self.items.remove(item)
        self.controls[2].controls.remove(item)
        self.update()

def main(page: ft.Page):
    page.title = "Uptown Stationery Shop Manager"
    page.bgcolor = ft.colors.LIGHT_BLUE_100
    page.add(StationeryApp())

ft.app(target=main)
