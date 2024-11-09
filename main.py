import flet as ft
from pages.home import load_home_page
from pages.classify_page import load_page1
from pages.generation_page import load_page2
from pages.explanation_page import load_page3
from pages.chat_page import load_page4
from pages.meters_page import load_page5
from pages.topic_based_page import load_page6

def main(page: ft.Page):
    page.title = "تطبيق علام الشعر"
    page.theme_mode = "light"
    page.fonts = {
        "Amiri": "fonts/Amiri-Regular.ttf"  # Ensure this path is correct
    }
    page.theme = ft.Theme(font_family="Amiri")

    # Function to navigate to different pages
    def navigate_to(page_name):
        page.clean()  # Clear the current page content

        if page_name == "الصفحة الرئيسية":
            load_home_page(page, navigate_to)
        elif page_name == "الصفحة الأولى":
            load_page1(page, navigate_to)
        elif page_name == "الصفحة الثانية":
            load_page2(page, navigate_to)
        elif page_name == "الصفحة الثالثة":
            load_page3(page, navigate_to)
        elif page_name == "الصفحة الرابعة":
            load_page4(page, navigate_to)
        else:
            load_page6(page, navigate_to)

    # Load the main page on start
    navigate_to("الصفحة الرئيسية")

# Run the Flet app
ft.app(target=main)
