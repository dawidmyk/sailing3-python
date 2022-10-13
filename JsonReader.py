from JsonException import JsonException
from OneChoiceQuestion import OneChoiceQuestion
from OneChoiceSolution import OneChoiceSolution
from MultiChoiceQuestion import MultiChoiceQuestion
from MultiChoiceSolution import MultiChoiceSolution
import json

class JsonReader:
	
	@staticmethod
	def getQuestion(dictionary):
		header = None
		category = None
		possibleAnswers = None
		correctAnswer = None
		correctAnswers = None
		multiChoice = None
		for key in dictionary:
			if key == "header":
				header = dictionary[key]
			elif key == "category":
				category = dictionary[key]
			elif key == "possibleAnswers":
				possibleAnswers = dictionary[key]
			elif key == "correctAnswer":
				correctAnswer = dictionary[key]
				multiChoice = False
			elif key == "correctAnswers":
				correctAnswers = JsonReader.getAnswers(dictionary[key])
				multiChoice = True
			else:
				raise JsonException()
				# tu muszę napisać jaki wyjątek rzucam
		if header == None or category == None or possibleAnswers == None \
		or multiChoice == None:
			raise JsonException()
			# jak wyżej
		if multiChoice:
			return MultiChoiceQuestion(header, category, possibleAnswers, correctAnswers)
		else:
			return OneChoiceQuestion(header, category, possibleAnswers, correctAnswer)
	
	@staticmethod
	def getSolution(dictionary):
		chosenAnswer = None
		chosenAnswers = None
		multiChoice = None
		for key in dictionary:
			if key == "chosenAnswer":
				multiChoice = False
				chosenAnswer = dictionary[key]
			elif key == "chosenAnswers":
				multiChoice = True
				chosenAnswers = JsonReader.getAnswers(dictionary[key])
			else:
				raise JsonException()
		if multiChoice == None:
			raise JsonException()
		if multiChoice:
			return MultiChoiceSolution(chosenAnswers)
		else:
			return OneChoiceSolution(chosenAnswer)
			
	def parseQuestion(self, filename):
		dictionary = JsonReader.readDocument(filename)
		return JsonReader.getQuestion(dictionary)
		
	def parseTest(self, filename):
		array = JsonReader.readDocument(filename)
		questions = list()
		for dictionary in array:
			questions.append(JsonReader.getQuestion(dictionary))
		return questions
	
	def parseSolution(self, filename):
		dictionary = JsonReader.readDocument(filename)
		return JsonReader.getSolution(dictionary)
		
	def parseSolvedTest(self, filename):
		array = JsonReader.readDocument(filename)
		solutions = list()
		for dictionary in array:
			solutions.append(JsonReader.getSolution(dictionary))
		return solutions
		
	@staticmethod
	def readDocument(filename):
		with open(filename) as content:
			return json.load(content)
			
	@staticmethod
	def getAnswers(liste):
		return set(liste)
