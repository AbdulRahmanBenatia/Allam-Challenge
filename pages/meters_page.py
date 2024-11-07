BUHOOR = [
    "السريع",
    "الكامل",
    "المتقارب",
    "المتدارك",
    "المنسرح",
    "المديد",
    "المجتث",
    "الرمل",
    "البسيط",
    "الخفيف",
    "الطويل",
    "الوافر",
    "الهزج",
    "الرجز",
    
    "المقتضب",
    "الخبب",
]
import flet as ft
def load_page5(page: ft.Page, navigate_to):
    page.clean()

    back_button = ft.ElevatedButton("رجوع", on_click=lambda _: navigate_to("الصفحة الرئيسية"), width=150)

    # Create a dropdown with 16 options
    options = [ft.dropdown.Option(bahr) for bahr in BUHOOR]
    dropdown = ft.Dropdown(label="اختر خيارًا", options=options,
                             text_style=ft.TextStyle(font_family="Ruqaa", size=18)
        )

    # Text label to show the selected option
    selected_option_label = ft.Text("", size=20, text_align=ft.TextAlign.RIGHT)

    # Function to update the selected option label
    def on_option_change(e):
        selected_option_label.value = f"اخترت الخيار {dropdown.value}:"
        page.update()  # Update the page to reflect the new label value

    # Attach the change event to the dropdown
    dropdown.on_change = on_option_change

    content_column = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        expand=True
    )
    
    content_column.controls.extend([
        ft.Text("اختر البحر الذي تريد معرفة تفعيلاته الأساسية", size=30, text_align=ft.TextAlign.CENTER,font_family='Ruqaa'),
        dropdown,
        selected_option_label,  # Add the label for showing the selected option
        back_button
    ])

    page.add(content_column)

# Note: Integrate this function into your main app structure to ensure it is called correctly.
