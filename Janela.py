import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        #caracteristicas da janela
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 640
        self.titulo = "Main"
        #botão 1 e suas caracteristica
        botao1 = QPushButton("Ok", self)
        botao1.move(50,500)
        botao1.resize(150,70)
        botao1.setStyleSheet('QPushButton {background-color: #6ec5f1; font: bold}')
        botao1.clicked.connect(self.botao1_click) # Ação de clicar, chamando a função botao1_click()
        # botão 2 e suas caracteristica
        botao2 = QPushButton("Cancelar", self)
        botao2.move(600, 500)
        botao2.resize(150, 70)
        botao2.setStyleSheet('QPushButton {background-color: #6ec5f1; font: bold}')
        botao2.clicked.connect(self.botao2_click)  # Ação de clicar, chamando a função botao1_click()
        #carregando a janela
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    def botao1_click(self):
        print ("Botão Ok foi clicado")
    def botao2_click(self):
        print ("Botão Cancelar foi clicado")
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())