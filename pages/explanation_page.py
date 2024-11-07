import flet as ft
from ibm_API import get_response

def load_page3(page: ft.Page, navigate_to):
    page.clean()

    back_button = ft.ElevatedButton("رجوع", on_click=lambda _: navigate_to("الصفحة الرئيسية"), width=150)
    output_label = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)

    def on_submit(e):
        prompt = f"""
        اشرح هذا البيت شرحا موجزا جدا: 
        {text_box.value}
        لا تقل اسم الشاعر، ولا تكتب البيت ثانية.
        مثال: 
        قم للمعلم وفه التبجيلا كاد المعلم أن يكون رسولا
        جوابك: 
        احترم معلمك وقدره، فإن مكانته شبيهة بمكانة الرسل لأنه يحمل رسالة العلم.
        """
        print("PRESSED")
        response = get_response(prompt=prompt)
        print(response)
        # output_label.value = f"لقد أدخلت: {text_box.value}"
        output_label.value = response
        page.update()

    text_box = ft.TextField(
        label="أدخل البيت هنا",
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
        ft.Text("أدخل بيتًا وسيوضح علَّام معناه", size=30, text_align=ft.TextAlign.CENTER,font_family="Ruqaa"),
        text_box,
        ft.ElevatedButton("عرض الشرح", on_click=on_submit),
        output_label,
        back_button
    ])

    page.add(content_column)
