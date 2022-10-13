from PartialMark import PartialMark

class BinaryMarker:
	
	def mark(self, question, solution):
		if(question.fit(solution)):
			return PartialMark(1, 1)
		return PartialMark(0, 1)
