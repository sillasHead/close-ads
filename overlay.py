from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer

class OverlayWindow(QMainWindow):
    def __init__(self, areas):
        super().__init__()
        self.areas = areas  # List of rectangles (coordinates)
        self.setWindowTitle("Overlay")
        self.setGeometry(0, 0, 1920, 1080)  # Fullscreen overlay (adjust as needed)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 0, 0, 100))  # Red with transparency
        painter.setPen(Qt.NoPen)
        for area in self.areas:
            # Draw each rectangle
            painter.drawRect(QRect(area[0], area[1], area[2], area[3]))

def create_overlay(areas):
    app = QApplication([])
    window = OverlayWindow(areas)
    # Automatically quit after 10 seconds
    QTimer.singleShot(8000, app.quit) 
    app.exec_()
