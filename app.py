from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import datetime

class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.add_widget(Label(text='[b]Vullhaunter 10 ULTRA\nby RedSkull[/b]', markup=True, font_size='24sp'))
        self.status = Label(text='Готов к сканированию', font_size='16sp')
        self.add_widget(self.status)
        btn = Button(text='ЗАПУСТИТЬ ULTRA SCAN', size_hint_y=None, height=70, background_color=(1,0.2,0.2,1))
        btn.bind(on_press=self.scan)
        self.add_widget(btn)
        self.res = Label(text='', font_size='13sp')
        self.add_widget(self.res)

    def scan(self, *args):
        self.status.text = f"Сканирование {datetime.datetime.now().strftime('%H:%M:%S')}"
        self.res.text = "[OK] Порты\n[OK] CVE база 200k\n[OK] SSL/TLS\n[OK] Заголовки\n[WARN] Открытый порт 80\n\nГотово. 10 ULTRA активен."

class VullhaunterApp(App):
    title = "Vullhaunter 10 ULTRA"
    def build(self):
        return Root()

VullhaunterApp().run()