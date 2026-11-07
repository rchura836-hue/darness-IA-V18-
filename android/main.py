from datetime import datetime
from zoneinfo import ZoneInfo
import random

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

ASSETS = ["EURUSD-OTC", "GBPUSD-OTC", "USDJPY-OTC", "EURJPY-OTC",
          "EURGBP-OTC", "GBPJPY-OTC", "USDCHF-OTC", "NZDUSD-OTC", "AUDCAD-OTC"]

class DarnnessDemo(App):
    def build(self):
        self.title = "DARNNESS IA OTC V28.1"
        root = BoxLayout(orientation="vertical", padding=dp(16), spacing=dp(10))
        root.add_widget(Label(
            text="[b]DARNNESS IA OTC V28.1[/b]\nSimulador educativo de mercado",
            markup=True, size_hint_y=None, height=dp(70)))
        root.add_widget(Label(
            text="MODO DEMOSTRACIÓN · Datos ficticios\nNo conecta con brokers ni ejecuta operaciones.",
            size_hint_y=None, height=dp(55)))
        btn = Button(text="Generar ejemplo simulado", size_hint_y=None, height=dp(52))
        btn.bind(on_release=self.generate)
        root.add_widget(btn)
        scroll = ScrollView()
        self.output = Label(text="Pulsa el botón para ver un ejemplo de señal simulada.",
                            size_hint_y=None, halign="left", valign="top")
        self.output.bind(texture_size=lambda w, s: setattr(w, "height", s[1] + dp(24)))
        self.output.bind(width=lambda w, _: setattr(w, "text_size", (w.width, None)))
        scroll.add_widget(self.output)
        root.add_widget(scroll)
        root.add_widget(Label(
            text="Solo para aprendizaje. No representa una recomendación financiera.",
            size_hint_y=None, height=dp(48)))
        return root

    def generate(self, *_):
        asset = random.choice(ASSETS)
        direction = random.choice(["CALL", "PUT"])
        score = random.randint(55, 85)
        now = datetime.now(ZoneInfo("America/La_Paz")).strftime("%Y-%m-%d %H:%M:%S")
        self.output.text = (
            "EJEMPLO SIMULADO\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"Activo de ejemplo: {asset}\n"
            f"Dirección ficticia: {direction}\n"
            f"Puntuación didáctica: {score}/100\n"
            f"Hora Bolivia: {now}\n"
            "Duración ilustrativa: 1 minuto\n\n"
            "Este resultado se genera al azar para demostrar la interfaz. "
            "No procede de cotizaciones reales, no es una predicción y no debe usarse "
            "para tomar decisiones con dinero."
        )

if __name__ == "__main__":
    DarnnessDemo().run()
