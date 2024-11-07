import flet as ft


def load_home_page(page: ft.Page, navigate_to):
    page.clean()
    page.title = "علَّام الشعر"
    page.theme_mode = "dark"
    page.fonts = {
        "Amiri": "fonts/Amiri-Regular.ttf",
        "Ruqaa": "fonts/ArefRuqaa-Regular.ttf",
        "Ruqaa-Bold": "fonts/ArefRuqaa-Bold.ttf",
        "Thuluth": "fonts/AM_Thulth_Regular_0.1.otf",
    }
    page.theme = ft.Theme(font_family = "Amiri")
    # page.bgcolor = "lightblue"

    # pattern_overlay = ft.Container(
    #     # content=None, 
    #     width=page.width,
    #     height=page.height,
    #     # image=ft.Image(src="pattern.png", repeat=ft.ImageRepeat.REPEAT, opacity=0.3), 
    #     image_src="pattern.png",  # Path to your pattern image
    #     image_repeat=ft.ImageRepeat.REPEAT,
    #     alignment=ft.alignment.center,
    #     # opacity=0.1
    # )

    
    main_column = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        expand=True
    )

    
    main_column.controls.extend([
        ft.Text('عَلَّامُ الشِّعْرِ', size=40, text_align=ft.TextAlign.CENTER,font_family='Thuluth'),
        # buttons
        ft.ElevatedButton("تحديد البحر الشعري", on_click=lambda _: navigate_to("الصفحة الأولى"),   width=300),
        ft.ElevatedButton("إنشاء أبيات جديدة", on_click=lambda _: navigate_to("الصفحة الثانية"), width=300),
        ft.ElevatedButton("شرح الأبيات", on_click=lambda _: navigate_to("الصفحة الثالثة"), width=300),
        ft.ElevatedButton("دراسة البحور", on_click=lambda _: navigate_to("الصفحة الخامسة"), width=300),
        ft.ElevatedButton("اسأل علَّام", on_click=lambda _: navigate_to("الصفحة الرابعة"), width=300),
        ft.ElevatedButton("تغنى بموضوعك", on_click=lambda _: navigate_to("الصفحة السادسة"), width=300),

        ])

    # main_container = ft.Stack(
    #     controls=[pattern_overlay, main_column],
    #     width=page.width,
    #     height=page.height,
    # )  
    # page.add(main_container)

    page.add(main_column)