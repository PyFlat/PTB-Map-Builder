from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QImage

class ImagePainterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_entries = {}  # Dictionary to hold image data by image ID
        self.counter = 0

    def add_image(self, image_path, x, y):
        self.counter += 1
        image = QImage(image_path)
        self.image_entries[self.counter] = {'position': (x, y), 'image': image, 'visible': True}
        self.update()
        return self.counter

    def remove_image(self, unique_id):
        if unique_id in self.image_entries:
            del self.image_entries[unique_id]
            self.update()

    def set_image_visibility(self, unique_id, visible):
        if unique_id in self.image_entries:
            self.image_entries[unique_id]['visible'] = visible
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for entry in self.image_entries.values():
            if entry['visible']:
                x, y = entry['position']
                image = entry['image']
                painter.drawImage(x, y, image)
