from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
import sys, io, os

class PythonRunner(App):

    def build(self):
        main = BoxLayout(orientation='vertical')

        # Code editor
        self.editor = TextInput(
            hint_text="Write Python code here...",
            size_hint=(1, 0.5)
        )

        # Output area
        self.output = TextInput(
            text="Output...",
            readonly=True,
            size_hint=(1, 0.3)
        )

        # Buttons layout
        btn_layout = BoxLayout(size_hint=(1, 0.2))

        run_btn = Button(text="Run ▶️")
        run_btn.bind(on_press=self.run_code)

        save_btn = Button(text="Save 💾")
        save_btn.bind(on_press=self.save_code)

        load_btn = Button(text="Open 📂")
        load_btn.bind(on_press=self.load_code)

        clear_btn = Button(text="Clear 🧼")
        clear_btn.bind(on_press=self.clear_all)

        btn_layout.add_widget(run_btn)
        btn_layout.add_widget(save_btn)
        btn_layout.add_widget(load_btn)
        btn_layout.add_widget(clear_btn)

        main.add_widget(self.editor)
        main.add_widget(btn_layout)
        main.add_widget(self.output)

        return main

    def run_code(self, instance):
        code = self.editor.text

        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        try:
            exec(code)
            result = sys.stdout.getvalue()
        except Exception as e:
            result = "Error:\n" + str(e)

        sys.stdout = old_stdout
        self.output.text = result if result else "No output"

    def save_code(self, instance):
        filename = "my_code.py"
        with open(filename, "w") as f:
            f.write(self.editor.text)
        self.output.text = f"Saved as {filename}"

    def load_code(self, instance):
        filename = "my_code.py"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.editor.text = f.read()
            self.output.text = "File loaded"
        else:
            self.output.text = "No saved file found"

    def clear_all(self, instance):
        self.editor.text = ""
        self.output.text = ""

PythonRunner().run()
