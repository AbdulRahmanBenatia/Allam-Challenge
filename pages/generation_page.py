import flet as ft
from ibm_API import get_response

def load_page2(page: ft.Page, navigate_to):
    page.clean()

    back_button = ft.ElevatedButton("رجوع", on_click=lambda _: navigate_to("الصفحة الرئيسية"), width=150)
    output_label = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)

    def on_submit(e):
        prompt = f"""
        اكتب أبياتًا بعد هذا البيت:
        {text_box.value}
        """
        # مثال: 
        # يَــقُــولون لي أَعــرَضــتَ عَـمَّنـ تُـحـبُّهُ كَـذَبـتُـم وَلَكـن لَم يَكُن رائِقَ النَفسِ
        # جوابك: 
        # وَلَم يَــكُــن الإِعــراضُ مِـنّـي تَـعَـمُّداً وَهَل يُمكِنُ الإِعراضُ عَن غايَةِ الأُنسِ
        # وَلَكـن صَـرَفـتُ الطَـرفَ مِـن نُـور وَجهِهِ كَما تُصرَفُ الأَبصارُ عَن قُرصَةِ الشَمسِ
        
        print("PRESSED")
        response = get_response(prompt=prompt)
        print(response)
        # output_label.value = f"لقد أدخلت: {text_box.value}"ء
        output_label.value = response
        print('Done Generating')
        page.update()

    text_box = ft.TextField(
        label="اكتب البيت هنا",
        text_align=ft.TextAlign.RIGHT,
        on_submit=on_submit,
        multiline=True,
    )

    content_column = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        expand=True
    )
    
    content_column.controls.extend([
        ft.Text("أدخِل بيتًا أو بيتين وسيكمل علام الأبيات من إبداعه", size=30, text_align=ft.TextAlign.CENTER,font_family='Ruqaa'),
        text_box,
        ft.ElevatedButton("إرسال", on_click=on_submit),
        output_label,
        back_button
    ])

    page.add(content_column)
