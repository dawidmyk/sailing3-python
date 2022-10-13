from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout

class QuestionWidget(QWidget):

	def __init__(self, question, parent):
		super(QuestionWidget, self).__init__(parent)
		self.question = question
		self.header = QLabel()
		self.header.setText(question.header)
		self.layout = QVBoxLayout(self)
		self.layout.addWidget(self.header)