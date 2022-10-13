from NormalQuestion import NormalQuestion
from MultiChoiceQuestionWidget import MultiChoiceQuestionWidget

class MultiChoiceQuestion(NormalQuestion):
	
	def __init__(self, header, category, possibleAnswers, correctAnswers):
		super(MultiChoiceQuestion, self).__init__(header, category, possibleAnswers)
		self.correctAnswers = correctAnswers
		
	def fit(self, solution):
		return self.correctAnswers == solution.chosenAnswers

	def makeQuestionWidget(self, parent):
		return MultiChoiceQuestionWidget(self, parent)

	def makeColors(self, solution):
		colors = []
		for i in range(len(self.possibleAnswers)):
			j = i + 1
			color = None
			if j in self.correctAnswers and j in solution.chosenAnswers:
				color = "green"
			elif not j in self.correctAnswers and j in solution.chosenAnswers:
				color = "red"
			elif j in self.correctAnswers and not j in solution.chosenAnswers:
				color = "gold"
			else:
				color = "gray"
			colors.append(color)
		return colors