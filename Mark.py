class Mark:

	def __init__(self):
		self.points = 0
		self.totalPoints = 0
	
	def add(self, partialMark):
		self.points += partialMark.points
		self.totalPoints += partialMark.totalPoints
