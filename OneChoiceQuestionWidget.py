from NormalQuestionWidget import NormalQuestionWidget
from PyQt5.QtWidgets import QRadioButton
from OneChoiceSolution import OneChoiceSolution

class OneChoiceQuestionWidget(NormalQuestionWidget):

	def __init__(self, question, parent):
		super(OneChoiceQuestionWidget, self).__init__(question, parent)
		for _ in question.possibleAnswers:
			self.buttons.append(QRadioButton())
		self.create()

	def makeSolution(self):
		return OneChoiceSolution(self.group.checkedId())

	def beginCleaning(self):
		self.group.setExclusive(False)
	
	def endCleaning(self):
		self.group.setExclusive(True)