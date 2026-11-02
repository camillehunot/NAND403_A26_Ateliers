from maya import cmds
from PySide6.QtWidgets import (
    QWidget, 
)

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cours 8")
        self.setMinimumWidth(400)
        self.build_ui()