from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
# Importe suas classes de segurança (certifique-se que os arquivos estão na pasta)
# from seguranca import SegurancaVRS 

class AppAlunoVRS(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        Window.softinput_mode = "below_target"
        
        # Proteção Anti-Print (Aqui você chama sua função jnius/android)
        # SegurancaVRS.ativar_protecao_apk()

        self.screen = MDScreen()
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        self.layout.add_widget(MDLabel(
            text="VRS SOLUÇÕES", font_style="H4", halign="center", theme_text_color="Primary"
        ))

        self.email_input = MDTextField(
            hint_text="E-mail cadastrado", mode="rectangle", icon_right="email"
        )
        self.layout.add_widget(self.email_input)

        self.btn_entrar = MDRaisedButton(
            text="ENTRAR AGORA", pos_hint={"center_x": .5}, size_hint=(0.8, None),
            on_release=self.autenticar
        )
        self.layout.add_widget(self.btn_entrar)

        self.screen.add_widget(self.layout)
        return self.screen

    def autenticar(self, *args):
        email = self.email_input.text
        # Lógica de autenticação e validação de HWID entra aqui
        print(f"Autenticando: {email}")

if __name__ == "__main__":
    AppAlunoVRS().run()
