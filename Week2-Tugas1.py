"""
Aplikasi Biodata - PySide6.

Nama  : Apriesna Zulhan
NIM   : F1D02310100
Kelas : Pemrograman Visual C
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
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

        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(380, 480)
        self.setMinimumSize(380, 480)

        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                font-family: Arial, sans-serif;
                font-size: 13px;
                color: #333333;
            }
            QLabel {
                font-size: 13px;
                color: #333333;
                margin-top: 4px;
            }
            QLineEdit {
                border: 2px solid #82c882;
                border-radius: 6px;
                padding: 6px 10px;
                background-color: #f0fff0;
                font-size: 13px;
                color: #333333;
            }
            QComboBox {
                border: 2px solid #82c882;
                border-radius: 6px;
                padding: 6px 10px;
                background-color: #ffffff;
                font-size: 13px;
                color: #555555;
            }
            QPushButton#btn_tampil {
                background-color: #5b9bd5;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 8px 20px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton#btn_tampil:hover {
                background-color: #4a8bc4;
            }
            QPushButton#btn_tampil:pressed {
                background-color: #3a7ab3;
            }
            QPushButton#btn_reset {
                background-color: #aaaaaa;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 8px 20px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton#btn_reset:hover {
                background-color: #999999;
            }
            QPushButton#btn_reset:pressed {
                background-color: #888888;
            }
        """)

        # ===== Widget =====
        self.label_nama = QLabel("Nama Lengkap:")
        self.entry_nama = QLineEdit()

        self.label_nim = QLabel("NIM:")
        self.entry_nim = QLineEdit()
        self.entry_nim.setPlaceholderText("Masukkan NIM")

        self.label_kelas = QLabel("Kelas:")
        self.entry_kelas = QLineEdit()
        self.entry_kelas.setPlaceholderText("Contoh: TI-2A")

        self.label_jk = QLabel("Jenis Kelamin:")
        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["", "Laki-laki", "Perempuan"])

        # Tombol
        self.btn_tampil = QPushButton("Tampilkan")
        self.btn_tampil.setObjectName("btn_tampil")
        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setObjectName("btn_reset")

        # Area hasil
        self.hasil = QLabel("")
        self.hasil.setStyleSheet("""
            background-color: #d5e8d4;
            border: 1px solid #a8d5a2;
            border-radius: 6px;
            padding: 10px;
            font-size: 13px;
            color: #2d6a2d;
                                 border-left: 4px solid #4cae4c
        """)
        self.hasil.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.hasil.setFixedHeight(120)

        # ===== Layout =====
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(6)

        layout.addWidget(self.label_nama)
        layout.addWidget(self.entry_nama)

        layout.addWidget(self.label_nim)
        layout.addWidget(self.entry_nim)

        layout.addWidget(self.label_kelas)
        layout.addWidget(self.entry_kelas)

        layout.addWidget(self.label_jk)
        layout.addWidget(self.combo_jk)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)
        btn_layout.addWidget(self.btn_tampil)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addStretch()

        layout.addSpacing(6)
        layout.addLayout(btn_layout)
        layout.addSpacing(6)
        layout.addWidget(self.hasil)

        self.setLayout(layout)
        self.center_on_screen()

    def setup_connections(self):
        """Setup signal-slot connections."""
        self.btn_tampil.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_data)

    def tampilkan_data(self):
        """Menampilkan data biodata."""
        nama = self.entry_nama.text()
        nim = self.entry_nim.text()
        kelas = self.entry_kelas.text()
        jk = self.combo_jk.currentText()

        if nama == "" or nim == "" or kelas == "" or jk == "":
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        self.hasil.setText(
            f"<b>DATA BIODATA</b><br><br>"
            f"Nama: {nama}<br>"
            f"NIM: {nim}<br>"
            f"Kelas: {kelas}<br>"
            f"Jenis Kelamin: {jk}"
        )

    def reset_data(self):
        """Reset semua input."""
        self.entry_nama.clear()
        self.entry_nim.clear()
        self.entry_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        self.hasil.setText("")

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