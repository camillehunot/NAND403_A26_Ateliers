import random
from maya import cmds
from PySide6.QtWidgets import (
    QFormLayout,
    QGridLayout,
    QLabel,
    QSpinBox,
    QDoubleSpinBox,
    QWidget,
    QPushButton,
    QVBoxLayout,
    
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)
        layout_horizontal = QFormLayout()
        grid = QGridLayout()

        layout.addLayout(layout_horizontal)
        layout.addLayout(grid)

        # choix du nombre d'objet en int
        self.object_number = QSpinBox()
        self.object_number.setRange(1, 100) 
        layout_horizontal.addRow("numbers of objects :", self.object_number)

        # choix pour les valeurs de paramètres en float
        self.number = QDoubleSpinBox()
        self.number.setRange(0, 100)  
        self.number.setValue(1)      # Valeur par défaut
        self.number.setDecimals(2) #determiner le nombre de chiffre après la virgule que l'on veut afficher dans le QDoubleSpinBox

      
        parameters = ["Position X :", "Position Y :", "Position Z :", "Scale :"]
        self.grid_values = {} #initialiser un dictionnaire pour garder les chiffres des paramètres

        grid.addWidget(QLabel("<b> </b>"), 0, 1)
        grid.addWidget(QLabel("<b>Min</b>"), 0, 2)
        grid.addWidget(QLabel("<b>Max</b>"), 0, 3)



        for i, category in enumerate(parameters[:-1]): # -1 car je règle le scale à la fin pour ne pas avoir de problème avec les valeurs min et max
            grid.addWidget(QLabel(category), i + 1, 1)
            min_box = QDoubleSpinBox()
            min_box.setRange(-100, 100) #ajouter un range sinon ca me bloquait a deux chiffres
            min_box.setValue(-10)
            grid.addWidget(min_box, i + 1, 2) # permet de mettre l'input min  dans la grille a la ligne i+1 et la colonne 2

            max_box = QDoubleSpinBox()
            max_box.setRange(-100, 100) #ajouter un range sinon ca me bloquait a deux chiffres
            max_box.setValue(10)
            grid.addWidget(max_box, i + 1, 3)

            self.grid_values[parameters[i]] = {"min": min_box, "max": max_box} # +1 car la première ligne est pour les titres min et max

        
        grid.addWidget(QLabel("Scale :"), 4, 1) # Ligne 4 (après X, Y, Z qui occupent 1, 2, 3)


        #>>>>>>>>>>>>>>>>>>scale valeur min        
        scale_min_box = QDoubleSpinBox()
        scale_min_box.setRange(0.1, 100) 
        scale_min_box.setValue(0.5)
        grid.addWidget(scale_min_box, 4, 2)

        #>>>>>>>>>>>>>>>>>>scale valeur max
        scale_max_box = QDoubleSpinBox()
        scale_max_box.setRange(0.1, 100) 
        scale_max_box.setValue(2)
        grid.addWidget(scale_max_box, 4, 3)
        
        self.grid_values["Scale :"] = {"min": scale_min_box, "max": scale_max_box} #enregistrer les valeurs de scale dans le dictionnaire grid_values
 

  

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)


     

    def create_object(self):

        
        forme = random.choice(["cube", "cylindre", "sphere"])

        number_of_objects = self.object_number.value() #récupérer le nombre d'objets 



        #>>>>>>>>>> Récupérer les valeurs min et max pour chaque paramètre <<<<<<<<<<<<<<<<<<<<<<<<<<<<

        pos_x_min = self.grid_values["Position X :"]["min"].value()
        pos_x_max = self.grid_values["Position X :"]["max"].value()

        pos_y_min = self.grid_values["Position Y :"]["min"].value()
        pos_y_max = self.grid_values["Position Y :"]["max"].value()

        pos_z_min = self.grid_values["Position Z :"]["min"].value()
        pos_z_max = self.grid_values["Position Z :"]["max"].value()

        scale_min = self.grid_values["Scale :"]["min"].value()
        scale_max = self.grid_values["Scale :"]["max"].value()


        #>>>>>>>>>>> création des objets et leur gestion <<<<<<<<<<<
        
        for i in range(number_of_objects):
            ##self.create_random_object(forme) ## je n'Arrivais pas a le faire avec cette ligne donc j'ai utilsiée une autre
            forme = random.choice(["cube", "cylindre", "sphere"])

            if forme == "cube":
                objet = cmds.polyCube()[0]
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
            else:
                objet = cmds.polySphere()[0]

            random_pos_x = random.uniform(pos_x_min, pos_x_max)
            random_pos_y = random.uniform(pos_y_min, pos_y_max)
            random_pos_z = random.uniform(pos_z_min, pos_z_max)
            random_scale = random.uniform(scale_min, scale_max)

            cmds.scale(random_scale, random_scale, random_scale, objet)
            cmds.move(random_pos_x, random_pos_y, random_pos_z, objet)

 


    


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass

    

    tool_window = RandomGenerator()
    tool_window.show()

main()