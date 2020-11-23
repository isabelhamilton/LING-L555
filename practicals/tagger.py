import sys
import nltk

class UniTagger:


	def __init__(self, tagged_words):
		self.CndFreqDist = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_words) #a conditional frequency distribution that holds all required information

	def __get_conditions(self):
		return self.CndFreqDist.conditions()


	def __get_pertinent_tags(self, word):
		return [condition for condition in self.__get_conditions() if word in self.__get_keys(condition)]


	def __get_keys(self, condition):
		return self.CndFreqDist[condition].keys()

	def __get_val(self, key, condition):
		return self.CndFreqDist[condition][key]

	def tag(self, word):
		conditions = self.__get_pertinent_tags(word)
		if len(conditions) == 0:
			return "None"
		tag = ""
		max_val = 0
		for condition in conditions:
			temp = self.__get_val(word, condition)
			if max_val < temp:
				max_val = temp
				tag = condition
		return tag

