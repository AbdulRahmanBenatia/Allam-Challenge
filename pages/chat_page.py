import flet as ft
from ibm_API import get_response
from utils import Text, SMALL_BTN_SIZE, BACK_BTN_STYLE

def load_page4(page: ft.Page, navigate_to):
    page.clean()

    back_button = ft.ElevatedButton(content=Text("رجوع", size=SMALL_BTN_SIZE), style=BACK_BTN_STYLE, on_click=lambda _: navigate_to("الصفحة الرئيسية"),  width=100, opacity=0.5)
    output_label = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)

    def on_submit(e):
        prompt = text_box.value
        print("PRESSED")
        response = get_response(prompt=prompt)
        print(response)
        output_label.value = response
        page.update()
        page.update()

    text_box = ft.TextField(
        label="اكتب سؤالك هنا",
        text_align=ft.TextAlign.RIGHT,
        on_submit=on_submit,
        multiline=True
    )

    content_column = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        expand=True
    )
    
    content_column.controls.extend([
        ft.Text("اسأل علام ما شئت في الشعر", size=30, text_align=ft.TextAlign.CENTER,font_family="Ruqaa"),
        text_box,
        ft.ElevatedButton(content=Text("إرسال", size=SMALL_BTN_SIZE), on_click=on_submit,  width=150),
        output_label,
        back_button
    ])

    page.add(content_column)
