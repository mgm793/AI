import nltk
import collections
import os
import codecs

class CalcVect():

	def __init__(self, vect,n,path):
		self.vector = None
		self.readAndMake(vect,n,path)

		
	def readAndMake(self,vect,n,path):
		output = open("output_" + n + ".arff","w")
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