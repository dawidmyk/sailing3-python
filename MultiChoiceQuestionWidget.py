from NormalQuestionWidget import NormalQuestionWidget
from PyQt5.QtWidgets import QCheckBox
from MultiChoiceSolution import MultiChoiceSolution

class MultiChoiceQuestionWidget(NormalQuestionWidget):

	def __init__(self, question, parent):
		super(MultiChoiceQuestionWidget, self).__init__(question, parent)
		for _ in question.possibleAnswers:
			self.buttons.append(QCheckBox())
		self.create()
		self.group.setExclusive(False)

	def makeSolution(self):
		nums = set()
		for i in range(len(self.buttons)):
			if(self.buttons[i].isChecked()):
				nums.add(i + 1)
		return MultiChoiceSolution(nums)

	def beginCleaning(self):
		pass

	def endCleaning(self):
		pass