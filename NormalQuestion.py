from Question import Question

class NormalQuestion(Question):

	def __init__(self, header, category, possibleAnswers):
		super(NormalQuestion, self).__init__(header, category)
		self.possibleAnswers = possibleAnswers
