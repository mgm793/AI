import nltk
import collections
import os
import codecs

path = './dataset/'

def init():
	n = raw_input("Number of most common words: ")
	corpus = CreateCorpus(n)
	print corpus.counts
	# calcVect = CalcVect(corpus.counts)

class CreateCorpus():

	def __init__(self, n):
		self.counts = None
		self.readAndMake(n)

	def readAndMake(self,n):	
		for filename in os.listdir(path):
			f = codecs.open(path + filename,"r",encoding="utf-8")
			text = f.read()
			words = nltk.word_tokenize(text)
			words = [word.lower() for word in words if word.isalpha()]
			if not self.counts:
				self.counts = collections.Counter(words)
			else:
				self.counts += collections.Counter(words)
		self.counts = self.counts.most_common(int(n))
		self.counts = [word[0] for word in self.counts]
			

class CalcVect():

	def __init__(self, vect):
		self.vector = None

		
	def readAndMake(self,vect):
		for filename in os.listdir(path):
			f = codecs.open(path + filename,"r",encoding="utf-8")
			text = f.read()
			words = nltk.word_tokenize(text)
			words = [word.lower() for word in words if word.isalpha() and word in vect]
			counts = collections.Counter(words)
			print counts


init()

