from QuestionWidget import QuestionWidget
from PyQt5.QtWidgets import QButtonGroup

class NormalQuestionWidget(QuestionWidget):

	def __init__(self, question, parent):
		super(NormalQuestionWidget, self).__init__(question, parent)
		self.group = QButtonGroup()
		self.buttons = []

	def create(self):
		for i in range(len(self.buttons)):
			self.buttons[i].setText(self.question.possibleAnswers[i])
			self.group.addButton(self.buttons[i], i + 1)
			self.layout.addWidget(self.buttons[i])
	
	def setColors(self, colors):
		for i in range(len(colors)):
			self.buttons[i].setStyleSheet("background-color: " + colors[i])

	def clean(self):
		self.beginCleaning()
		for i in range(len(self.buttons)):
			self.buttons[i].setStyleSheet("")
			self.buttons[i].setChecked(False)
		self.endCleaning()