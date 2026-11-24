import math

from maya import cmds
from maya import OpenMayaUI as omui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QSlider,
    QLabel,
    QPushButton,
)
from shiboken6 import wrapInstance


def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)


class RockMaker(QDialog):
    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowTitle("Rock Maker")
        self.setMinimumWidth(260)
        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout(self)
        form = QFormLayout()
        main_layout.addLayout(form)

        self.subdivisions_slider = self.add_slider(form, "Subdivisions", 4, 64, 20)
        self.amplitude_slider = self.add_slider(form, "Amplitude", 0, 100, 30, divisor=100)
        self.frequency_slider = self.add_slider(form, "Frequency", 5, 80, 30, divisor=10)
        self.seed_slider = self.add_slider(form, "Seed", 0, 100, 0)

        self.subdivisions_slider.valueChanged.connect(self.apply_subdivisions)

        create_button = QPushButton("Create rock")
        create_button.clicked.connect(self.make_rock)
        main_layout.addWidget(create_button)

    def add_slider(self, form, name, minimum, maximum, value, divisor=1):
        slider = QSlider(Qt.Horizontal)
        slider.setRange(minimum, maximum)
        slider.setValue(value)

        value_label = QLabel(f"{value / divisor:g}")
        value_label.setMinimumWidth(30)
        slider.valueChanged.connect(lambda v: value_label.setText(f"{v / divisor:g}"))

        row = QHBoxLayout()
        row.addWidget(slider)
        row.addWidget(value_label)
        form.addRow(name, row)
        return slider

    def make_rock(self):
        self.create_rock(
            self.subdivisions_slider.value(),
            self.amplitude_slider.value() / 100,
            self.frequency_slider.value() / 10,
            self.seed_slider.value(),
        )

    def create_rock(self, subdivisions, amplitude, frequency, seed):
        # étape 1 : créer une sphère
        
        base_rock = cmds.polySphere(n="rock", sx=subdivisions, sy=subdivisions)
       

        # étape 2 : faire une for loop sur chacun des vertices

        selected_rock = cmds.ls(selection=True)[0] 
        
        vertex = cmds.ls(f"{selected_rock}.vtx[*]", flatten=True)
        
        for obj in vertex:
        
            pos = cmds.xform(vertex, query=True, translation=True, worldSpace=True)
            x, y, z = pos[0], pos[1], pos[2]

            self.apply_subdivisionsget_bump(x, y, z, frequency, seed)

        # étape 3 : déplacer chaque vertex avec un valeur aléatoire (get_bump)
        

    def apply_subdivisions(self, subdivisions, amplitude, frequency, seed):
        selection = cmds.ls(selection=True)[0]
       

        #trouve le poly de base
        sphere_base_node = cmds.ls(cmds.listHistory(selection), type="polySphere")[0]

       #update subdivision
        cmds.setAttr(f"{sphere_base_node}.subdivisionsAxis", subdivisions)
        cmds.setAttr(f"{sphere_base_node}.subdivisionsHeight", subdivisions)

        self.applydeform(subdivisions, amplitude, frequency, seed)


    def applydeform(self, subdivisions, amplitude, frequency, seed):
        
        # étape 2 : faire une for loop sur chacun des vertices

        selected_rock = cmds.ls(selection=True)[0] 
        
        vertex = cmds.ls(f"{selected_rock}.vtx[*]", flatten=True)
        
        for obj in vertex:
        
            pos = cmds.xform(vertex, query=True, translation=True, worldSpace=True)
            x, y, z = pos[0], pos[1], pos[2]

            self.apply_subdivisionsget_bump(x, y, z, frequency, seed)

        # étape 3 : déplacer chaque vertex avec un valeur aléatoire (get_bump)

    def get_bump(x, y, z, frequency, seed):
            return (math.sin(x * frequency + seed)
                    + math.sin(y * frequency + seed * 2)
                    + math.sin(z * frequency + seed * 3)) / 3

        


def show_tool():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RockMaker()
    tool_window.show()


show_tool()

