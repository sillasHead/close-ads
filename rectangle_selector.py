from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QRect
import sys

class RectangleSelector(QLabel):
    def __init__(self):
        super().__init__()
        self.start_point = None
        self.end_point = None
        self.setWindowTitle("Select Rectangle")
        self.setGeometry(100, 100, 800, 600)  # Set the window size
        self.setWindowOpacity(0.3)  # Semi-transparent
        self.setWindowFlag(Qt.FramelessWindowHint)  # No border
        self.setStyleSheet("background-color: black;")  # Background color

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.start_point:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            rect = QRect(self.start_point, self.end_point).normalized()
            print(f"\nRectangle selected:\nx, y, width, height -> {rect.left()}, {rect.top()}, {rect.width()}, {rect.height()}")
            QApplication.quit()

    def paintEvent(self, event):
        if self.start_point and self.end_point:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            rect = QRect(self.start_point, self.end_point).normalized()
            painter.drawRect(rect)

def main():
    app = QApplication(sys.argv)
    selector = RectangleSelector()
    selector.showFullScreen()  # Show full screen to let the user select any area
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
