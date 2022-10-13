from NormalQuestion import NormalQuestion
from OneChoiceQuestionWidget import OneChoiceQuestionWidget

class OneChoiceQuestion(NormalQuestion):
	
	def __init__(self, header, category, possibleAnswers, correctAnswer):
		super(OneChoiceQuestion, self).__init__(header, category, possibleAnswers)
		self.correctAnswer = correctAnswer
		
	def fit(self, solution):
		return self.correctAnswer == solution.chosenAnswer

	def makeQuestionWidget(self, parent):
		return OneChoiceQuestionWidget(self, parent)

	def makeColors(self, solution):
		colors = []
		for i in range(len(self.possibleAnswers)):
			j = i + 1
			color = None
			if j == self.correctAnswer and j == solution.chosenAnswer:
				color = "green"
			elif j != self.correctAnswer and j == solution.chosenAnswer:
				color = "red"
			elif j == self.correctAnswer and j != solution.chosenAnswer:
				color = "gold"
			else:
				color = "gray"
			colors.append(color)
		return colors