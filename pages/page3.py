from components.arabic_text_input import ArabicTextInput
from utils import reshape_text
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from ibm_API import get_reponse

class Page3(Screen):
    def __init__(self, **kwargs):
        super(Page3, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title label
        self.label = Label(text=reshape_text("أدخل البيت المراد شرحه"), font_size='24sp', halign='center', valign='middle', font_name="Amiri-Regular.ttf")
        layout.add_widget(self.label)

        # Create a TextInput for Arabic text
        self.text_input = ArabicTextInput(hint_text=reshape_text('أدخل البيت هنا'), font_size='24sp', size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        layout.add_widget(self.text_input)

        # Create a Label to display reshaped text
        self.output_label = Label(text='', font_size='24sp', size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        layout.add_widget(self.output_label)

        # Bind the on_text event to update the output label and input text
        # self.text_input.bind(on_text=self.update_output)
        self.text_input.bind(text=self.update_output)

        # Submit button
        submit_button = Button(text=reshape_text("تأكيد"), size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        submit_button.bind(on_press=self.on_submit)
        layout.add_widget(submit_button)
        
        # Back button
        back_button = Button(text=reshape_text('رجوع'), size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)

        self.add_widget(layout)
        
        self.input_list = []
        self.last_value = ''
        self.full_verse = '' 


    def update_output(self, instance, value):        
        # Reshape Arabic text from the raw input
        # reshaped_text = arabic_reshaper.reshape(self.raw_text)  # Reshape the Arabic text for proper display
        print("Val : ",value)
        print("Reshaped: ",reshape_text(value))
        
        if self.text_input.BACK:
            self.input_list = self.input_list[:-1]
            value=value[:-1]
            
        else:
            self.input_list.append(value[-1])
            # Unbind to prevent recursion error when updating text
            instance.unbind(text=self.update_output)
            # instance.text = bidi_text
            till_now = reshape_text(''.join(self.input_list))
            if(self.input_list[-1]!=' '):
                instance.text = till_now
        # Rebind after updating the text
        
        instance.bind(text=self.update_output)
        self.full_verse = value
        
    def on_submit(self, interface):
        print(self.full_verse)
        prompt = f"""
        اشرح هذا البيت شرحا موجزا جدا: 
        {self.full_verse}
        """
        print("PRESSED")
        response = get_reponse(prompt=prompt)
        print(response)
        self.label.text = reshape_text(response)