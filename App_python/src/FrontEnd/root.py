import sys
import src.BackEnd.screen_utils as ScreenUtils
import src.BackEnd.json_utils as JsonUtils
import src.BackEnd.commands as Commands
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QDesktopWidget, QLabel, \
    QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class RootWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Načtení konfigurace
        screen_utils_instance = ScreenUtils.get_info()
        screen_info = screen_utils_instance.window_geometry()

        json_utils_instance = JsonUtils.Actions()
        background = json_utils_instance.read_config("FrontEnd_config", "Background_color_hex")
        self.__font_color = json_utils_instance.read_config("FrontEnd_config", "Font_color")

        # root window configuration
        self.setWindowTitle("The Fools App")
        self.setWindowIcon(QIcon('../assets/icon_gui.png'))
        self.setGeometry(screen_info[0], screen_info[1], screen_info[2], screen_info[3])
        self.setMinimumSize(screen_info[2] // 2, screen_info[3] // 2)

        self.setStyleSheet(f"background-color: {background};")

        """ Widget Configuration """
        self.title_label = QLabel("The Fools App", self)  # Hlavní nadpis
        self.title_label.setAlignment(Qt.AlignCenter)  # Vycentrování textu

        self.output_text = QTextEdit(self)  # Výstupní pole
        self.output_text.setReadOnly(True)  # Výstupní pole je pouze pro čtení
        self.output_text.setStyleSheet(f"color: {self.__font_color};")  # Nastavení barvy písma

        self.input_line = QLineEdit(self)  # Vstupní pole
        self.input_line.setPlaceholderText("Type 'stinky' and hit Enter")  # Placeholder
        self.input_line.setStyleSheet(f"color: {self.__font_color};")  # Nastavení barvy písma

        # Přidání signálu pro stisknutí klávesy Enter
        self.input_line.returnPressed.connect(self.process_input)

        self.root_widgets()

    def root_widgets(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        layout.addWidget(self.title_label)  # Přidání nadpisu
        layout.addWidget(self.output_text)  # Přidání textového pole pro výstup
        layout.addWidget(self.input_line)  # Přidání vstupního pole

        # Nastavení fokus na vstupní pole
        self.input_line.setFocus()

    def process_input(self):
        """Zpracovává vstup a zobrazuje parodii nebo vymaže text."""
        user_input = self.input_line.text().strip()  # Získání uživatelského vstupu

        # Přidáme uživatelský vstup do výstupního pole
        self.output_text.append(f">> {user_input}")

        """
        funny commands in console like thing: it goes to commands class and search in for loop array that has names
        of implemented "commands"        
        """
        instance = Commands.Handler(self.output_text)
        instance.is_function_implemented(user_input)

        self.input_line.clear()  # Vymaže vstupní pole pro další vstup

    def resizeEvent(self, event):
        self.setUpdatesEnabled(False)
        super().resizeEvent(event)
        self.setUpdatesEnabled(True)

    def showEvent(self, event):
        self.center_root_window()
        super().showEvent(event)

    def center_root_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def run():
    app = QApplication(sys.argv)
    window = RootWindow()
    window.show()
    sys.exit(app.exec())
