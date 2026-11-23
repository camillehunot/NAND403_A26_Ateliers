from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout, QPushButton, QLabel, QSpinBox

from PySide6.QtCore import Qt

import maya.cmds as cmds
import maya.OpenMayaUI as omui

import MASH.api as mapi #option qui permet le scatter dans maya

from shiboken6 import wrapInstance
 
def maya_main_window():

    pointer = omui.MQtUtil.mainWindow()

    return wrapInstance(int(pointer), QWidget)
 
class LiveScatter(QWidget):

    def __init__(self):

        super().__init__(maya_main_window())

        self.setWindowFlags(Qt.Window)

        self.build_ui()

        self.dist_node = None #sauvegarde de mon reseau mash
 
    def build_ui(self):

        self.main_layout = QVBoxLayout(self)
        
        self.create_instructions()
        self.create_label("Max scatter")
        self.create_spinbox()
        
        self.create_label("Scatter : ")
        self.create_slider(self.max_scatter.value())
        
 
    def create_label(self, texte):

        self.label_text_template = texte

        self.scatter_label = QLabel(self.label_text_template )

        self.main_layout.addWidget(self.scatter_label)

    def create_instructions(self):
        texte = (
          "1. Select object to scatter\n"
          "2. Then press shift and select surface where you want the scatter.\n"
          "3. Use slider to choose number of copy to scatter"
        )
        self.instructions_label = QLabel(texte)
        self.instructions_label.setStyleSheet(
          "color: #aaaaaa; font-style: italic; margin-bottom: 12px;"
        )
        self.main_layout.addWidget(self.instructions_label)

   

    def create_spinbox(self):
        self.max_scatter = QSpinBox()
        self.max_scatter.setRange(1, 1000) 
        self.max_scatter.setValue(30)
        self.main_layout.addWidget(self.max_scatter)
        self.max_scatter.valueChanged.connect(self.on_spinbox_changed)

    def on_spinbox_changed(self):
        max_value = self.max_scatter.value()  # <-- Récupère le nombre (int ou float)
        self.scatter_slider.setMaximum(max_value)
        return max_value

    def create_slider(self, value):

        max_scatter = value

        self.scatter_slider = QSlider()

        self.scatter_slider.setOrientation(Qt.Horizontal)

        self.scatter_slider.setRange(1, max_scatter)

        self.scatter_slider.setValue(1)

        self.scatter_slider.valueChanged.connect(self.apply_scatter)

        self.main_layout.addWidget(self.scatter_slider)
 
    def update_label(self, scatter_factor):

        self.scatter_label.setText(self.label_text_template + f"{scatter_factor}")
 
    def apply_scatter(self):

        scatter_factor = self.scatter_slider.value()

        self.update_label(scatter_factor)

        selection = cmds.ls(selection=True, transforms=True)

        #---vérification si mash existant + sécurité de sélection
        if not self.dist_node or not cmds.objExists(self.dist_node): #ne créer qu'un mash 
            #le mash a besoin de deux sélection : l'objet a scatter et la surface sur laquelle s'effectue le scatter
            # la ligne suivante permet de récupérer dans l'ordre la sélection.
            selection = cmds.ls(selection=True, transforms=True)

            if len(selection) != 2: 
                return #évite que cela crash si on oublie de sélectionner deux objets
            

            obj_to_scatter, target_surface = selection[0], selection[1]
            # le 0 est l'objet a scatter et le 1 la surface

            cmds.select(obj_to_scatter, replace=True)
            #ne conserver que l'objet a scatter pour la création du mash


            #---création du mash----
            mash_network = mapi.Network()
            mash_network.createNetwork(
                name="LiveScatter_MASH", geometry="Instancer"
            )#crée le système MASH en mode Instancer

            self.dist_node = mash_network.distribute 
            #Sauvegarde le nom du nœud de contrôle dans votre fenêtre pour le réutiliser aux mouvements suivants.

            #---- lier la surface au réseau mash, donc le selection[1]
            mash_network.meshDistribute(target_surface)


            #-----configuration du mash, incertaine de comment cela fonctionne, fonction prise sur google
            cmds.setAttr(f"{self.dist_node}.arrangement", 4)
            cmds.setAttr(f"{self.dist_node}.meshType", 0)

            

        #----Mise à jour le nombre d'instances en direct
        cmds.setAttr(f"{self.dist_node}.pointCount", scatter_factor)
 
def show_live_scatter():

    global live_scatter

    try:

        live_scatter.close()

    except:

        pass

    live_scatter = LiveScatter()

    live_scatter.show()
 
show_live_scatter()   

 