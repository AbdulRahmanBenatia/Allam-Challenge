import flet as ft
from ibm_API import get_response
from utils import Text, SMALL_BTN_SIZE, BACK_BTN_STYLE, SEND_BTN_STYLE

def load_page1(page: ft.Page, navigate_to):
    page.clean()

    back_button = ft.ElevatedButton(content=Text("رجوع", size=SMALL_BTN_SIZE), style=BACK_BTN_STYLE, on_click=lambda _: navigate_to("الصفحة الرئيسية"),  width=100, opacity=0.5)
    output_label = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)

    pattern_overlay = ft.Container(
        # content=None, 
        width=page.width,
        height=page.height,
        # image_src="pattern.png", 
        image_src="Backgrounds/bckg_pages.png",
        image_repeat=ft.ImageRepeat.REPEAT,
        alignment=ft.alignment.center,
        # opacity=0.5
    )

    def on_submit(e):
        prompt = f"""
        ما هو البحر الشعري لهذا البيت؟
        {text_box.value}
        رد باسم البيت فقط.
        مثال: 
        تَـقـرُّ بِهِ العَـيـنـان حُـسـنـاً وَمَنطِقاً وَدَرسـاً وَتَـحـقـيـقـاً بِـحُـسنِ النّصائِحِ
        جوابك: 
        الطويل
        """
        print("PRESSED")
        response = get_response(prompt=prompt)
        print(response)
        # output_label.value = f"لقد أدخلت: {text_box.value}"
        output_label.value = response
        page.update()

    text_box = ft.TextField(
        label='اكتب البيت هنا',
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
        ft.Text("أدخل بيتًا وسيخبرك علَّام على أيِّ بحرٍ كُتِب", size=30, text_align=ft.TextAlign.CENTER,font_family='Ruqaa'),
        text_box,
        ft.ElevatedButton(content=Text("تحديد البحر", size=SMALL_BTN_SIZE), on_click=on_submit,  width=150, style = SEND_BTN_STYLE),
        output_label,
        back_button
    ])
    
    main_container = ft.Stack(
    controls=[pattern_overlay, content_column],
    width=page.width,
    height=page.height,
    )  

    page.add(main_container)
