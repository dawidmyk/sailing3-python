from Mark import Mark

def markTest(questionList, solutionList, marker):
	mark = Mark()
	colors = []
	for i in range(len(questionList)):
		mark.add(marker.mark(questionList[i], solutionList[i]))
		colors.append(questionList[i].makeColors(solutionList[i]))
	return (mark, colors)
