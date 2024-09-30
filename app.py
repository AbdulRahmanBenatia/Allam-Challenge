import arabic_reshaper
from bidi.algorithm import get_display
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

# Handling Arabic Text
def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        font_path = "Amiri-Regular.ttf"  

        title_label = Label(text=reshape_text('علَّام الشعر'), font_size='32sp', size_hint=(1, 0.2),
                            halign='center', valign='middle', font_name=font_path)
        title_label.bind(size=title_label.setter('text_size'))

        button1 = Button(text=reshape_text("تحديد البحر الشعري"), font_size='24sp', size_hint=(1, 0.2), font_name=font_path)
        button1.bind(on_press=self.go_to_page1)

        button2 = Button(text=reshape_text("إنشاء أبيات جديدة"), font_size='24sp', size_hint=(1, 0.2), font_name=font_path)
        button2.bind(on_press=self.go_to_page2)

        button3 = Button(text=reshape_text("شرح الأبيات"), font_size='24sp', size_hint=(1, 0.2), font_name=font_path)
        button3.bind(on_press=self.go_to_page3)

        button4 = Button(text=reshape_text("دراسة البحور"), font_size='24sp', size_hint=(1, 0.2), font_name=font_path)
        button4.bind(on_press=self.go_to_page4)

        layout.add_widget(title_label)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)

        self.add_widget(layout)

    def go_to_page1(self, instance):
        self.manager.current = 'page1'
    
    def go_to_page2(self, instance):
        self.manager.current = 'page2'
    
    def go_to_page3(self, instance):
        self.manager.current = 'page3'
    
    def go_to_page4(self, instance):
        self.manager.current = 'page4'

class Page1(Screen):
    def __init__(self, **kwargs):
        super(Page1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title label
        label = Label(text=reshape_text("أدخل البيت المراد معرفة بحره"), font_size='24sp', halign='center', valign='middle', font_name="Amiri-Regular.ttf")
        layout.add_widget(label)

        # Create a TextInput for Arabic text
        self.text_input = TextInput(hint_text=reshape_text('أدخل البيت هنا'), font_size='24sp', size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        layout.add_widget(self.text_input)

        # Create a Label to display reshaped text
        self.output_label = Label(text='', font_size='24sp', size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        layout.add_widget(self.output_label)

        # Bind the on_text event to update the output label and input text
        self.text_input.bind(on_text=self.update_output)

        # Back button
        back_button = Button(text=reshape_text('رجوع'), size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_output(self, instance, value):
        # Update the output label to show the reshaped text
        reshaped_text = reshape_text(value)
        self.output_label.text = reshaped_text
        # Reshape text in the input field
        self.text_input.text = reshaped_text  # Update the input field with reshaped text
        
        print(f"Current input: {value}")  # Print the unreshaped input


class Page2(Screen):
    def __init__(self, **kwargs):
        super(Page2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        dropdown = DropDown()

        # Arabic options for the dropdown
        options = [
            'خيار ١', 'خيار ٢', 'خيار ٣', 'خيار ٤',
            'خيار ٥', 'خيار ٦', 'خيار ٧', 'خيار ٨',
            'خيار ٩', 'خيار ١٠', 'خيار ١١', 'خيار ١٢',
            'خيار ١٣', 'خيار ١٤', 'خيار ١٥', 'خيار ١٦'
        ]

        # Add options to dropdown
        for option in options:
            btn = Button(text=reshape_text(option), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select_option(btn.text, dropdown))
            dropdown.add_widget(btn)

        main_button = Button(text=reshape_text('اختر بحرا'), size_hint=(1, 0.1), font_name="Amiri-Regular.ttf")
        main_button.bind(on_release=dropdown.open)
        layout.add_widget(main_button)
        layout.add_widget(dropdown)

        back_button = Button(text=reshape_text('رجوع'), size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)

        self.add_widget(layout)

    def select_option(self, option, dropdown):
        # Update main button text to show selected option
        dropdown.parent.children[1].text = reshape_text(option)
        dropdown.dismiss()

class Page3(Screen):
    def __init__(self, **kwargs):
        super(Page3, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        label = Label(text=reshape_text("أدخل البيت المراد شرحه"), font_size='24sp', halign='center', valign='middle', font_name="Amiri-Regular.ttf")
        layout.add_widget(label)

        text_input = TextInput(hint_text=reshape_text('أدخل البيت هنا'), font_size='24sp', size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        layout.add_widget(text_input)

        back_button = Button(text=reshape_text('رجوع'), size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)

        self.add_widget(layout)

class Page4(Screen):
    def __init__(self, **kwargs):
        super(Page4, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        dropdown = DropDown()

        # Arabic options for the dropdown
        options = [
            'خيار ١', 'خيار ٢', 'خيار ٣', 'خيار ٤',
            'خيار ٥', 'خيار ٦', 'خيار ٧', 'خيار ٨',
            'خيار ٩', 'خيار ١٠', 'خيار ١١', 'خيار ١٢',
            'خيار ١٣', 'خيار ١٤', 'خيار ١٥', 'خيار ١٦'
        ]

        # Add options to dropdown
        for option in options:
            btn = Button(text=reshape_text(option), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select_option(btn.text, dropdown))
            dropdown.add_widget(btn)

        main_button = Button(text=reshape_text('اختر بحرا'), size_hint=(1, 0.1), font_name="Amiri-Regular.ttf")
        main_button.bind(on_release=dropdown.open)
        layout.add_widget(main_button)
        layout.add_widget(dropdown)

        back_button = Button(text=reshape_text('رجوع'), size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)

        self.add_widget(layout)

    def select_option(self, option, dropdown):
        # Update main button text to show selected option
        dropdown.parent.children[1].text = reshape_text(option)
        dropdown.dismiss()

class ArabicApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainPage(name='main'))
        sm.add_widget(Page1(name='page1'))
        sm.add_widget(Page2(name='page2'))
        sm.add_widget(Page3(name='page3'))
        sm.add_widget(Page4(name='page4'))

        return sm

if __name__ == '__main__':
    ArabicApp().run()
