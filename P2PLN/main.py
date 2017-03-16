import nltk
import collections
import os
import codecs

path = './dataset/'

def init():
	n = raw_input("Number of most common words: ")
	corpus = CreateCorpus(n)
	calcVect = CalcVect(corpus.counts)

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
			f.close()
		self.counts = [str(word[0]) for word in self.counts.most_common(int(n))]
			

class CalcVect():

	def __init__(self, vect):
		self.vector = None
		self.readAndMake(vect)

		
	def readAndMake(self,vect):
		output = open("output.arff","w")
		output.write("@relation training\n\n")
		for v in sorted(vect):
			output.write("@attribute " + v + " numeric\n")
		output.write("@attribute gender {male,female}\n\n@data\n")
		for filename in os.listdir(path):
			gender = filename.split("_")[1]
			counts = []
			f = codecs.open(path + filename,"r",encoding="utf-8")
			text = f.read()
			words = nltk.word_tokenize(text)
			lenW = len(words)
			words = [str(word.lower()) for word in words if word.isalpha() and word in vect]
			counts += collections.Counter(words).most_common()
			counts += [(word , 0) for word in vect if word not in words]
			counts.sort(key=lambda x: x[0])
			counts = [str(word[1]) for word in counts]
			counts = [int(num) / float(lenW) for num in counts]
			for c in counts:
				output.write(str(c)+",")
			output.write(gender+"\n")
			f.close()
		output.close()
init()

