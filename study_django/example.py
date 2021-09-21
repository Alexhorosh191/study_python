import sys
import numpy
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    QMessageBox.critical(None, 'Ошибка!', text)
    quit()

sys.excepthook = log_uncaught_exceptions


class ShowImage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.setWindowTitle("Пример рисования изображения")
        self.setGeometry(400, 200, 600, 400)

        pixel = numpy.zeros((10, 10, 3)).astype(int)
        pixel[0][0][2] = 255
        print(pixel)

        image = Image.fromarray(pixel, 'RGB')

        self.image_qt = ImageQt(image)

        pixmap = QPixmap(QImage(self.image_qt))

        label = QLabel(self)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setStyleSheet("background-color: white")
        label.setGeometry(0, 0, 100, 100)
        label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_application = ShowImage()
    my_application.show()
    sys.exit(app.exec_())