from components.arabic_text_input import ArabicTextInput
from utils import reshape_text
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from ibm_API import get_response

class Page1(Screen):
    def __init__(self, **kwargs):
        super(Page1, self).__init__(**kwargs)

        # Use FloatLayout to allow precise positioning
        float_layout = FloatLayout()

        # Main content layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(1, 0.9), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Title label
        self.label = Label(
            text=reshape_text("أدخل البيت المراد معرفة بحره"),
            font_size='24sp', halign='center', valign='middle',
            font_name="Amiri-Regular.ttf"
        )
        layout.add_widget(self.label)

        # Text input for Arabic text
        self.text_input = ArabicTextInput(
            hint_text=reshape_text('أدخل البيت هنا'),
            font_size='24sp', size_hint=(1, 0.2),
            font_name="Amiri-Regular.ttf"
        )
        layout.add_widget(self.text_input)

        # Output label
        self.output_label = Label(
            text='', font_size='24sp', size_hint=(1, 0.2),
            font_name="Amiri-Regular.ttf"
        )
        layout.add_widget(self.output_label)

        # Bind text changes to update output label
        self.text_input.bind(text=self.update_output)

        # Submit button
        submit_button = Button(
            text=reshape_text("تأكيد"),
            size_hint=(1, 0.2),
            font_name="Amiri-Regular.ttf"
        )
        submit_button.bind(on_press=self.on_submit)
        layout.add_widget(submit_button)

        # Add the main layout to the FloatLayout
        float_layout.add_widget(layout)

        # Back button in the top-left corner with custom icon
        back_button = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0.02, 'top': 0.98},  # Positioned in the top-left corner
            background_normal='/home/ozeiri/repos/Allam-Challenge/icons/back.png',
            background_down='/home/ozeiri/repos/Allam-Challenge/icons/back.png',
            border=(0, 0, 0, 0)  # Removes padding around the icon
        )
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        float_layout.add_widget(back_button)  # Add back button directly to FloatLayout

        self.add_widget(float_layout)  # Add FloatLayout to the screen

        # Initialize input tracking
        self.input_list = []
        self.full_verse = ''

    def update_output(self, instance, value):
        # Update Arabic text in input
        print("Val:", value)
        print("Reshaped:", reshape_text(value))

        if self.text_input.BACK:
            self.input_list = self.input_list[:-1]
            value = value[:-1]
        else:
            self.input_list.append(value[-1])
            instance.unbind(text=self.update_output)
            till_now = reshape_text(''.join(self.input_list))
            if self.input_list[-1] != ' ':
                instance.text = till_now

        instance.bind(text=self.update_output)
        self.full_verse = value

    def on_submit(self, interface):
        print(self.full_verse)
        prompt = f"""
        ما بحر هذا البيت؟ 
        {self.full_verse}
        فقط البحر.
        """
        print("PRESSED")
        response = get_response(prompt=prompt)
        print(response)
        self.label.text = reshape_text(response)
