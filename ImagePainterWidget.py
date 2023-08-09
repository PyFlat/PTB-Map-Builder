from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QImage

class ImagePainterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_entries = {}  # Dictionary to hold image positions (x, y) by image path
        self.counter = 0

    def add_image(self, image_path, x, y):
        self.counter += 1
        image = QImage(image_path)
        self.image_entries[self.counter] = ((x, y), image)
        self.update()
        return self.counter

    def remove_image(self, unique_id):
        if unique_id in self.image_entries:
            del self.image_entries[unique_id]
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y), image in self.image_entries.values():
            painter.drawImage(x, y, image)