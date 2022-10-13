from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from JsonReader import JsonReader
from MarkTest import markTest
from BinaryMarker import BinaryMarker
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()
		questions = JsonReader().parseTest("test1.test")
		self.questions = questions
		self.widget = QWidget()
		self.layout = QVBoxLayout(self.widget)
		self.questionWidgets = []
		for question in questions:
			widget = question.makeQuestionWidget(self)
			self.layout.addWidget(widget)
			self.questionWidgets.append(widget)
		self.buttons = QWidget()
		self.buttonsLayout = QHBoxLayout(self.buttons)
		checkButton = QPushButton()
		checkButton.setText("Sprawdź")
		self.buttonsLayout.addWidget(checkButton)
		checkButton.clicked.connect(self.check)
		cleanButton = QPushButton()
		cleanButton.setText("Wyczyść")
		self.buttonsLayout.addWidget(cleanButton)
		cleanButton.clicked.connect(self.clean)
		self.layout.addWidget(self.buttons)
		self.score = QLabel()
		self.layout.addWidget(self.score)
		self.scrollArea = QScrollArea()
		self.scrollArea.setWidget(self.widget)
		self.setCentralWidget(self.scrollArea)
		menuBar = QMenuBar()
		testMenu = QMenu()
		menuBar.addMenu(testMenu)
		loadTestAction = QAction()
		loadTestAction.setText("Ładuj test")
		loadTestAction.triggered.connect(self.loadTest)
		testMenu.addAction(loadTestAction)
		self.setMenuBar(menuBar)
		self.resize(350, 700)

	def getSolutions(self):
		solutions = []
		for widget in self.questionWidgets:
			solutions.append(widget.makeSolution())
		return solutions

	def check(self):
		solutions = self.getSolutions()
		(mark, colors) = markTest(self.questions, solutions, BinaryMarker())
		self.score.setText("%d/%d" % (mark.points, mark.totalPoints))
		self.setColors(colors)

	def setColors(self, colors):
		for i in range(len(self.questions)):
			self.questionWidgets[i].setColors(colors[i])
		
	def clean(self):
		for i in range(len(self.questions)):
			self.questionWidgets[i].clean()

	def loadTest(self):
		print("Load test")