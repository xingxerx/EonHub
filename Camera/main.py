import sys
import cv2
from PySide6.QtCore import QTimer, Slot, QObject, Signal, Property
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
#from camera_module import Camera # Removed this line
from create_model import Camera # Added this line
from quantum_module import get_quantum_random_number
from effects_module import superposition_effect
import os

class Backend(QObject):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera
        self._is_superposition_enabled = False

    frameChanged = Signal(QPixmap)
    superpositionEnabledChanged = Signal(bool)

    @Property(bool, notify=superpositionEnabledChanged)
    def isSuperpositionEnabled(self):
        return self._is_superposition_enabled

    @isSuperpositionEnabled.setter
    def isSuperpositionEnabled(self, value):
        if self._is_superposition_enabled != value:
            self._is_superposition_enabled = value
            self.superpositionEnabledChanged.emit(value)

    @Slot()
    def captureFrame(self):
        frame = self.camera.capture_frame()
        if frame is not None:
            if self._is_superposition_enabled:
                frame = superposition_effect(frame)
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.frameChanged.emit(pixmap)

    @Slot(int)
    def getRandomNumber(self, num_bits):
        random_number = get_quantum_random_number(num_bits)
        print(f"Quantum Random Number: {random_number}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    camera = Camera()
    backend = Backend(camera)
    engine.rootContext().setContextProperty("backend", backend)

    # Construct the absolute path to main.qml
    current_dir = os.path.dirname(os.path.abspath(__file__))
    qml_file_path = os.path.join(current_dir, "ui", "main.qml")

    engine.load(qml_file_path)
    if not engine.rootObjects():
        sys.exit(-1)

    timer = QTimer()
    timer.timeout.connect(backend.captureFrame)
    timer.start(30)  # Update every 30 milliseconds (adjust as needed)

    sys.exit(app.exec())
