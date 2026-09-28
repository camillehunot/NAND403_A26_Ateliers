from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout,QTextEdit, QPushButton, QMessageBox
 
class MessageBoard(QWidget): #definition de la classe
    def __init__(self): #constructeur self équivalent de this du cpp, le constructeur dans python prend self en paramètre
        super().__init__() # Constructeur de notre parent (super = mot clé générique pour l'héritage)
        self.setWindowTitle("Message board")   #fonction qui existe déjà dans QWidget self(en gros la class messageBoard) appel la fonction setWindoTitle
        self.create_ui()#pas besoin de mettre self ici. permet d'appeler create UI

    #definir une fonction
    def create_ui(self): #premier parametre toujours self dans les class
        print("create ui")
        layout = QVBoxLayout(self)   #container
        title = QLabel("Message board")
        layout.addWidget(title) #permet de ranger le title dans le layout

        # QTextEdit
        texte = QTextEdit(self) 
        layout.addWidget(texte)
 
        # QPushButton
        
        button = QPushButton("test", self) #ajouter un string pour ajouter du texte sur notre bouton
        layout.addWidget(button)
        button.clicked.connect(self.on_click) #permet de connecter le bouton a un évenement, ici c'est activer la fonction on_click
        
        
    def on_click(self):
        print("on click called")
        QMessageBox.information(self, )
        
        # QMessageBox

        


 
def main(): #definition fonction main
    global widget #global permet que la variable widget est accessible partout, permet de garder la variable pour plus tard
    try: #permet de pas les accumuler plus d'une fois
        widget.close()
    except Exception:
        pass

    
    widget = MessageBoard() 
    widget.show()
 
main() #call la fonction main
 