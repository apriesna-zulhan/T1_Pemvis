"""
Aplikasi Konversi Suhu - PySide6

Nama : Apriesna Zulhan
NIM  : F1D02310100
Kelas: Pemvis - C
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    """Jendela utama aplikasi."""

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        """Inisialisasi komponen UI."""

        self.setWindowTitle("Konversi Suhu")
        self.resize(420, 340)
        self.setMinimumSize(380, 300)

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
                font-size: 13px;
                color: #333333;
            }
            QLabel {
                font-size: 13px;
                color: #333333;
            }
            QLineEdit {
                border: 2px solid #82c882;
                border-radius: 6px;
                padding: 8px 10px;
                background-color: #f0fff0;
                font-size: 13px;
                color: #333333;
            }
            QLineEdit:focus {
                border: 2px solid #4cae4c;
            }
            QPushButton {
                background-color: #4da6e8;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3a95d8;
            }
            QPushButton:pressed {
                background-color: #2a84c7;
            }
        """)

        # Judul
        self.judul = QLabel("KONVERSI SUHU")
        self.judul.setAlignment(Qt.AlignCenter)
        self.judul.setStyleSheet("""
            background-color: #4da6e8;
            color: white;
            padding: 14px;
            font-size: 15px;
            font-weight: bold;
            border-radius: 8px;
        """)

        # Label input
        self.label_input = QLabel("Masukkan Suhu (Celsius):")

        # Input suhu
        self.entry_celsius = QLineEdit()
        self.entry_celsius.setPlaceholderText("Contoh: 100")

        # Tombol konversi
        self.btn_f = QPushButton("Fahrenheit")
        self.btn_k = QPushButton("Kelvin")
        self.btn_r = QPushButton("Reamur")

        # Label hasil
        self.label_hasil_title = QLabel("Hasil Konversi:")
        self.label_hasil_title.setStyleSheet("font-weight: bold; color: #333333;")

        self.hasil = QLabel("")
        self.hasil.setAlignment(Qt.AlignLeft)

        # Wrapper hasil
        self.hasil_box = QWidget()
        self.hasil_box.setStyleSheet("""
            background-color: #cce7f8;
            border-left: 5px solid #4da6e8;
            border-radius: 0px;
            padding: 4px;
        """)
        hasil_inner = QVBoxLayout(self.hasil_box)
        hasil_inner.setContentsMargins(10, 10, 10, 10)
        hasil_inner.setSpacing(6)
        hasil_inner.addWidget(self.label_hasil_title)
        hasil_inner.addWidget(self.hasil)

        # Layout tombol
        tombol_layout = QHBoxLayout()
        tombol_layout.setSpacing(10)
        tombol_layout.addWidget(self.btn_f)
        tombol_layout.addWidget(self.btn_k)
        tombol_layout.addWidget(self.btn_r)

        # Layout utama
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)
        layout.addWidget(self.judul)
        layout.addWidget(self.label_input)
        layout.addWidget(self.entry_celsius)
        layout.addLayout(tombol_layout)
        layout.addWidget(self.hasil_box)

        self.setLayout(layout)
        self.center_on_screen()

    def setup_connections(self):
        """Hubungkan tombol dengan fungsi."""
        self.btn_f.clicked.connect(self.konversi_fahrenheit)
        self.btn_k.clicked.connect(self.konversi_kelvin)
        self.btn_r.clicked.connect(self.konversi_reamur)

    def ambil_celsius(self):
        """Ambil nilai Celsius dengan validasi."""
        try:
            return float(self.entry_celsius.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Input harus berupa angka!")
            return None

    def konversi_fahrenheit(self):
        c = self.ambil_celsius()
        if c is not None:
            f = (c * 9/5) + 32
            self.hasil.setText(f"{c:.2f} Celsius = {f:.2f} Fahrenheit")

    def konversi_kelvin(self):
        c = self.ambil_celsius()
        if c is not None:
            k = c + 273.15
            self.hasil.setText(f"{c:.2f} Celsius = {k:.2f} Kelvin")

    def konversi_reamur(self):
        c = self.ambil_celsius()
        if c is not None:
            r = c * 4/5
            self.hasil.setText(f"{c:.2f} Celsius = {r:.2f} Reamur")

    def center_on_screen(self):
        """Posisikan jendela di tengah layar."""
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


def main():
    """Entry point aplikasi."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()